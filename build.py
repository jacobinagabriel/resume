"""Render resume.html + style.css to resume.pdf using headless Chromium."""

from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).parent
SOURCE = ROOT / "resume.html"
OUTPUT = ROOT / "resume.pdf"


def build() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(SOURCE.resolve().as_uri())
        page.pdf(path=str(OUTPUT), format="A4", print_background=True)
        browser.close()
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    build()
