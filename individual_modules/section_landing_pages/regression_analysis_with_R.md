# Introduction to Regression with R
## Overview
Welcome to **Introduction to Regression with R**. Our aim is to provide you with a comprehensive introduction to the statistical tool regression and how to perform these analyses in R.

## Course Objectives

By the end of this session you will be able to:

* describe what regression is
* fit a range of regression models with R including:
    * simple linear regression
    * multiple linear regression 
* describe the concept behind hypothesis testing in regression analysis
* describe and evaluate the assumptions behind hypothesis testing in regression analysis
* interpret the coefficients of a regression model
* make predictions from a regression model
* describe the link between regression and other common statistical tools

## Pre-requisite Knowledge

This course will not include an introduction to R, or how to setup and use R or Rstudio. It is assumed you are comfortable coding in R and are familiar with:

* how to write and execute commands in the R console
* what type of variables are available in R and how to work with these

We also assume that you are comfortable with fitting simple linear regression models in R and interpreting the output of these. If not we recommend that you consult our pre-requisite course **Introduction to Regression with R**.

This course it the first in a series of 3: 

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
  name = "Introduction to Regression with R",
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