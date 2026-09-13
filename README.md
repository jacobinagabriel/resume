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

## Publicação

O site é publicado no GitHub Pages pelo workflow `.github/workflows/pages.yml`,
a cada push na `master`:

<https://jacobinagabriel.github.io/resume/>

O workflow regenera o PDF a partir de `resume.html` antes de publicar, então o
`resume.pdf` do site está sempre em sincronia com a fonte. O botão "Baixar PDF"
aparece apenas no site — a regra `@media print` o remove do PDF gerado.
