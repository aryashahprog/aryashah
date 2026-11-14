"""Check the built site: internal links and anchors resolve, content rules hold."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content"
EMAIL = "aryashah@gatech.edu"
NAV = ["/", "/theses/", "/building/"]
PAPERS = ROOT / "review" / "papers"
PLACEHOLDERS = ["[AUTHOR", "TO CONFIRM", "TO ADD", "not verified", "TODO", "TBD"]
THESIS_SECTIONS = ["The claim", "Reasoning", "Where value might accrue", "What would change my mind"]


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.h2: list[str] = []
        self.h1 = 0
        self._in_h2 = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
        if tag in ("link", "script", "img") and (a.get("href") or a.get("src")):
            self.links.append(a.get("href") or a.get("src"))
        if tag == "h1":
            self.h1 += 1
        if tag == "h2":
            self._in_h2 = True
            self.h2.append("")

    def handle_endtag(self, tag):
        if tag == "h2":
            self._in_h2 = False

    def handle_data(self, data):
        if self._in_h2:
            self.h2[-1] += data


def resolve(path: str) -> Path:
    target = DIST / unquote(path).lstrip("/")
    return target / "index.html" if path.endswith("/") or target.is_dir() else target


def main() -> int:
    errors: list[str] = []
    pages = {}
    for f in sorted(DIST.rglob("*.html")):
        p = Page()
        p.feed(f.read_text(encoding="utf-8"))
        pages[f] = p

    for f, p in pages.items():
        rel = f.relative_to(DIST)
        if p.h1 != 1:
            errors.append(f"{rel}: expected one h1, found {p.h1}")
        for href in NAV:
            if href not in p.links:
                errors.append(f"{rel}: nav link {href} missing")
        for href in p.links:
            u = urlparse(href)
            if u.scheme in ("http", "https", "mailto"):
                if u.scheme == "mailto" and u.path != EMAIL:
                    errors.append(f"{rel}: unexpected mailto {href}")
                continue
            base = (
                f
                if not u.path
                else resolve(u.path if u.path.startswith("/") else "/" + str((f.parent / u.path).relative_to(DIST)))
            )
            if not base.exists():
                errors.append(f"{rel}: broken link {href}")
                continue
            if u.fragment and base in pages and u.fragment not in pages[base].ids:
                errors.append(f"{rel}: missing anchor {href}")

    theses = [f for f in pages if f.parent.parent == DIST / "theses"]
    if len(theses) != 12:
        errors.append(f"expected 12 theses, found {len(theses)}")
    for f in theses:
        missing = [s for s in THESIS_SECTIONS if s not in pages[f].h2]
        if missing:
            errors.append(f"{f.relative_to(DIST)}: missing sections {missing}")
        if "Last updated" not in f.read_text(encoding="utf-8"):
            errors.append(f"{f.relative_to(DIST)}: missing last-updated metadata")
    home = pages[DIST / "index.html"]
    if f"mailto:{EMAIL}" not in home.links:
        errors.append("home: mailto link missing")
    if any(re.fullmatch(r"/theses/[^/]+/", link) for link in home.links):
        errors.append("home: should link to the theses index, not individual theses")
    research = [f for f in pages if f.parent.parent == DIST / "research"]
    for f in research:
        url = f"/research/{f.parent.name}/"
        if url not in home.links:
            errors.append(f"home: research page {url} not linked")
        pdfs = [link for link in pages[f].links if link.endswith(".pdf")]
        if not pdfs or any(not (DIST / p.lstrip("/")).read_bytes().startswith(b"%PDF-") for p in pdfs):
            errors.append(f"{f.relative_to(DIST)}: needs a poster PDF")
        if any("paper" in p for p in pdfs):
            errors.append(f"{f.relative_to(DIST)}: links the unreviewed paper PDF")
    for f in pages:
        if re.search(r"<img(?![^>]*\balt=\"[^\"]+\")[^>]*>", f.read_text(encoding="utf-8")):
            errors.append(f"{f.relative_to(DIST)}: image without alt text")
    if "reading" in " ".join(link.lower() for p in pages.values() for link in p.links):
        errors.append("a Reading link exists")

    for pdf in PAPERS.glob("*.pdf"):
        if any(DIST.rglob(pdf.name)):
            errors.append(f"dist: unreviewed paper {pdf.name} is published")
    for f in PAPERS.glob("*.md"):
        text = f.read_text(encoding="utf-8")
        for marker in PLACEHOLDERS:
            if marker.lower() in text.lower():
                errors.append(f"{f.relative_to(ROOT)}: contains placeholder {marker!r}")
        for fig in re.findall(r'src="(figures/[^"]+)"', text):
            if not (f.parent / fig).exists():
                errors.append(f"{f.relative_to(ROOT)}: missing figure {fig}")

    for f in [*CONTENT.rglob("*.md"), *PAPERS.glob("*.md")]:
        text = f.read_text(encoding="utf-8")
        if "\u2014" in text or "---" in text.split("---\n", 2)[-1]:
            errors.append(f"{f.relative_to(ROOT)}: contains an em dash")

    for e in errors:
        print("FAIL", e)
    print(f"Checked {len(pages)} pages: {'ok' if not errors else f'{len(errors)} problems'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
