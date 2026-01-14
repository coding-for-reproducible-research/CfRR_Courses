# Introduction to Regression with R
```{important}
Please note that we recommend engaging with this course via the `learnr` interface described below, rather than using the pages that follow. The pages below are retained for reference purposes and to provide an overview of the course content and may not represent the up to date course content. 
```
## Overview
Regression analysis is a fundamental statistical technique used to model the relationship between multiple variables. It is a very flexible tool that can handle a range of different data types (continuous, binary or categorical) and address both complex and simple research questions. Here we look at how to fit a range of regression models with R, how to interpret the output and the link between regression and other common statistical tools.

## Course Objectives
- Understand the types of questions regression can be used to answer.
- Be able to fit a linear regression model with multiple predictor variables.
- Be able to fit a logistic regression model with multiple predictor variables.
- Be able to extract and summarise the results from a range of regression models.
- Be able to design a regression model appropriate for addressing a specific research question.

## Pre-requisite Knowledge

Learners are expected to already be familiar with the basics of R, such as how to load a dataset from a local file and manipulate variables.

## Install necessary R packages

There are three packages need for this workshop. The first two (devtools & learnr) are available from CRAN. The third is a package we have developed with the course materials in and is available from GitHub (cfrrRTutorials). 

This code will install these three packages.

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