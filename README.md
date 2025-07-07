# Coding for Reproducible Research (CfRR) Home Repository

Welcome to the **Coding for Reproducible Research (CfRR)** training programme repository at the University of Exeter. This repository contains all the course materials, modules, and resources used in the CfRR training workshops. The content is also presented on our Jupyter Book website for easy browsing and reading. The CfRR program offers a series of workshops covering specific coding languages (Python, R, Unix/Linux) and general best practices for coding and reproducible research. It provides a holistic approach to learning programming and good research computing practices, empowering researchers to conduct their work more efficiently, reproducibly, and with confidence. All workshops are open to any staff or student (from any college or campus).

If you have any questions or feedback, please contact us at
codingforreproducibleresearch@exeter.ac.uk.

## Repository Structure 
The repository is organised into several directories (each corresponding to part of the training materials or supporting materials) and files: 

- `cfrr_program_details/`:  General information about the CfRR program (e.g. About Us, code of conduct, how to use the website, etc.). 
- `contributing/`: Resources and guidelines for contributing to the CfRR program (these correspond to the "Join Us!" section of the website). This includes notebooks on how to contribute, community guidelines, roles, and how to develop a new course. 
- `course_homepages/`:  Jupyter notebooks for the homepage/overview of each broad course category (e.g. Python, R, Unix, etc.). 
- `data/`: Data files (CSV datasets) used by the notebooks to generate content on the website. For example: 
- `workshop_info.csv`: data used to generate the upcoming Workshop Schedule and Signup page (via the notebook cfrr_program_details/courses_overview.ipynb ).
- `previous_workshops.csv`: data used to generate the list of past workshops (also via the above notebook).
- `workshop_details.csv`: data used to generate the "How do these courses relate?" network graph on the pathways page (via `pathways/related_courses.ipynb`). 
- `individual_modules/`: The main content for each workshop module. Each subdirectory here (e.g. `introduction_to_python/`, `introduction_to_r/`, `software_development_best_practices/`, etc.) contains the Jupyter notebooks, markdown files, and images for a specific course. 
- `section_landing_pages/`: (Within `individual_modules`) Contains overview markdown pages for each course module, including course descriptions, objectives, and prerequisites. These serve as the "landing page" for each course in the self-study notes section of the website. 
- `pathways/`: Notebooks and content describing how the courses interrelate (for example, visualising pathways through the courses). 
- `programme_information/`: Detailed information pages for each course offering. These notebooks form the content of the Workshop Information section of the website (providing outlines and details for each workshop). 
- `short_courses/`: Materials for any short courses or special topics (for example, a short module on virtual environments). 
- `where_is_my_understanding/`: Interactive quizzes to help learners gauge their understanding of various courses. (This corresponds to the self-assessment quizzes section of the website.)

In addition to the directories, the root of the repository contains important configuration and documentation files, including: 

- `home_page.md`: The main homepage content for the Jupyter Book (the landing page of the CfRR website). 
- `_config.yml`: Configuration for the Jupyter Book (controls the website's appearance and behaviour). 
- `_toc.yml`: Table of contents for the Jupyter Book (defines the structure and navigation of the site). 
- `CITATION.cff`: Citation information for the CfRR materials (how to cite this training program and content). 
- `references.bib`: Bibliographic references used across the materials (for citations within course content). 
- `pyproject.toml`: Project configuration and dependencies (for Python environment, uses Poetry format) for building the Jupyter Book. 
- `requirements.in`: List of Python packages required to run the notebooks and build the book (e.g., Jupyter Book, numpy, pandas, etc.). 
- `.github/workflows/`: CI workflows for automated building and deployment (see Continuous Integration section below).

## Getting Started: Using the Materials 
You can engage with the CfRR course materials in two main ways: 

### Browse Online

The easiest way to view the content is on our Jupyter Book website (hosted via GitHub Pages). There you will find all the workshops organised into sections with interactive elements. Visit the CfRR Courses Website, [here](https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html).

### Run Locally
You can run the materials on your own machine to interact with the notebooks directly. To set up the repository locally and explore the content: 

Clone this repository to your local machine: 

```bash
git clone https://github.com/coding-for-reproducible-research/ CfRR_Courses.git 
```

Install the required dependencies, which can be done with pip:

```bash
pip install -r requirements.in
```

Alternatively, you can use the provided `pyproject.toml` file with Poetry, or manually install the packages listed in `requirements.in`. 

### Launch Jupyter
to interact with the notebooks: 
```bash
jupyter lab
```

 or

```bash
 jupyter notebook
```

Then navigate to the course content of interest (e.g. open the notebooks in `individual_modules/<course_name>/ for a given workshop). 

(Optional) Build the Jupyter Book site locally: 

To build the complete website from this repository, run: 
```bash
jupyter-book build
```

This will generate the static site under the `_build/html/` directory, which you can open in a browser to view the book offline. (This step requires the `jupyter-book` package, which is included in the requirements.) 

### Launch on Binder (Interactive Online Environment)

If you prefer not to set up anything locally, you can try out the notebooks in an interactive environment using Binder. Click the Binder link below to open the repository in an online Jupyter environment (no installation needed, runs in your browser): [Launch Binder](https://mybinder.org/v2/gh/coding-for-reproducible-research/CfRR_Courses/main)

## Contributing 

Contributions to improve and expand the CfRR training materials are welcome! If you have improvements, corrections, or new content to add, please see our contribution guidelines. We have detailed instructions on how to contribute in the repository's `contributing/` directory (see the notebooks there for information on our contribution process, community guidelines, and how to develop new courses). This information is also summarised on the Contributing section of our website for easy reading, [here](https://coding-for-reproducible-research.github.io/CfRR_Courses/contributing/contributing.html). Before contributing, you may want to familiarise yourself with the repository structure (above) and ensure you have the required environment set up (see Getting Started section). Feel free to open an issue or discussion if you have ideas or questions about contributing.

## License 
Since this repository aggregates several courses and materials (potentially from different origins), there is no single license that applies to the entire repository. Instead, each course or module has its license specified. Please refer to the `LICENSE.txt` file located in each course's directory, under `individual_modules/`, to view the applicable license for that content. Generally, the materials are open for reuse under permissive licenses, but make sure to check the specific license file in the module you are interested in. If you have any questions or concerns about the reuse of the content, please get in touch with the CfRR team (see Contact information below).

## Continuous Integration and Deployment 
This project uses GitHub Actions for continuous integration and deployment. Whenever changes are pushed or a pull request is made, the Jupyter Book is automatically built and checked using the workflow in `.github/workflows/build-book.yml`. On pushes to the main branch (and on a schedule), the site is automatically deployed to GitHub Pages via `.github/workflows/deploybook.yml`. This means the online site is kept up-to-date with the latest materials from the repository. Contributors do not need to build or deploy the website manually; the CI system handles it, ensuring that changes in the content will appear on the live site after being merged into the main branch.

Happy coding, and we hope you find the Coding for Reproducible Research materials useful for your research journey! Feel free to explore, learn, and contribute. 
