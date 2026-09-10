# Resume

Source of truth for my resume: `resume.html` (content) + `style.css` (layout/design).
`resume.pdf` is the generated, distributable output and is committed so the repo always has a ready-to-share copy.

## Edit

Update `resume.html` for content changes, `style.css` for layout/design changes.

## Rebuild the PDF

One-time setup:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

Regenerate `resume.pdf` after any edit:

```bash
python build.py
```
