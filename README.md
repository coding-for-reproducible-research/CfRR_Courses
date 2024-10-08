# Coding For Reproducible Research (CfRR) - Training Program Repository

Welcome to the repository for the Coding For Reproducible Research (CfRR) training program at the [University of Exeter](https://www.exeter.ac.uk/). This repository contains all the materials and modules used in the CfRR training program, presented on our [Jupyter Book website](https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html).

This training programme provides workshops to support researchers at the University of Exeter to expand their skillsets and position them to perform their informatics research projects efficiently and reproducibly confidently. The program covers training on specific coding languages, such as Python, R, and Unix/Linux, as well as training relating to good coding practice and reproducible working methods designed to be agnostic of programming language. In this way, we offer a holistic perspective on how programming tasks should be approached, ultimately providing researchers with the tools and knowledge to feel confident in their actions. All workshops are open to any staff or student from any college or department and are accessible from any campus.

These workshops are brought to you by the [University of Exeter Research Software and Analytics Group](https://www.exeter.ac.uk/research/research-software-and-analytics/), [University of Exeter Researcher Development](https://www.exeter.ac.uk/research/doctoralcollege/researcherdevelopment/) and the [University of Exeter Doctoral College](https://www.exeter.ac.uk/research/doctoralcollege/).

You can contact the CfRR team at the following email: [codingforreproducibleresearch@exeter.ac.uk](mailto:codingforreproducibleresearch@exeter.ac.uk)

## Repository Structure

The repository is organized into several directories:
- **cfrr_program_details**: Several jupyter notebook files relate to general content concerning the CfRR training programme, including the code of conduct, feedback ages, how to use the website, etc.
- **contributing**: Several jupyter notebook files that describe the process that is used to contribute to the the CfRR program and website. Broadly relate to the "Join Us!" section on the website. 
- **course_homepages**: Homepage content for the individual courses.
- **data**: Contains several .csv files that are used with code throughout the website to generate HTML and markdown content to populate different parts of the website.
    - **workshop_info.csv**: Used to generate the content on the "Workshop Schedule and Signup Page", generated via the Jupyter Notebook at "cfrr_program_details/courses_overview.ipynb". Within this notebook, markdown content on the upcoming workshops is generated alongside the MS Forms to sign up based on the data within workshop_info.csv.
    - **previous_workshops.csv**: Used to generate the content on the "Workshop Schedule and Signup Page", generated via the Jupyter Notebook at "cfrr_program_details/courses_overview.ipynb". Within this notebook, HTML content on historical workshops is created that act as a record of individuals contributions to the CfRR program.
    - **workshop_details.csv**: Used to generate the pathway content on the "How do these courses relate?" section of the website. The Jupyter notebook that creates the networks used within this section is "pathways/related_courses.ipynb".
- **individual_modules**: The main content for each course module. These are all of the markdown and Jupyter notebook files used for the self study content on the website.
    - **section_landing_pages**: A number of different markdown files that provide an overview of the different modules within the program. Including an overview of the course, objectives and pre-reqs, that act as heading splash page for each of the courses within the self-study notes section of the website.
- **pathways**: Information on how the courses interrelate.
- **programme_information**: Detailed information on each of the courses that are offered. These files make up the content of the "Workshop Information" section of the website. 
- **where_is_my_understanding**: Quizzes to help gauge understanding of course content.

There are also several files within the root directory; these include: 
- **home_page.md**: This file is the main root page for the CfRR Jupyter Book website.
- **_config.yml**: This file customizes the appearance and behaviour of the overall Jupyter Book. 
- **_toc.yml**: This file organizes the structure and overall navigation of the content of the Jupyter Book that is built.
- **CITATION.cff**: Provides citation information for the CfRR website, and the course content aggregated throughout the website. 
- **references.bib**: Used to store bibliographic references throughout all of the content on the website. 
- **requirements.txt**: A file that specifies the dependencies of the Python kernel used in the website.  

## Contributing

We welcome contributions to improve and expand the CfRR training materials. Please visit the [contributing guidance](https://coding-for-reproducible-research.github.io/CfRR_Courses/contributing/contributing.html) on the CfRR website that explains the steps to take to contribute to this repo.

## License

As this repository aggregates several courses, several different licenses apply depending on the content. The license is included in the course content's directory, and so will be in the subdirectory within "individual_modules". If you have any queries or concerns please reach out to us.

---

Feel free to explore, learn, and contribute! If you have any questions, please open an issue or contact us through the repository.

---

**Contact Information**:
- [CfRR Home Page](https://coding-for-reproducible-research.github.io/CfRR_Courses/home_page.html)
- [University of Exeter](https://www.exeter.ac.uk/)

---

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/coding-for-reproducible-research/CfRR_Courses/main)

