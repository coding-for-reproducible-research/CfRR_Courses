# Coding for Reproducible Research (CfRR) Courses

This repository contains the **Coding for Reproducible Research (CfRR)** training programme materials from the University of Exeter. The content is published as a Jupyter Book website and is also usable locally (e.g., to run notebooks or preview changes before opening a pull request).

- Website: https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html
- Contact: codingforreproducibleresearch@exeter.ac.uk

## Repository layout

Content is organized as a Jupyter Book (see `_config.yml` and `_toc.yml`), with notebooks/markdown grouped by programme area:

- `home_page.md`: Jupyter Book homepage content.
- `cfrr_program_details/`: Programme-level pages (e.g., About, Code of Conduct, how to use the site).
- `course_homepages/`: Course-category overview pages (Python, R, Unix/Linux, etc.).
- `programme_information/`: Workshop information pages (outlines/details for each workshop).
- `individual_modules/`: Core teaching materials for each module (notebooks, markdown, images).
- `individual_modules/section_landing_pages/`: Per-module landing pages (objectives, prerequisites, overview).
- `short_courses/`: Short/special-topic materials.
- `where_is_my_understanding/`: Self-assessment quiz materials.
- `pathways/`: Notebooks/content describing relationships between courses (e.g., pathway visualizations).
- `data/`: Shared data used to generate parts of the site (e.g., workshop schedule and pathway graphs).
- `resources/`: Shared resources referenced across materials.
- `R_functions/`, `julia_functions/`: Language-specific helper functions used in materials.
- `_static/`, `_templates/`: Jupyter Book static assets and template overrides.
- `.github/workflows/`: CI workflows (build, deploy, accessibility checks).

Key repo files:

- `_config.yml`: Jupyter Book configuration.
- `_toc.yml`: Jupyter Book table of contents.
- `pyproject.toml`: Python dependencies used in CI to build the book.
- `requirements.in`: A lightweight dependency list (kept for convenience; CI uses `pyproject.toml`).
- `CITATION.cff`, `references.bib`: Citation metadata and bibliographic references.

## Finding the source file for a webpage

If you are browsing the published website and want to edit the corresponding source (`.md` or `.ipynb`) locally, you can usually map from the URL path to the repo path:

1) Take the part of the URL after `CfRR_Courses/` and remove the `.html` suffix.
2) Look for a matching source file in the repo with the same path and either a `.md` or `.ipynb` extension.

Examples:

- Website page `.../home_page.html` → `home_page.md`
- Website page `.../contributing/contributing.html` → `contributing/contributing.md` (or `.ipynb` if that page is a notebook)
- Website page `.../pathways/related_courses.html` → `pathways/related_courses.ipynb`

If you cannot find an exact match (some pages are generated/renamed), `_toc.yml` is the source of truth for what files are included in the book and in what structure.

## Getting started

### Browse online

For most users, browsing the published website is the easiest way to use the materials:

https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html

### Run locally (Poetry, matches CI)

CI builds use Python 3.11, so using Python 3.11 locally is recommended as well.

1) Clone the repo:

```bash
git clone https://github.com/coding-for-reproducible-research/CfRR_Courses.git
cd CfRR_Courses
```

2) Install dependencies with Poetry:

```bash
poetry install
```

3) Launch JupyterLab to interact with notebooks:

```bash
poetry run jupyter lab
```

Notes:

- Poetry installs from `pyproject.toml` (the same source used in GitHub Actions).
- If you prefer an activated shell instead of prefixing commands with `poetry run`, use `poetry shell`.

## Build and preview the website

Build the Jupyter Book:

```bash
poetry run jupyter-book build .
```

The generated static site is written to `_build/html/`. To preview locally:

```bash
poetry run python -m http.server --directory _build/html 8000
```

Then open `http://localhost:8000/` in your browser.

## Contributing

Contributions are welcome. See `contributing/` for contribution guidelines and course-development notes. The contributing section is also published here:

https://coding-for-reproducible-research.github.io/CfRR_Courses/contributing/contributing.html

## License

There is no single license that applies to the entire repository. Each module typically includes its own `LICENSE.txt` under `individual_modules/<module_name>/`.

## CI and deployment

This project uses GitHub Actions to build, test, and deploy the website:

- `.github/workflows/build-book.yml`: builds the book on pull requests to `main`.
- `.github/workflows/deploy-book.yml`: builds and deploys `_build/html` to GitHub Pages on pushes to `main` (and on a schedule).
- `.github/workflows/accessibility*.yml`: builds the book and runs accessibility checks (see above).
