# Regression Analysis in R: Adapting to Varied Data Types

## Overview


Welcome to **Regression Analysis in R: Adapting to Varied Data Types**. Our aim is to build on your understanding of simple linear regression and expand this framework to enable you to analyse a broad range of data and answer more complex questions.


## Course Objectives 
By the end of this session you will be able to:

* understand what a generlised linear model is
* fit a logistic regression models with R 
* select the appropriate regression model for either a continuous or binary outcome
* include a range of different types of predictor variables in your regression models
* interpret the coefficients of a regression model

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
  name = "Regression Analysis in R: Adapting to Varied Data Types",
  package = "cfrrRtutorials"
)


```