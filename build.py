"""Build the static site from content/ into dist/."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
from dataclasses import dataclass, field
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "content"
STATIC = ROOT / "static"
TEMPLATES = ROOT / "templates"

NAV = [("Home", "/"), ("Working theses", "/theses/"), ("Building", "/building/")]


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


def read(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path} is missing front matter")
    _, front, body = text.split("---\n", 2)
    meta = yaml.safe_load(front) or {}
    html = markdown.markdown(body, extensions=["smarty", "sane_lists"], output_format="html")
    return Page(meta=meta, html=html, slug=path.stem)


def human_date(value: dt.date) -> str:
    return f"{value:%B} {value.day}, {value.year}"


def load_theses() -> tuple[dict, list[Page]]:
    index = read(CONTENT / "theses" / "_index.md")
    theses = [read(p) for p in sorted((CONTENT / "theses").glob("*.md")) if p.name != "_index.md"]
    by_slug = {t.slug: t for t in theses}
    for t in theses:
        missing = [s for s in t.meta.get("related", []) if s not in by_slug]
        if missing:
            raise ValueError(f"{t.slug}: unknown related notes {missing}")
        t.related = [by_slug[s] for s in t.meta.get("related", [])]
    themes = index.meta["themes"]
    order = {name: i for i, name in enumerate(themes)}
    for t in theses:
        if t.theme not in order:
            raise ValueError(f"{t.slug}: unknown theme {t.theme!r}")
    theses.sort(key=lambda t: (order[t.theme], t.meta.get("order", 0)))
    grouped = [(name, [t for t in theses if t.theme == name]) for name in themes]
    return {"page": index, "groups": grouped}, theses


def build(out: Path) -> None:
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.filters["date"] = human_date
    env.globals["nav"] = NAV

    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(STATIC, out)

    def render(template: str, dest: str, **ctx) -> None:
        target = out / dest
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(env.get_template(template).render(**ctx), encoding="utf-8")

    home = read(CONTENT / "home.md")
    theses_index, theses = load_theses()
    featured = sorted((t for t in theses if t.meta.get("featured")), key=lambda t: t.featured)
    building = read(CONTENT / "building" / "_index.md")
    projects = sorted(
        (read(p) for p in (CONTENT / "building").glob("*.md") if p.name != "_index.md"),
        key=lambda p: p.order,
    )

    render("home.html", "index.html", page=home, featured=featured, current="/")
    render("theses.html", "theses/index.html", current="/theses/", **theses_index)
    for t in theses:
        render("thesis.html", f"theses/{t.slug}/index.html", page=t, current="/theses/")
    render("building.html", "building/index.html", page=building, projects=projects, current="/building/")
    render("404.html", "404.html", current="")
    print(f"Built {len(theses)} theses, {len(projects)} projects into {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist")
    build(parser.parse_args().out)
