# Mixed Effects Regression with R

## Overview 

Welcome to **Mixed Effects Regression with R**. Our aim is to build on your existing knowledge of regression to fit more complex models that can handle more complicated data sets. In this session you will learn about different types of regression analysis, when to use them and how to interpret the results.

## Course Objectives 
By the end of the session you will be able to :

-   Use regression answer to answer a wide range of research questions .
-   Be able to fit a regression model with interactions between predictor variables.
-   Be able to fit multi-level regression models
-   Be able to extract and summarise the results from a range of regression models.
-   Be able to design a regression model appropriate for addressing their specific research question.

While it is delivered as a stand alone session, it is designed as a part of a series of Regression with R workshops where the content develops the ideas further to give you a comprehensive understanding how regression can be used to address a broad range of questions. 

The complete series includes:

1. [Introduction to Regression with R](regression_analysis_with_R.md)
2. [Regression Analysis in R: Adapting to Varied Data Types](regression_analysis_in_R_adapting_to_varied_data_types.md)
3. [Mixed Effects Regression with R](mixed_effects_regression_with_R.md)

## Install necessary R packages

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
  name = "Mixed Effects Regression with R",
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