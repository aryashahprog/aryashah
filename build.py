"""Build the static site from content/ into dist/."""

from __future__ import annotations

import argparse
import datetime as dt
import itertools
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown.extensions.footnotes import FootnoteExtension

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
SITE_URL = "https://aryashah0.com"
GOATCOUNTER_CODE = "arya"
TEMPLATES = ROOT / "templates"

# Building is kept in content/ but not published; set True to bring it back.
SHOW_BUILDING = False
NAV = [("Home", "/"), ("Working theses", "/theses/")] + ([("Building", "/building/")] if SHOW_BUILDING else [])


@dataclass
class Page:
    meta: dict
    html: str
    slug: str = ""
    related: list[Page] = field(default_factory=list)

    def __getattr__(self, name: str):
        try:
            return self.meta[name]
        except KeyError as exc:
            raise AttributeError(name) from exc


MD_EXTENSIONS = ["smarty", "sane_lists"]
PAPER_EXTENSIONS = [*MD_EXTENSIONS, "tables", "md_in_html"]
NOTES_HEADING = re.compile(r'(<div class="footnote">)\s*<hr ?/?>')


def thesis_extensions() -> list:
    return [
        *MD_EXTENSIONS,
        FootnoteExtension(SUPERSCRIPT_TEXT="[{}]", BACKLINK_TEXT="\u21a9\ufe0e", BACKLINK_TITLE="Back to text"),
    ]


def read(path: Path, extensions: list[str] = MD_EXTENSIONS) -> Page:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} is missing front matter")
    _, front, body = text.split("---\n", 2)
    meta = yaml.safe_load(front) or {}
    html = markdown.markdown(body, extensions=extensions, output_format="html")
    html = NOTES_HEADING.sub(r'\1\n<h2 id="notes">Notes:</h2>', html)
    return Page(meta=meta, html=html, slug=path.stem)


def human_date(value: dt.date) -> str:
    return f"{value:%B} {value.day}, {value.year}"


def link_arrow(url: str) -> str:
    target = urlsplit(url)
    hostname = urlsplit(SITE_URL).hostname
    if target.scheme and target.scheme not in ("http", "https"):
        return "↗"
    return "→" if not target.netloc or target.hostname in (hostname, f"www.{hostname}") else "↗"


def load_theses() -> tuple[dict, list[Page]]:
    index = read(CONTENT / "theses" / "_index.md")
    theses = [read(p, thesis_extensions()) for p in sorted((CONTENT / "theses").glob("*.md")) if p.name != "_index.md"]
    by_slug = {t.slug: t for t in theses}
    for t in theses:
        words = re.findall(r"\b[\w’-]+\b", re.sub(r"<[^>]+>", " ", t.html))
        t.meta["reading_minutes"] = max(1, (len(words) + 219) // 220)
        missing = [s for s in t.meta.get("related", []) if s not in by_slug]
        if missing:
            raise ValueError(f"{t.slug}: unknown related notes {missing}")
        t.related = [by_slug[s] for s in t.meta.get("related", [])]
    replaced = [old for t in theses for old in t.meta.get("replaces", [])]
    clash = set(replaced) & set(by_slug) | {s for s in replaced if replaced.count(s) > 1}
    if clash:
        raise ValueError(f"redirects clash with notes or each other: {sorted(clash)}")
    themes = index.meta["themes"]
    order = {name: i for i, name in enumerate(themes)}
    for t in theses:
        if t.theme not in order:
            raise ValueError(f"{t.slug}: unknown theme {t.theme!r}")
    theses.sort(key=lambda t: (order[t.theme], t.meta.get("order", 0)))
    by_date = sorted(theses, key=lambda t: t.meta["started"], reverse=True)
    years = [(y, list(items)) for y, items in itertools.groupby(by_date, key=lambda t: t.meta["started"].year)]
    return {"page": index, "years": years}, theses


def build(out: Path, base: str = "") -> None:
    base = base.rstrip("/")
    if GOATCOUNTER_CODE and not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", GOATCOUNTER_CODE):
        raise ValueError("GOATCOUNTER_CODE must be a GoatCounter site code, not a URL")
    root_links = re.compile(r'((?:href|src|srcset|poster)="|url=)/(?!/)')
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.filters["date"] = human_date
    env.filters["link_arrow"] = link_arrow
    env.globals["nav"] = NAV
    env.globals["site_url"] = SITE_URL
    env.globals["goatcounter_code"] = GOATCOUNTER_CODE

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(STATIC, out)
    sitemap_urls: list[str] = []

    def render(template: str, dest: str, **ctx) -> None:
        target = out / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        indexable = template not in ("redirect.html", "404.html")
        canonical_url = f"{SITE_URL}/{dest.removesuffix('index.html')}" if indexable else None
        if canonical_url:
            sitemap_urls.append(canonical_url)
        html = env.get_template(template).render(
            analytics_enabled=indexable,
            canonical_url=canonical_url,
            og_type="article" if template in ("thesis.html", "research.html") else "website",
            **ctx,
        )
        if base:
            html = root_links.sub(rf"\g<1>{base}/", html)
        target.write_text(html, encoding="utf-8")

    home = read(CONTENT / "home.md")
    theses_index, theses = load_theses()
    building = read(CONTENT / "building" / "_index.md")
    projects = sorted(
        (read(p) for p in (CONTENT / "building").glob("*.md") if p.name != "_index.md"),
        key=lambda p: p.order,
    )

    render("home.html", "index.html", page=home, current="/")
    render("theses.html", "theses/index.html", current="/theses/", **theses_index)
    for t in theses:
        render("thesis.html", f"theses/{t.slug}/index.html", page=t, current="/theses/")
        for old in t.meta.get("replaces", []):
            render("redirect.html", f"theses/{old}/index.html", target=t, current="/theses/")
    if SHOW_BUILDING:
        render("building.html", "building/index.html", page=building, projects=projects, current="/building/")
    research_index = read(CONTENT / "research" / "_index.md")
    render("research-index.html", "research/index.html", page=research_index, current="/research/")
    research = [read(p) for p in sorted((CONTENT / "research").glob("*.md")) if p.name != "_index.md"]
    for r in research:
        render("research.html", f"research/{r.slug}/index.html", page=r, current="")
    render("404.html", "404.html", current="")
    sitemap = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in sorted(sitemap_urls):
        ET.SubElement(ET.SubElement(sitemap, "url"), "loc").text = url
    ET.indent(sitemap)
    ET.ElementTree(sitemap).write(out / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    (out / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"Built {len(theses)} theses, {len(projects)} projects, {len(research)} research pages into {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    parser.add_argument("--base", default="", help="path prefix when served from a subdirectory, e.g. /aryashah")
    args = parser.parse_args()
    build(args.out, args.base)
