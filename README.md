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

### URLs públicas

| URL | Uso |
| --- | --- |
| <https://jacobinagabriel.github.io/resume/> | Página do currículo, com botão de download |
| <https://jacobinagabriel.github.io/resume/gabriel-jacobina.pdf> | Link direto para o PDF (LinkedIn, assinatura de e-mail) |
| <https://jacobinagabriel.github.io/resume/resume.pdf> | Mesmo arquivo, nome interno usado pelo botão |

O PDF é publicado nos dois nomes: `gabriel-jacobina.pdf` para links externos,
onde o nome do arquivo salvo importa, e `resume.pdf` para o botão da página.
