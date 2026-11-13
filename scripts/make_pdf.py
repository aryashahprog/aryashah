"""Typeset content/research/*.md into the working paper PDFs under static/research/."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from build import CONTENT, MANUSCRIPT_EXTENSIONS, STATIC, TEMPLATES, human_date, read  # noqa: E402

FOOTER = (
    "<div style=\"width:100%;font-family:Arial,'Liberation Sans',sans-serif;font-size:8pt;"
    'color:#000;padding:0 1in;display:flex;justify-content:space-between">'
    "<span>{status}</span><span><span class=pageNumber></span> / <span class=totalPages></span></span></div>"
)


def main() -> None:
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.filters["date"] = human_date
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        for source in sorted((CONTENT / "research").glob("*.md")):
            page = read(source, MANUSCRIPT_EXTENSIONS)
            target = STATIC / page.pdf.lstrip("/")
            tab = browser.new_page()
            tab.set_content(env.get_template("research-print.html").render(page=page), wait_until="load")
            tab.pdf(
                path=str(target),
                format="Letter",
                print_background=False,
                prefer_css_page_size=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=FOOTER.format(status=page.status),
                margin={"top": "0.9in", "bottom": "0.9in", "left": "1in", "right": "1in"},
            )
            tab.close()
            print(f"Wrote {target.relative_to(ROOT)}")
        browser.close()


if __name__ == "__main__":
    main()
