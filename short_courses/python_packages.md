# Creating Python packages

```{card}

<div class="alert alert-block" style="background-color: #ffffff; border: 1px solid #ccc; padding: 1em; border-radius: 8px;">

**Author:** Sophia Nora (GitHub: [sophianora](https://github.com/sophianora), ORCID ID:[0009-0007-2061-1764](https://orcid.org/0009-0007-2061-1764))

**License:** Creative Commons Attribution-ShareAlike 4.0 International license[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  

</div>

```

## Learning objectives

By the end, you will be able to:

- Put a documented function into a minimal Python package.
- Recognise the package metadata and source-code files.
- Install the package locally and use it from another directory.

## Before you start

Before the session, install Python 3.11 or later and prepare a text editor and terminal. You need basic functions, imports, and terminal navigation; review [virtual environments](python_environments.ipynb) and [functions and docstrings](python_language_features.ipynb) beforehand if needed.

Create an empty `cfrr-package-workshop` directory **outside CfRR_Courses** and open a terminal there. Shell commands run there or in its package subdirectory; Python code blocks are file contents unless stated otherwise.

Before starting the timer, create and activate an environment. On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

After activation, `python` refers to this environment. Before the session, run `python -m pip install --upgrade pip`; internet access is needed for installation.

## 1. Why create a package? 

A package lets you import reusable functions into different projects. Our distribution is named `cfrr-demo-package`; Python imports it as `cfrr_demo_package`. We will create just two files: the Python code and the package configuration.

## 2. Create your package 

From `cfrr-package-workshop/`, run in the terminal:

```bash
mkdir cfrr-demo-package
cd cfrr-demo-package
```

Using your editor, create these files and directories:

```text
cfrr-demo-package/
├── pyproject.toml
└── src/
    └── cfrr_demo_package/
        └── __init__.py
```

In `src/cfrr_demo_package/__init__.py`, put the documented function:

```python
def celsius_to_fahrenheit(celsius):
    """Convert a temperature in degrees Celsius to degrees Fahrenheit."""
    return celsius * 9 / 5 + 32
```

Copy this configuration into the learner project's `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"

[project]
name = "cfrr-demo-package"
version = "0.1.0"
requires-python = ">=3.11"

[tool.setuptools.packages.find]
where = ["src"]
```

Explain only the essentials: `project` supplies the installable name and version; `build-system` selects the tool that prepares the package; the final table tells that tool to find Python packages under `src/`.

## 3. Install and use it 

From the learner package root containing `pyproject.toml`, run in the terminal:

```bash
python -m pip install .
cd ..
python -c "from cfrr_demo_package import celsius_to_fahrenheit; print(celsius_to_fahrenheit(0))"
```

Expected output: `32.0`. `cd ..` moves you outside the package project directory; the import uses the package installed in your active environment.

## 4. Exercise and recap 

While still outside the package directory, repeat the `python -c` command with `100` instead of `0`. Predict the result before running it. Expected output: `212.0`; an optional second input, `-40`, gives `-40.0`.

Recap the workflow: put a function in a package → add metadata → install → import and call it. Ask: which name goes in the installation metadata, and which name goes after `import`?

## Further resources

- [PyPA packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/) — explore package development after this introduction.
- [Writing pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) — look up configuration fields when you need them.
