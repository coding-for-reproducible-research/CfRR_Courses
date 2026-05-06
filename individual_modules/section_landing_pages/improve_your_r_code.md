# Improve Your R Code

## Overview

Welcome to Improve Your R Code! R is primarily known as a language and environment for statistical computing and graphics. However, the flexibility and accessibility of R has led to its popularity across a diverse range of disciplines including biosciences, medicine and, of course, statistics. This workshop aims to extend your existing knowledge of R, enabling you to improve the **style** and the **speed** of your R code.


### Course Objectives

By the end of the session you will:

-   Be able to write clean, readable, and maintainable R code following the tidyverse style guide.
-   Be able to accurately measure the speed of your code using `microbenchmark`.
-   Be comfortable with built-in R functions and packages (e.g. `parallel`, `data.table`, `Rcpp`) for improving execution speed.
    

## Pre-requisite Knowledge

This workshop is designed for learners who:

- Have prior experience working with R and R scripts.
- Are familiar with basic R syntax and using functions.
- Have used R interactively in environments like RStudio or Jupyter.

If you are not comfortable with some of these topics then you may wish to attend some of our other R programming language courses, particularly [Introduction to R](introduction_to_r.md)

There are three packages need for this workshop. The first two (devtools & learnr) are available from CRAN. The third is a package we have developed with the course materials in and is available from GitHub (cfrrRTutorials). 

This code will install these three packages, and then open the `learnr` window with the interactive course content.

```
install.packages("devtools")
install.packages("learnr")

library(devtools)
library(learnr)

devtools::install_github("ejh243/cfrr-r-tutorials")

library(cfrrRtutorials)

learnr::run_tutorial(
  name = "Improve Your R Code",
  package = "cfrrRtutorials"
)
```

## Course Development 

If you are developing content for this course, the learnr materials are maintained in the repository [cfrrRtutorials](https://github.com/coding-for-reproducible-research/cfrrRtutorials)

Please refer to the guidance provided in that repository for the required development workflows and processes to follow.

## Accessibility statement – learnr-based R courses

Some CfRR courses, including this one, are delivered using the `learnr` framework and are intended to be run within the RStudio software environment.

The use of the `learnr` package supports efficient delivery within a shorter workshop format. By handling data loading and interactive setup automatically, `learnr` reduces technical overhead and allows the workshop to focus more fully on the theoretical concepts being taught, rather than on environment configuration or data management.

However, because these courses are executed within RStudio, overall accessibility is influenced by the capabilities and configuration of the learner’s local software environment. While RStudio provides a range of accessibility features, it may not be fully accessible for all users.

If you encounter barriers when using a learner-based course or require reasonable adjustments or alternative formats, please contact the CfRR team. We are happy to discuss individual needs and explore appropriate support options.

For more information about accessibility across the CfRR programme, and particular guidance on improving the accessibility of RStudio, please see the full accessibility statement: [Accessibility at Coding for Reproducible Research](../../cfrr_program_details/accessibility.ipynb)