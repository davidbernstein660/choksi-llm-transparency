#!/usr/bin/env python3
from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
PUBLIC = ROOT / "public"

SITE_NAME = "Choksi LLM"
APP_URL = "https://llm.choksillmservice.com"
GITHUB_URL = "https://github.com/davidbernstein660/choksi-llm-transparency"

NAV_LINKS = [
    ("Privacy", "/privacy/"),
    ("Technical", "/privacy/technical/"),
    ("FAQ", "/faq/"),
    ("Source", "/source/"),
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip() + "\n"


def render_inline(text: str) -> str:
    code_tokens: list[str] = []

    def code_repl(match: re.Match[str]) -> str:
        code_tokens.append(f"<code>{html.escape(match.group(1))}</code>")
        return f"@@CODE{len(code_tokens) - 1}@@"

    text = re.sub(r"`([^`]+)`", code_repl, text)
    text = html.escape(text)

    def link_repl(match: re.Match[str]) -> str:
        label = match.group(1)
        href = html.escape(match.group(2), quote=True)
        return f'<a href="{href}">{label}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)

    for idx, token in enumerate(code_tokens):
        text = text.replace(f"@@CODE{idx}@@", token)

    return text


def parse_blocks(text: str) -> list[tuple[str, object]]:
    blocks: list[tuple[str, object]] = []
    paragraph: list[str] = []
    list_type: str | None = None
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(("p", " ".join(part.strip() for part in paragraph if part.strip())))
            paragraph = []

    def flush_list() -> None:
        nonlocal list_type, list_items
        if list_type and list_items:
            blocks.append((list_type, list_items[:]))
        list_type = None
        list_items = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()

        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            flush_paragraph()
            flush_list()
            blocks.append((f"h{len(heading.group(1))}", heading.group(2).strip()))
            continue

        ul = re.match(r"^\s*-\s+(.*)$", line)
        if ul:
            flush_paragraph()
            if list_type not in (None, "ul"):
                flush_list()
            list_type = "ul"
            list_items.append(ul.group(1).strip())
            continue

        ol = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if ol:
            flush_paragraph()
            if list_type not in (None, "ol"):
                flush_list()
            list_type = "ol"
            list_items.append(ol.group(1).strip())
            continue

        if line.lstrip().startswith("<"):
            flush_paragraph()
            flush_list()
            blocks.append(("raw", line))
            continue

        if list_type:
            flush_list()
        paragraph.append(line)

    flush_paragraph()
    flush_list()
    return blocks


def render_blocks(blocks: list[tuple[str, object]]) -> str:
    rendered: list[str] = []
    for kind, value in blocks:
        if kind.startswith("h"):
            rendered.append(f"<{kind}>{render_inline(str(value))}</{kind}>")
        elif kind == "p":
            rendered.append(f"<p>{render_inline(str(value))}</p>")
        elif kind == "ul":
            items = "".join(f"<li>{render_inline(item)}</li>" for item in value)  # type: ignore[arg-type]
            rendered.append(f"<ul>{items}</ul>")
        elif kind == "ol":
            items = "".join(f"<li>{render_inline(item)}</li>" for item in value)  # type: ignore[arg-type]
            rendered.append(f"<ol>{items}</ol>")
        elif kind == "raw":
            rendered.append(str(value))
    return "\n      ".join(rendered)


def split_markdown_sections(text: str) -> tuple[str | None, str | None, list[str], dict[str, list[str]]]:
    title: str | None = None
    eyebrow: str | None = None
    intro: list[str] = []
    sections: dict[str, list[str]] = {}
    current: str | None = None

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if match := re.match(r"^#\s+(.*)$", line):
            if title is None:
                title = match.group(1).strip()
                continue
        if match := re.match(r"^##\s+(.*)$", line):
            heading = match.group(1).strip()
            if eyebrow is None:
                eyebrow = heading
                current = None
                continue
            current = heading
            sections[current] = []
            continue
        if match := re.match(r"^###\s+(.*)$", line):
            current = match.group(1).strip()
            sections[current] = []
            continue

        target = sections[current] if current else intro
        target.append(line)

    return title, eyebrow, intro, sections


def parse_link_list(lines: list[str]) -> list[tuple[str, str]]:
    links: list[tuple[str, str]] = []
    for line in lines:
        match = re.match(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)\s*$", line)
        if match:
            links.append((match.group(1), match.group(2)))
    return links


def extract_paragraphs(lines: list[str]) -> list[str]:
    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if not line.strip():
            if current:
                paragraphs.append(" ".join(part.strip() for part in current))
                current = []
            continue
        if re.match(r"^\s*-\s+", line) or re.match(r"^\s*\d+\.\s+", line):
            continue
        current.append(line)
    if current:
        paragraphs.append(" ".join(part.strip() for part in current))
    return paragraphs


def article_shell(*, title: str, description: str, body: str, current_nav: str) -> str:
    nav = "\n        ".join(
        f'<a href="{href}"{" aria-current=\"page\"" if label == current_nav else ""}>{label}</a>'
        for label, href in NAV_LINKS
    )
    return f"""<!-- Generated by scripts/build_site.py. Do not edit public/*.html by hand. -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description, quote=True)}">
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <header class="site-header">
    <div class="wrap nav">
      <a class="brand" href="/">{SITE_NAME}</a>
      <nav class="nav-links" aria-label="Primary">
        {nav}
      </nav>
    </div>
  </header>

  <main class="section">
    <article class="wrap prose">
      {body}
    </article>
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <p>{SITE_NAME}</p>
      <nav class="footer-links" aria-label="Footer">
        <a href="/">Home</a>
        <a href="/privacy/">Privacy</a>
        <a href="/privacy/technical/">Technical</a>
        <a href="/faq/">FAQ</a>
        <a href="/source/">Source</a>
      </nav>
    </div>
  </footer>
</body>
</html>
"""


def render_article_page(source_name: str, output_path: Path, page_title: str, description: str, nav_name: str) -> None:
    text = read_text(CONTENT / source_name)
    blocks = parse_blocks(text)
    title = None
    meta = None
    body_blocks: list[tuple[str, object]] = []

    for kind, value in blocks:
        if kind == "h1" and title is None:
            title = str(value)
            continue
        if kind == "p" and meta is None and str(value).startswith("Last updated: "):
            meta = str(value)
            continue
        body_blocks.append((kind, value))

    fragments = [
        f'<p class="eyebrow">{render_inline(title or page_title)}</p>',
        f"<h1>{render_inline(title or page_title)}</h1>",
    ]
    if meta:
        fragments.append(f'<p class="meta">{render_inline(meta)}</p>')
    fragments.append(render_blocks(body_blocks))
    body = "\n      ".join(fragment for fragment in fragments if fragment)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(article_shell(title=page_title, description=description, body=body, current_nav=nav_name), encoding="utf-8")


def render_homepage() -> None:
    text = read_text(CONTENT / "homepage.md")
    title, eyebrow, intro_lines, sections = split_markdown_sections(text)
    intro_paragraphs = extract_paragraphs(intro_lines)
    primary_actions = parse_link_list(sections.get("Primary Actions", []))
    checklist = [item for _, items in [("Before You Use It", sections.get("Before You Use It", []))] for item in [re.sub(r"^\s*-\s+", "", line).strip() for line in items if re.match(r"^\s*-\s+", line)]]

    card_titles = [
        "Plain-Language Summary",
        "Technical Review",
        "Open Source Review",
    ]
    cards_html: list[str] = []
    for section_title in card_titles:
        lines = sections.get(section_title, [])
        paragraphs = extract_paragraphs(lines)
        links = parse_link_list(lines)
        link_html = ""
        if links:
            label, href = links[0]
            link_html = f'<p><a href="{html.escape(href, quote=True)}">{render_inline(label)}</a></p>'
        cards_html.append(
            f"""<article class="card">
          <h2>{render_inline(section_title)}</h2>
          <p>{render_inline(paragraphs[0] if paragraphs else "")}</p>
          {link_html}
        </article>"""
        )

    legal_paragraphs = extract_paragraphs(sections.get("Not a Legal Policy", []))

    button_classes = ["primary", "strong", "strong", ""]
    buttons = []
    for idx, (label, href) in enumerate(primary_actions):
        extra = button_classes[idx] if idx < len(button_classes) else ""
        class_names = "button" if not extra else f"button {extra}"
        class_attr = f' class="{class_names}"'
        buttons.append(f'<a{class_attr} href="{html.escape(href, quote=True)}">{render_inline(label)}</a>')

    checklist_html = "".join(f"<li>{render_inline(item)}</li>" for item in checklist)

    body = f"""<section class="hero">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">{render_inline(eyebrow or "Privacy & Transparency")}</p>
          <h1>{render_inline(intro_paragraphs[0] if intro_paragraphs else title or SITE_NAME)}</h1>
          <p class="lede">{render_inline(intro_paragraphs[1] if len(intro_paragraphs) > 1 else "")}</p>
          <p class="hero-note">{render_inline(intro_paragraphs[2] if len(intro_paragraphs) > 2 else "")}</p>
          <div class="button-row">
            {' '.join(buttons)}
          </div>
        </div>
        <aside class="panel">
          <h2>Before you use it</h2>
          <ul class="checklist">
            {checklist_html}
          </ul>
          <p><a href="{GITHUB_URL}">Open the public GitHub repo</a></p>
        </aside>
      </div>
    </section>

    <section class="section">
      <div class="wrap cards">
        {' '.join(cards_html)}
      </div>
    </section>

    <section class="section section-muted">
      <div class="wrap narrow">
        <h2>Not a legal policy</h2>
        <p>{render_inline(legal_paragraphs[0] if legal_paragraphs else "")}</p>
      </div>
    </section>"""

    nav = "\n        ".join(
        f'<a href="{href}">{label}</a>' for label, href in NAV_LINKS
    )
    html_text = f"""<!-- Generated by scripts/build_site.py. Do not edit public/*.html by hand. -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{SITE_NAME}</title>
  <meta name="description" content="Plain-language privacy and transparency information for the {SITE_NAME} service.">
  <link rel="stylesheet" href="/assets/site.css">
</head>
<body>
  <header class="site-header">
    <div class="wrap nav">
      <a class="brand" href="/">{SITE_NAME}</a>
      <nav class="nav-links" aria-label="Primary">
        {nav}
      </nav>
    </div>
  </header>

  <main>
    {body}
  </main>

  <footer class="site-footer">
    <div class="wrap footer-grid">
      <p>{SITE_NAME}</p>
      <nav class="footer-links" aria-label="Footer">
        <a href="/privacy/">Privacy</a>
        <a href="/privacy/technical/">Technical</a>
        <a href="/faq/">FAQ</a>
        <a href="/source/">Source</a>
        <a href="{GITHUB_URL}">GitHub</a>
        <a href="{APP_URL}">Access the App</a>
      </nav>
    </div>
  </footer>
</body>
</html>
"""
    (PUBLIC / "index.html").write_text(html_text, encoding="utf-8")


def main() -> None:
    render_homepage()
    render_article_page(
        "privacy-summary.md",
        PUBLIC / "privacy" / "index.html",
        "Privacy & Transparency | Choksi LLM",
        "Plain-language privacy and transparency summary for the Choksi LLM service.",
        "Privacy",
    )
    render_article_page(
        "privacy-technical.md",
        PUBLIC / "privacy" / "technical" / "index.html",
        "Technical Privacy Document | Choksi LLM",
        "Public-safe technical privacy reference for the Choksi LLM service.",
        "Technical",
    )
    render_article_page(
        "faq.md",
        PUBLIC / "faq" / "index.html",
        "FAQ | Choksi LLM",
        "Frequently asked questions about privacy and data handling for the Choksi LLM service.",
        "FAQ",
    )
    render_article_page(
        "source-review.md",
        PUBLIC / "source" / "index.html",
        "Source Code and Review | Choksi LLM",
        "Source code and technical review guidance for the Choksi LLM service.",
        "Source",
    )


if __name__ == "__main__":
    main()
