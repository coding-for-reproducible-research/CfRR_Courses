# Data Science Project Best Practices
This guide provides a comprehensive reference for best practices in conducting reproducible research using Python, specifically for data science projects with a focus on research applications.

The goal of this document is to offer a regularly updated resource that outlines approaches, tools, and methodologies that can help ensure the reproducibility, transparency, and overall quality of your research outcomes. By adopting these practices, you can facilitate collaboration, increase the reliability of your findings, and make it easier for others to understand and build upon your work.

While it is not essential to follow every recommendation to the letter, thoughtfully considering and incorporating the practices discussed here can significantly improve the reproducibility, usability, and interpretability of your research.

## Table of Contents

- [Quick Start](#quick-start)
- [Language: Python](#language-python)
- [Version Control: Git](#version-control-git)
- [Project Structure](#project-structure)
- [README: README.md](#readme-readmemd)
- [Project Config: TOML](#project-config-toml)
- [IDE: VSCode](#ide-vscode)
- [Packaging and Dependency Management: Poetry](#packaging-and-dependency-management-poetry)
- [Code Formatter: Ruff](#code-formatter-ruff)
- [Tests: Pytest](#tests-pytest)
- [Data](#data)
- [Examples](#examples)
- [Scripts](#scripts)

---

## Quick Start
Most of the instructions in this guide require use of the commandline interface in a Unix based system (Mac and Linux). For use with Windows first install Gitbash via [git for windows](https://gitforwindows.org).
Where `{project-name}` is referenced, replace this with the name of your project *without* the curly braces.


To get started you will need to make sure [Python](#language-python), [Git](#version-control-git) and [Poetry](#packaging-and-dependency-management-poetry) are installed.
Python and Git come pre-installed on both Mac and Linux systems, and Git is installed as part of Git For Windows, but Windows users will need to [download](https://www.python.org/downloads/) and install Python.
You will need to additionally install Poetry, which can be done from the [website](https://python-poetry.org/) or by running
```shell
curl -sSL https://install.python-poetry.org | python -
```
from the command line. Then run
```
poetry config virtualenvs.in-project true
```
to configure virtual environments to be built and stored within the project root directory.

### Creating a new project
To create a new project open the command line tool for your system in the desired parent directory for the project. Then run:
```shell
poetry new --src {project-name}
```
Now change directory into the newly created project using:
```shell
cd {project-name}
```
From here you will have a basic project structure complete with a basic `pyproject.toml` and empty `README.md` file:
```shell
{project-name}
├── pyproject.toml
├── README.md
├── src
│   └── {project-name}
│       └── __init__.py
└── tests
    └── __init__.py
```
You can now run:
```shell
poetry init
```
Which will walk you through some basic configuration and addition of dependencies to the project.
And finally:
```shell
poetry install
```
which will build the virtual environment containing the dependencies, and install your new `{project-name}` project also allowing you to easily manage imports of the project code.

Additional libraries can then be added later using:
```shell
poetry add {package-name}
```

### Writing Code:
We recommend doing the main code development in [VSCode](#ide-vscode), instructions for installation of which can be found [here](https://code.visualstudio.com/download). It should recommend selecting the locally created `.venv/` as the project interpreter. 

Core project code can be added to a new `module_name.py` file in `src/{project-name}/module_name.py` and then functions, classes and values from that module can be imported into other files using:

```python
from {project-name}.module_name import function_name
```

For writing code which is intended to be interacted with in some way or produces visualisations we recommend using jupyter notebooks which can be installed using:
```shell
poetry add jupyterlab
```
and creating a new file with the file extension `.ipynb`. It is recommended to add a new directory to the project root to contain these notebooks:
```shell
mkdir notebooks
```
Source code can then be imported into them just like with a `.py` file using
```python
from {project-name}.module_name import function_name
```
There is an [extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) for jupyter notebooks in VSCode that allows notebooks to be written and run from within the VSCode environment. 

### Committing Changes:
Now is a good time to add a boilerplate `.gitignore` file, to keep non-essential and auto-generated files from being added to the remote repository:
```shell
curl https://www.toptal.com/developers/gitignore/api/python,jupyternotebooks > .gitignore
```
(generated by [toptal.com](https://www.toptal.com/developers/gitignore))
and make your first git commit: 
```shell
git add -A
git commit -m "initial commit containing basic project structure"
```
See the version control [section](#version-control-git) for more on git and configuring a remote repository.

You are now set up and ready to go. The rest of this document outlines the tools discussed here and others in greater detail and should be used as a reference. 

# Language: Python
[installation](https://www.python.org/downloads/) · [basics](https://wiki.python.org/moin/BeginnersGuide/Programmers) · [course](https://link-to-courst-tbc)

Python is a popular, high-level programming language known for its readability and versatility. It’s widely used in fields like web development, data science, automation, and artificial intelligence. Python’s simple syntax and vast ecosystem of libraries make it a go-to choice for both beginners and professionals looking to build efficient, scalable applications.

Python is pre-installed on most macOS and Linux systems, meaning users can typically start using it right away from the terminal. However, on Windows, Python usually needs to be installed manually. Windows users can download it from the official Python [website](https://www.python.org/) and should ensure to check the box to "Add Python to PATH" during installation for easy access from the command line.

## Version Control: Git
[installation](https://git-scm.com/downloads) · [basics](https://git-scm.com/doc) · [course](https://link-to-course-tbc)

Git is a widely-used version control system that helps developers track changes in code, collaborate with others, and manage project history efficiently. Git enables branching, merging, and rollback features, making it essential for team-based development and large projects.

Git is often pre-installed on macOS and Linux systems, allowing users to start using it from the terminal. On Windows, Git usually needs to be installed manually. Windows users can download it from the official Git [website](https://git-scm.com/downloads) and should choose "Git Bash" for an enhanced command-line experience.

### Setting Up GitHub
To host and share your repositories online, you can use GitHub, a popular remote hosting platform for Git repositories.

1. **Create a GitHub Account**:  
   - Visit [GitHub](https://github.com/) and sign up for a free account.  
   - Set up your profile, including a username, email, and password.  

2. **Create a Remote Repository**:  
   - Log in to your GitHub account.  
   - Click on the **+** icon in the top-right corner and select **New repository**.  
   - Name your repository and optionally add a description.  
   - Choose to make it public or private.  
   - Initialize the repository with a README if desired, then click **Create repository**.  

3. **Link a Local Repository to GitHub**:  
   After setting up a local Git repository, link it to the remote GitHub repository:  
   ```bash
   git remote add origin https://github.com/your-username/your-repository.git
   git branch -M main
   git push -u origin main
   ```
   Replace your-username and your-repository with your GitHub username and repository name.

4. **Push Changes to GitHub**:  
   Use the following commands to commit and push changes:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push
   ```

### Excluding Files: .gitignore
A .gitignore file is a simple text file used in Git repositories to specify which files and directories should be ignored by Git. This is essential for excluding unnecessary files (like build artifacts, compiled code, and sensitive information) from version control, keeping the repository clean and reducing clutter. By listing patterns in .gitignore, you ensure that specified files won’t be tracked, staged, or committed. Common entries include temporary files, system files, and virtual environment directories (e.g., .venv/, *.log, __pycache__/).

A lot of the content for the `.gitignore` is standard boilerplate which does not change between projects, and there are useful [generators](https://www.toptal.com/developers/gitignore/) to help build comprehensive files. An example `.gitignore` file has been included [here](./.gitignore).

There are also online resources for generating .gitignore files such as [toptal.com](https://www.toptal.com/developers/gitignore), where you can search operating system, IDEs or programming languages you are using and generate a boilerplate .gitignore to exclude associate unwanted files. 

## Project Structure

A well-organized project structure is key to keeping code manageable, especially as a project grows. This layout provides a clear separation of examples, scripts, source code, tests, and configuration files.

```shell
{project-name}
├── examples
│   └── example_notebook.ipynb
├── scripts
│   └── example_script.py
├── src
│   ├── {project-name}
│   │   ├── __init__.py
│   │   └── example_module.py
│   └── scripts
│       └── example_script.py
├── tests
│   └── test_example_module.py
├── .vscode
│   └── settings.json
├── .git
│   └── ... git generated files ...
├── .venv
│   └── ... venv/Poetry generated files ...
├── config.toml
├── pyproject.toml
├── .gitignore
└── README.md
```

- **examples/**: Contains example notebooks or usage files to demonstrate project functionality.
- **scripts/**: Holds scripts for tasks like preprocessing, data downloading, or automation.
- **src/**: Stores the main source code of the project. The folder `{project-name}` matches the project name and includes the core modules.
- **tests/**: Includes test files to validate the code in `src/`.
- **.vscode/**: contains VSCode settings specific to this project.
- **.venv/**: contains the venv specific to this project.
- **config.toml**: Configuration file for project settings.
- **pyproject.toml**: Defines project dependencies and configurations, especially when using tools like Poetry.
- **.gitignore**: Defines what is and is not to be included in the git repository fot the project.
- **README.md**: Provides an overview of the project, setup instructions, and usage examples.

There will be some additional files created through use of [git](#version-control-git) and [VSCode](#ide-vscode).

NOTE: files beginning `.` are hidden files and will not appear unless showing hidden files is specified, i.e. using:
```shell
ls -A
```

## README: README.md
A well-structured README file is essential for providing users with clear instructions about the project. It should give an overview of the project, installation steps, usage instructions, and contribution guidelines. README.md file should be written in markdown, and contain basic project information, installation instructions and links to associated publications.

```markdown
# {Project Name}

## Description
Briefly describe the project, its purpose, and the problem it solves.

## Installation
Instructions for installing the project and setting up the environment.

```shell
pip install {project-name}
```​

## Publication
- Link any associated publication here

## Contact
- Firstname Lastname: exampleemail@domain.com
```

## Project Config: TOML
Configuration file for managing and setting parameters and configuration features which may need to be altered or changed by a user. The .toml file format is commonly used for managing project configurations in Python. It provides a human-readable and easily editable way configure settings.

example configuration file:
```shell
[database]
host = "localhost"
port = 5432
user = "admin"
password = "password"

[logging]
level = "DEBUG"
file = "app.log"

[api credentials]
username = "first.last@exeter.ac.uk"
password = "VQf>:aK/@hgbRj!8?xPq6Y"

[paths]
data_directory = "/path/to/data/directory"
```

which can be loaded and its used:

```python
import toml

# Load the configuration file
config = toml.load('{project_root}/config.toml')

# Access values from the config
database_host = config['database']['host']
database_port = config['database']['port']
logging_level = config['logging']['level']
```

NOTE: If including api credentials, then this file should be added to the `.gitignore` and not included in the github remote repository.


## IDE: VSCode
[installation](https://code.visualstudio.com/Download) · [basics](https://code.visualstudio.com/docs) · [course](https://link-to-courst-tbc)

Visual Studio Code (VSCode) is a popular, free, and open-source code editor developed by Microsoft. It’s known for its lightweight nature, speed, and rich feature set, including debugging support, integrated Git control, extensions, and language support. VSCode is highly customizable, with a wide range of extensions available to enhance functionality, making it an excellent choice for Python, web development, data science, and many other programming tasks.

VSCode can be installed on all major platforms (Windows, macOS, Linux) and is often used with Python via the Python extension, which provides features like IntelliSense, code linting, and environment management.

## Packaging and Dependency Management: Poetry
[installation](https://python-poetry.org/docs/#installation) · [official documentation](https://python-poetry.org/docs/) · [tutorial](https://python-poetry.org/docs/basic-usage/)

Poetry is a powerful dependency manager and build tool for Python projects, streamlining the process of creating, configuring, and maintaining project environments. It simplifies dependency management, ensuring reproducible builds and enabling easier project collaboration.

Poetry is compatible with most operating systems, and it integrates seamlessly with virtual environments (venvs), allowing isolated, self-contained environments for projects.

The project configuration is stored in the file `pyproject.toml`, which can be configured manually. Otherwise Poetry provides a set of commands to build and manage this file interactively:

### Setting Up a New Project

1. **Create a Blank Project**

   Navigate to where you want to store your project and run:
   ```shell
   poetry new --src {project-name}
   ```

2. **Basic Poetry Configuration in Project Root**
   Navigate into your project directory:
   ```shell
   cd {project-name}
   ```
   and run:
   ```shell
   poetry init
   ```
   This command will guide you through setting up your project’s metadata and initial dependencies.

3. **Configuring Virtual Environments to be Created in the Project Root**
   We recommend configuring Poetry to create virtual environments within the project directory, as this ensures the smoothest integration with VSCode (especially if using VSCode to write Jupyter notebooks). To set this configuration:
   ```shell
   poetry config virtualenvs.in-project true
   ```
   This will cause the virtual environment to be created in a `.venv` folder inside your project root, making it easier to manage and locate dependencies. This configuration only needs to be set once and the desired behaviour will be set for all future Poetry projects.

   NOTE: The `.venv/` directory should be added to the `.gitignore` and not included in the remote git repository, just check there is a line `.venv/` somewhere in the .gitignore file.

4. **Installing the Environment:**

   Once the basic project is configured the environment can be installed by running:
   ```shell
   poetry install
   ```
   from the project root directory. This does several things:

      1) Creates the venv and adds the files to `.venv/`
      2) Installs the dependencies specified in the `pyproject.toml` file to the venv.
      3) Installs the current project in *editable* mode. This allows you to import your own code, stored in `src/{project-name}/` using:
         ```python
         from project-name.module import feature
         ```
         without relying on relative imports, and instantly updates the virtual environment to include any changes made to the code.




5. **Activating the Local Poetry Shell**
   Poetry provides a local shell to work within the project environment. Run:
   ```shell
   poetry shell
   ```
   This command will activate the virtual environment for the project, making all dependencies available in the current terminal session.

6. **Adding Dependencies**
   To add a package to the project, use:
   ```shell
   poetry add <package-name>
   ```
   Poetry will resolve dependencies, add the package to your `pyproject.toml`, and update the lock file (`poetry.lock`) to ensure reproducibility.

7. **Adding Dev Dependencies**
   To add development-only dependencies (e.g., testing or linting tools), use:
   ```shell
   poetry add --group dev <package-name>
   ```
   This keep development dependencies separate, improving the project’s portability and stability.

With these steps, Poetry provides a structured, efficient way to build, manage, and maintain your Python projects, making collaboration and dependency management a breeze.

## Code Formatter: Ruff
[installation](https://pypi.org/project/ruff/) · [configuration](https://ruff.rs/docs/configuration/) · [usage](https://ruff.rs/docs/usage/)

**Ruff** is a fast, modern, and highly efficient Python linter and code formatter that combines several tools like `flake8`, `pylint`, and `black`. Ruff is designed to improve code quality by enforcing style and detecting errors, while also being incredibly fast, making it suitable for even large Python codebases.

With Ruff, you can automatically format your Python code according to [PEP 8](https://peps.python.org/pep-0008/) standards and apply other customizable linting rules to ensure consistency and quality in your project. It's especially useful when working in a team or maintaining a large codebase, as it helps enforce a uniform code style across all contributors.

To use **Ruff** as a code formatter with **Poetry**, you'll first need to install it in your project, and then configure it through your `pyproject.toml`. This setup ensures that Ruff can automatically format your code every time you make changes, allowing you to focus more on writing code than on formatting.

### Installation

To install **Ruff** in your Poetry-managed Python project, run the following command:

```bash
poetry add --dev ruff
```

This installs **Ruff** as a development dependency in your project, so it will be available in your virtual environment.

### Configuration

Once installed, you can configure **Ruff** by adding a section to your `pyproject.toml` file. Here’s an example configuration:

```toml
[tool.ruff]
line-length = 88  # Standard line length for PEP 8, compatible with Black
select = ["E", "F", "W"]  # Enable error, flake8 compatibility, and warning checks
ignore = ["E501"]  # Ignore line length rule (E501), since we use Black's style
```

This configuration sets up **Ruff** with sensible defaults, including a line length of 88 characters (the default for Black) and ignoring the line length check (E501) since it's already handled by Black.

### Usage

Once **Ruff** is installed and configured, you can use it to format your Python code. Run the following command to automatically format your files:

```bash
poetry run ruff --fix
```

This command will fix any formatting issues in your project files, including indentation, line length, and other style-related concerns.

### Integrating with VSCode

To make the most of Ruff within your development environment, you can integrate it with **VSCode** by modifying your `.vscode/settings.json` file:

```json
{
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.linting.ruffPath": ".venv/bin/ruff",  // Path to Ruff in Poetry environment
    "python.formatting.provider": "black",       // Use black for code formatting
    "python.formatting.blackPath": ".venv/bin/black",  // Ensure black is used from the venv
    "editor.formatOnSave": true                  // Automatically format on save
}
```

This setup ensures that **VSCode** will use **Ruff** for linting and **Black** for code formatting, all within the context of your Poetry-managed virtual environment.

### Running the Linter

You can also run **Ruff** as a linter to check your code for potential issues:

```bash
poetry run ruff check .
```

This will show any linting errors or warnings in your code.

### Why Use Ruff?

- **Speed**: Ruff is one of the fastest linters available, making it ideal for large codebases.
- **Comprehensive Linting**: It includes checks for both common errors and style issues, helping to keep your code clean and maintainable.
- **PEP 8 Compliance**: Ruff ensures that your code follows PEP 8 standards and can be customized to fit your own project’s coding style.
- **Easy Integration**: With simple installation and configuration, integrating Ruff into your workflow is straightforward.

By using **Ruff** with **Poetry**, you can maintain clean, consistent code while benefiting from the speed and efficiency of one of the fastest Python linters and formatters available.



## Tests: Pytest
[documentation](https://docs.pytest.org/en/stable/)
pytest is a powerful testing framework for Python that makes it easy to write simple and scalable test cases. It's known for its simplicity, ease of use, and ability to scale from small unit tests to complex functional tests. pytest can be used to write tests for individual units of code and also for larger, more complex features.

One of the key advantages of pytest is its ability to automatically discover and run test functions. It also supports fixtures to manage pre-test setup and cleanup, and provides detailed reports on test results, making it easier to diagnose issues quickly.

To use pytest in a Poetry-managed project, you'll first need to install it as a development dependency. Once installed, you can write and run tests directly from the command line or integrate pytest with other tools like VSCode for better developer experience.

### Installation
To install pytest in the dev environment we can use poetry:
```shell
poetry add --dev pytest
```

### Configuration
You can configure pytest by adding a block to the `pyproject.toml` file:

```toml
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "--maxfail=1 --disable-warnings -q"
testpaths = ["tests"]
```
In this example:

- `minversion` specifies the minimum version of pytest that your project supports.
- `addopts` defines additional command-line options for pytest. The options here tell pytest to stop after the first failure (--maxfail=1), disable warnings (--disable-warnings), and run quietly (-q).
- `testpaths` specifies the directory where your tests are located (in this case, `./tests`).

### Usage
Once pytest is installed and configured, you can start writing your tests. Create a file named test_*.py in the tests directory (e.g., test_example_module.py), and write test functions prefixed with test_. Here's an example of a simple test:

```python
# tests/test_example_module.py

def test_example():
    assert 1 + 1 == 2
```

To run the tests, execute the following command from command line:

```shell
poetry run pytest

```
pytest will automatically discover and run all tests in your project and display the results in the terminal.

These tests can also be run in groups or individually from the Testing panel in vscode.

### Writing Tests
It can be easy to get bogged down in writing extensive tests to ensure your code is doing what you expect. We suggest writing a basic set of tests initially and from there, as and when you encounter bugs or unexpected behaviour in your code, fix the bug, write a test that confirms it is fixed and move on. Over time a comprehensive set of test will develop that ensure your functions and methods are doing precisely what is expected, and prior mistakes are not being repeated.

Some templates for [simple](./test_simple.py) and more [advanced](./test_advanced.py) test files have been included.

## Data
Data should not be included in the git repository. If data is publicly available, then information on where to find it can be included in the README.md, or a script to download the data can be include in `scripts/`.

Recommendations for hosting data within the university are coming soon...

## Examples
We recommend including examples of your working code as [jupyter notebooks](https://jupyter.org/), importing your source code from `src/{project-name}` and showing step-by-step how it can be used.

A similar approach can be used for any data analysis: Notebooks which visualise results data, and produce the plots used in any publications can similarly be included here or in a similar directory.

## Scripts
Scripts should be placed in `scripts/` as `.py` files. They can be added to the `pyproject.toml` file as follows:

```toml
[tool.poetry.scripts]
example-script = "scripts.example_module:main_function"
```
This can then be run with poetry as:
```shell
poetry run example-script
```

### Examples
Things that we may want to execute as stand-alone scripts include:

- Downloading publicly  available data.
- Pre-processing data.
- Running experiments.
