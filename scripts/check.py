"""Check the built site: internal links and anchors resolve, content rules hold."""

from __future__ import annotations

import re
import struct
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content"
SITE_URL = f"https://{(ROOT / 'static' / 'CNAME').read_text().strip()}"
EMAIL = "aryavms@outlook.com"
NAV = ["/", "/theses/"]
PAPERS = ROOT / "review" / "papers"
PLACEHOLDERS = ["[AUTHOR", "TO CONFIRM", "TO ADD", "not verified", "TODO", "TBD"]
ARCHIVE = ROOT / "archive" / "theses"
WORDS = (250, 450)


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.ids: set[str] = set()
        self.h2: list[str] = []
        self.h1 = 0
        self._in_h2 = False
        self.meta: dict[str, str] = {}
        self.canonical: list[str] = []
        self.title = ""
        self._in_title = False
        self.link_labels: list[tuple[str, str]] = []
        self._anchor_href: str | None = None
        self._anchor_text = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta" and "content" in a:
            key = a.get("property") or a.get("name")
            if key:
                self.meta[key] = a["content"]
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a.get("href", ""))
        if tag == "title":
            self._in_title = True
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and "href" in a:
            self.links.append(a["href"])
            self._anchor_href = a["href"]
            self._anchor_text = ""
        if tag in ("link", "script", "img", "video", "source") and (a.get("href") or a.get("src")):
            self.links.append(a.get("href") or a.get("src"))
        if tag == "video" and a.get("poster"):
            self.links.append(a["poster"])
        if tag == "source" and a.get("srcset"):
            self.links.append(a["srcset"])
        if tag == "h1":
            self.h1 += 1
        if tag == "h2":
            self._in_h2 = True
            self.h2.append("")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "a" and self._anchor_href is not None:
            self.link_labels.append((self._anchor_href, self._anchor_text))
            self._anchor_href = None
        if tag == "h2":
            self._in_h2 = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._anchor_href is not None:
            self._anchor_text += data
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
        for href, label in p.link_labels:
            u = urlparse(href)
            internal = (not u.scheme and not u.netloc) or u.hostname in (
                urlparse(SITE_URL).hostname,
                f"www.{urlparse(SITE_URL).hostname}",
            )
            if internal and "↗" in label:
                errors.append(f"{rel}: internal link {href} uses an external arrow")
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

    thesis_dirs = [f for f in pages if f.parent.parent == DIST / "theses"]
    redirects = [f for f in thesis_dirs if 'http-equiv="refresh"' in f.read_text(encoding="utf-8")]
    theses = [f for f in thesis_dirs if f not in redirects]
    if len(theses) != 7:
        errors.append(f"expected 7 theses, found {len(theses)}")
    for old in ARCHIVE.glob("*.md"):
        page = DIST / "theses" / old.stem / "index.html"
        if not page.exists():
            errors.append(f"old URL /theses/{old.stem}/ no longer resolves")
    for f in redirects:
        target = re.search(r'url=(/theses/[^/"]+/)"', f.read_text(encoding="utf-8"))
        if not target or resolve(target.group(1)) not in theses:
            errors.append(f"{f.relative_to(DIST)}: redirect target is not a thesis")
    index_links = set(pages[DIST / "theses" / "index.html"].links)
    for f in redirects:
        if f"/theses/{f.parent.name}/" in {link for p in pages.values() for link in p.links}:
            errors.append(f"something links to redirect /theses/{f.parent.name}/")
    for f in theses:
        if f"/theses/{f.parent.name}/" not in index_links:
            errors.append(f"theses index is missing /theses/{f.parent.name}/")
    for f in theses:
        html = f.read_text(encoding="utf-8")
        header = re.search(r'<header class="article-header">(.*?)</header>', html, flags=re.S)
        if not header or "Working draft" in header[1] or "Updated " in header[1]:
            errors.append(f"{f.relative_to(DIST)}: thesis header must omit draft status and updated date")
        if not header or not re.search(r"\b[1-9]\d* min read\b", header[1]):
            errors.append(f"{f.relative_to(DIST)}: reading time missing")
        figures = re.findall(r"<figure.*?</figure>", html, flags=re.S)
        if not any("<img" in fg and "<figcaption>" in fg for fg in figures):
            errors.append(f"{f.relative_to(DIST)}: needs at least one captioned image")
    for f in (CONTENT / "theses").glob("*.md"):
        if f.name == "_index.md":
            continue
        body = f.read_text(encoding="utf-8").split("---\n", 2)[-1]
        body = re.sub(r"^\[\^[^\]]+\]:.*$", " ", body, flags=re.M)
        body = re.sub(r"\[\^[^\]]+\]", "", body)
        prose = re.sub(r"<[^>]+>", " ", re.sub(r"<figure.*?</figure>", " ", body, flags=re.S))
        n = len(re.findall(r"[A-Za-z0-9’'%.,$-]+", prose))
        if not WORDS[0] <= n <= WORDS[1]:
            errors.append(f"{f.relative_to(ROOT)}: {n} words, expected {WORDS[0]} to {WORDS[1]}")
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
        if len(pdfs) != 2 or any(not (DIST / p.lstrip("/")).read_bytes().startswith(b"%PDF-") for p in pdfs):
            errors.append(f"{f.relative_to(DIST)}: needs poster and working paper PDFs")
    for f in pages:
        if re.search(r"<img(?![^>]*\balt=\"[^\"]+\")[^>]*>", f.read_text(encoding="utf-8")):
            errors.append(f"{f.relative_to(DIST)}: image without alt text")

    canonical_urls = set()
    for f, p in pages.items():
        rel = f.relative_to(DIST)
        if f in redirects or rel == Path("404.html"):
            if p.meta.get("robots") != "noindex":
                errors.append(f"{rel}: redirects and the 404 page must be noindex")
            if "og:url" in p.meta:
                errors.append(f"{rel}: must not advertise a social card")
            continue
        url = f"{SITE_URL}/{rel.as_posix().removesuffix('index.html')}"
        canonical_urls.add(url)
        if p.canonical != [url]:
            errors.append(f"{rel}: expected one canonical URL matching {url}")
        expected = {
            "og:site_name": "Arya Shah",
            "og:type": "article" if f in theses or f in research else "website",
            "og:title": p.title,
            "og:description": "Arya Shah" if f == DIST / "index.html" else p.meta.get("description"),
            "og:url": url,
            "og:image": f"{SITE_URL}/social-preview.png?v=2",
            "og:image:alt": "Arya Shah",
            "og:image:type": "image/png",
            "og:image:width": "1200",
            "og:image:height": "630",
            "twitter:card": "summary_large_image",
            "twitter:title": p.title,
            "twitter:description": "Arya Shah" if f == DIST / "index.html" else p.meta.get("description"),
            "twitter:image": f"{SITE_URL}/social-preview.png?v=2",
            "twitter:image:alt": "Arya Shah",
        }
        for key, value in expected.items():
            if not value or p.meta.get(key) != value:
                errors.append(f"{rel}: missing or incorrect {key}")

    image = DIST / "social-preview.png"
    if not image.exists():
        errors.append("social-preview.png: missing")
    else:
        header = image.read_bytes()[:24]
        if (
            len(header) != 24
            or not header.startswith(b"\x89PNG\r\n\x1a\n")
            or struct.unpack("!II", header[16:24]) != (1200, 630)
        ):
            errors.append("social-preview.png: expected a 1200 by 630 PNG")

    try:
        sitemap = ET.parse(DIST / "sitemap.xml")
    except (OSError, ET.ParseError) as exc:
        errors.append(f"sitemap.xml: {exc}")
    else:
        ns = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
        urls = [loc.text for loc in sitemap.findall(f"{ns}url/{ns}loc")]
        if sitemap.getroot().tag != f"{ns}urlset" or set(urls) != canonical_urls or len(urls) != len(canonical_urls):
            errors.append("sitemap.xml: must contain each canonical HTML page once, without redirects or 404")

    robots = DIST / "robots.txt"
    if not robots.exists():
        errors.append("robots.txt: missing")
    else:
        rules = RobotFileParser()
        rules.parse(robots.read_text(encoding="utf-8").splitlines())
        if rules.site_maps() != [f"{SITE_URL}/sitemap.xml"]:
            errors.append("robots.txt: canonical sitemap URL missing or incorrect")
        if any(not rules.can_fetch("*", url) for url in canonical_urls):
            errors.append("robots.txt: a canonical page is blocked")
    if "reading" in " ".join(link.lower() for p in pages.values() for link in p.links):
        errors.append("a Reading link exists")

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
