"""Typeset review/papers/*.md into PDFs beside their sources, inlining figures from review/papers/figures/.

review/ is not copied into dist, so these PDFs are not served by the site.
"""

from __future__ import annotations

import base64
import mimetypes
import re
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "review" / "papers"
sys.path.insert(0, str(ROOT))

from build import PAPER_EXTENSIONS, TEMPLATES, read  # noqa: E402

FOOTER = (
    "<div style=\"width:100%;font-family:Arial,'Liberation Sans',sans-serif;font-size:8pt;"
    'color:#000;padding:0 1in;display:flex;justify-content:space-between">'
    "<span>{running}</span><span class=pageNumber></span></div>"
)


def inline_figures(html: str) -> str:
    def data_uri(match: re.Match) -> str:
        path = PAPERS / match.group(1)
        mime = mimetypes.guess_type(path.name)[0]
        return f'src="data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"'

    return re.sub(r'src="(figures/[^"]+)"', data_uri, html)


def main() -> None:
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    chrome = shutil.which("google-chrome") or shutil.which("chromium")
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=chrome) if chrome else p.chromium.launch()
        for source in sorted(PAPERS.glob("*.md")):
            page = read(source, PAPER_EXTENSIONS)
            page.html = inline_figures(page.html)
            target = PAPERS / page.pdf
            tab = browser.new_page()
            tab.set_content(env.get_template("research-print.html").render(page=page), wait_until="load")
            tab.pdf(
                path=str(target),
                format="Letter",
                print_background=True,
                display_header_footer=True,
                header_template="<span></span>",
                footer_template=FOOTER.format(running=page.running_title),
                margin={"top": "0.85in", "bottom": "0.85in", "left": "1in", "right": "1in"},
            )
            tab.close()
            print(f"Wrote {target.relative_to(ROOT)}")
        browser.close()


if __name__ == "__main__":
    main()
