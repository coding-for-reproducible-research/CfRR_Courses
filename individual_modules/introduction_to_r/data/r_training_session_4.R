# SESSION 4 - Manipulating and Plotting Data

#
'
Descripition: R Course Session 4
Date: November 2022
Author: Fiona Warren and Laura Roldan Gomez 
Adapted by: Laura Roldan-Gomez
'

# 1. Set-up your working directory----

# 2. Load the data----
 
# We'll use a data set called `bp_dataset`, provided as a csv file. It's based on a clinical trial to test the effect of two drugs (Drug A and Drug B), compared with a placebo, on blood pressure in people who have high blood pressure. The purpose of the drugs is to reduce blood pressure. Some additional information about the people in the trial, such as their age and sex, is also provided (see codebook for further information about the variables).
 
bp_dataset<-read.csv(file="bp_dataset_session4.csv", header=TRUE)

# 3. Explore the data set----

head(bp_dataset)
names(bp_dataset)

# We need to check the types of variable in the dataframe: 

# In this dataset we have both integer and character variables (see the code snippet below). The variable `male` is an integer coded as 0 and 1, but could also be a character variable i.e. recorded as "Male", "Female". The variable `intervention` is a character variable, but could be an integer coded, for example, as Control=0, Drug A=1, Drug B=2.

str(bp_dataset)


# 4. 

# 4.1 Basic statistics----

# There are 4 variables that include numeric data, that is, the information is an actual number rather than using numbers as codes. These are `age`, and blood pressure measured at three timepoints (`bp_baseline`, `bp_3m`, `bp_6m`).

# We want to find the mean, median, standard deviation and variance for these variables.

# Age mean
mean(bp_dataset$age)

# We can attach the dataframe `bp_dataset`, so we don't need to use the $ notation for each command. Remember to use the 'detach' command when you wish to detach the dataframe.

attach(bp_dataset)

mean(age)


# We can summarise for different subsets of the data by using *tapply*. This command takes 3 arguments:

#  `age`: numeric variable for which we wish to calculate the mean
#  `male`: variable indicating the subgroups, in this case 0 and 1
#  mean: the statistic we wish to calculate

tapply(age, male, mean)

# We can also calculate the mean for males [male==1]. Remember to use == to set the value of the variable `male` to be equal to 1.

mean(age[male==1])


# We can do the same for intervention group.

tapply(age, intervention, mean)

# Let's say we want to calculate the mean age by sex and intervention group. We can use the 'aggregate' command. The FUN argument means function, which is the mean in this example.

aggregate(age ~ male + intervention, data=bp_dataset, FUN=mean)

# We can also calculate the median, standard deviation, variance, minimum, maximum, range and sum.
# *Note* The commands 'sd' and 'var' calculate the sample sd and variance, not the population sd and variance.

sd(age)

median(age)

var(age)

min(age)

max(age)

range(age)

sum(age)

# We can also calculate percentiles. Using the 'quantile' command we can set the quantiles that we wish to find. Note that the 0.5 quantile is the median.

quantile(age, probs = c(.25, .5, .75))

# To get the inter-quartile range (75th percentile minus 25th percentile):

IQR(age)


# We can create a frequency table for categorical variables using the 'table' command.

table.male<-table(male)

# If we also wish to calculate proportions or percentages, we can use the 'prop.table' command. We first need to create the table and then pass to 'prop.table'.

prop.table(table.male)

# We can also create a table for a subgroup of the data. For example: table by sex for people aged over 50.

table.male.over50<-table(male[age>=50])

# We can also produce a table of proportions.
prop.table(table.male.over50)

# We can also produce cross-tabulations for two categorical variables.

table.male.intervention<-table(male, intervention)

prop.table(table.male.intervention)


## Tasks ---- 
# 1. Find the means for `bp_baseline` and `bp_3m`.



# 2. Calculate the mean, SD, median, 10th and 90th percentiles for `bp_baseline` for each intervention group. Also calculate the 25th centile, 50th centile (median) and 75th centile for `age`, by each combination of sex and intervention group. The aggregate command will be needed for this task: note that we need to include the dataset as a function, even though we have attached `bp_dataset`.


# 3. Create table of frequencies and a table of percentages by intervention group.



# 4. Create table of frequencies and a table of percentages by intervention group for people whose baseline blood pressure is greater than or equal to 180.


##------------------------------------##

# 4.2. Normal distribution----

# We can use R to get the cumulative density function (cdf) of a given normal distribution, based on the mean and sd. For example, to find the proportion of people with blood pressure less than 80, assuming mean BP=112 and SD is 15, we can use the 'pnorm' command.

pnorm(80, mean=112, sd=15)

# To find the proportion of people with BP above 125 we can use the code below.
# *Note* The argument lower.tail=FALSE tells the pnorm function to return the value to the right of the given value.

pnorm(125, mean=112, sd=15, lower.tail=FALSE)


# The same result can be obtained by using the command '1-pnorm'.

1-pnorm(125, mean=112, sd=15)


# The command 'qnorm' gives the inverse of the cdf (i.e. Z-score for the associated quantile). For example, for quantiles of the standard normal distribution (mean=0, sd=1) Z-score for 95th quantile:

qnorm(0.95, mean=0, sd=1)


# Z-score for 10th quantile:

qnorm(0.1, mean=0, sd=1)

## Tasks ----
# 5. Using the mean and sd for `age`, find the quantile for the 5th quantile and 97.5th quantile, assuming the distribution of `age` to be normal. Use values to 1 decimal place.
 
 
# 6. Find the probability that a member of the sample is aged under 35 and the probability that a member of the sample is aged over 60.


# 7. Find the probability that a member of the sample is aged between 50 and 55.



##------------------------------------##

# 4.3. Confidence intervals----

# You will need to install package 'Rmisc' for this section.

install.packages("Rmisc")
library(Rmisc)

# **2-sided confidence interval** .
# We will start by calculating a 2-sided 95% confidence interval for a mean, using the `age` variable. The command 'CI' is used. The 95% CI is the most common certainty level used: this is indicated by the 'ci' argument.

CI(age, ci=0.95)

# For a 2-sided 99% CI:

CI(age, ci=0.99)

# **One-sided CI** .
# For a one-sided CI, calculate the two-sided CI that corresponds to the required upper or lower bound. For example, for a lower 80% CI, calculate the 60% CI and take upper bound.

CI(age, ci=0.60)

# **CI for subgroups** .
# For example, to calculate the 90% CI for `age` by sex:

group.CI(age~male,data=bp_dataset, ci=0.90)


## Tasks----

# 9. Calculate the 2-sided 80% and 90% CI for `bp_baseline`.



# 10. Calculate the 1-sided lower 97.5th% CI for `bp_baseline`.



# 11. Calculate the 95% CI for baseline BP for each intervention group.



##------------------------------------##

# 4.4. Random sampling----
 
## Sampling from a data set----

# We may sometimes wish to randomly select a subset of participants from a dataset. We can use the 'sample' function in R. 
 
# To select 5 rows from our dataframe `bp_dataset`:

bp_dataset[sample(nrow(bp_dataset), 5), ]

# We may also wish to generate a random sample of numbers from a specific distribution.

# To simulate 5 numbers from a uniform distribution between 0 and 1:

runif(5,0,1)

# To simulate 10 numbers from a normal distribution with mean =0 and SD =5:

rnorm (10, mean = 0, sd = 5)

# To simulate Bernoulli/binomial trials:

# rbinom ( observations, trials per observation, probability of success for each trial)

# For a single observation of one Bernoulli trial, p(success)=0.2:

rbinom(1, 1, 0.2)


# For five observations of one Bernoulli trial, p(success)=0.7:

rbinom(5, 1, 0.7)

# For one observation of a binomial distribution, 10 trials, p(success=0.8):

rbinom(1, 10, 0.8) # The number of successes (out of a maximum of 10) is returned.

# For 5 observations of a binomial distribution, 20 trials, p(success=0.25):

rbinom(5, 20, 0.25)

# The number of successes (out of a maximum of 20) for each observation is returned.
 


##------------------------------------##

# 4.5. Normality testing----

# Prior to performing statistical tests that are based on the assumption of a normally distributed variable, we wish to test the assumption of normality. One way to do this is with a histogram.


# Basic syntax: hist (v, main, xlab, xlim, ylim, breaks,col,border)
# .`v` is the variable that is being plotted.

# As an example, we can create a histogram of `age`.

hist(age)

# By default, we are given frequencies of the plotted variable on the y-axis. If we want a density histogram we can use the *prob* option.

hist(age, prob=TRUE)


# We can add a title (main), x-axis label (xlab), set limitations to the axes (xlim, ylim), set the number of bins (breaks), and colours for the columns and borders.


hage<-hist(age, main="Age at baseline", 
     xlab="Age (years)",
     xlim=c(25,90), 
     ylim=c(0,20), 
     breaks=15,
     col="green",
     border="black")

# We can also get details about the histogram, e.g. bin boundaries, number of observations in each bin.

hage

# To get just the bin boundaries:

hage$breaks

# We can also add a normal curve. This is done in three stages. First, we need to create a list of values, called age2. This is a sequence of values from minimum age to maximum age, and with the same number of values as in the dataset. This is done using the *seq* function.

# The second step is to create another list of values, called fun (function) in the below example. This is done using the *dnorm* command, using the mean and SD of `age` and based on the `age2` sequence of values. This provides the probability density function for all values of `age2` based on a normal distribution with the mean and SD of `age`.

# The third step is to create the histogram, making sure we are using the densities and not the frequencies. The *lines* command plots the values of `age2` against the values of `fun` on the y-axis. The option *lwd* refers to line width.


# X-axis grid
age2 <- seq(min(age), max(age), length = 100)

# Normal curve
fun <- dnorm(age2, mean = mean(age), sd = sd(age))

# Histogram
hist(age, prob = TRUE, col = "white",
     ylim = c(0, 0.04),
     xlim=c(25,90), 
     main = "Histogram of age with normal curve")
lines(age2, fun, col = "blue", lwd = 2)

 
# An alternative graphical method for testing normality is to use the boxplot. For example, we can create a boxplot of age.

boxplot(age)


# We can also create separate plots for different subgroups, such as by sex. It is necessary to use the `male` variable coded as 0 and 1 for this command, and it needs to be stored as a factor variable. The variable `male` is stored as an integer, not a factor. Therefore, we need to create a new factor variable `male_factor`, which is coded as male=1, female=0.


male_factor<-factor(male)
class(male_factor)
levels(male_factor)
table(male, male_factor)


# We can create separate boxplots for age by sex
# (using `male_factor`) or `intervention`.

boxplot(age ~ male_factor)

boxplot(age ~ intervention,
        col = c("#FFE0B2", "#FFA726", "#F57C00"))

# We can also perform a Shapiro-Wilk test for normality.

shapiro.test(age) # p value < 0.05, so we reject the normality hypothesis 


# 4.6. Correlation----

# Check the relationship between variables with a scatterplot. For example, relationship between `age` and `bp_baseline`:

plot(age, bp_baseline)

# Pearson correlation: remember that variables should be distributed normally and with a linear relationship.

cor.test(age, bp_baseline) # by default - Pearson: –1 and 1, measures the strength and direction of the relationship between two variables.

# For a Spearman correlation, change the 'method':

cor.test(age, bp_baseline, method="spearman") # the closer to 1 the stronger the monotonic relationship. No requirement for normality.

## Tasks----
# 12. Calculate the Pearson and Spearman correlation between `bp_baseline` and `bp_3m`.



##------------------------------------##

# 4.7. T-test----
# Stats test to compare the means of two groups.

# Types:

## One-sample t-test----

# the simplest - a one-sample 2-sided t-test: test the null hypothesis that the true mean value of a continuous variable is equal to a pre-specified value. For example, we can use a t-test to test if true mean `age`=50.

t.test(age, mu=50) # p-value > 0.05, so we favour the null (fail to reject the null), which means that the true mean is equal to 50 with a 95%

# t-test to test if true mean `age`= 49:

t.test(age, mu=60) # p-value < 0.05 so we favour the alternative hypothesis, true mean is not equal to 50 with a 95%

# We can vary the width of the confidence interval provided as part of the t-test output - the default is 95% CI.

t.test(age, mu=50, conf.level=0.90)

# We can also specify the dataset and a subset of the data if needed. For example, in females only:

female_only<-subset(bp_dataset, male==0)
head(female_only)
detach(bp_dataset)


attach(female_only)
t.test(age, mu=50)
detach(female_only)
attach(bp_dataset)

# We can also specify a 1-sided t-test looking for whether the true mean of the variable is greater than or less than the specified value. To test whether true mean `age` is less than 45:

t.test(age, mu=45, alternative="less") # p > 0.05, favour null, true mean is greater than 45

# To test whether true mean `age` is greater than 45:

t.test(age, mu=45, alternative="greater") # p < 0.05, favour alternative, true mean is greater than 45


## Two-sample unpaired t-test----
 
# The two-sample unpaired t-test is used to compare the mean values of a continuous variable for two independent groups (the groups are not matched or paired in any way).

# In this example, we wish compare the mean value of age between males and females, or in other words we wish to know whether the true mean `age` is equal for males and females.

# `age` is the response variable (also called outcome variable or dependent variable); we are comparing mean `age` in Group 1 (male) with mean `age` in Group 0 (female), i.e. mean difference= Group 1 mean - Group 0 mean.
 
# *Note* This version of the t-test assumes unequal variance.

t.test(age~male) # p < 0.05, we favor the alternative - true difference in means is not equal to 0 (in english: the age mean of men and women is different)

# We can also use a factor variable to indicate the two groups (i.e. as opposed to an integer variable with groups coded as numbers).

t.test(age~male_factor)

# We can test for equal variance by using a statistical test called an F test. The null hypothesis for this test is that variances are equal. To compare the variance of `age` by `male`:

var.test(age ~ male)

# An alternative statistical test to test for equal variances is Bartlett's test (again, the null hypothesis assumes that variances are equal for each group):
 
bartlett.test(age ~ male)

# If we wish to repeat the t-test using the assumption of equal variance:

t.test(age~male, var.equal=FALSE)


## Paired t-test: comparing pairs of matched values----

# A paired t-test is used to compare two variables that are matched or paired in some way, for example: measurements made on the same person at two different times. The paired t-test uses the differences between matched pairs of measurements to test whether the true means are equal.

# For example, we may wish to perform a paired- t-test to test whether the true mean values for BP at baseline (`bp_baseline`) and BP at 3 months (`bp_3m`) are the same, taking into account that each person has their blood pressure measured at both baseline and 3 months, i.e. each measurement at baseline has a 'matched' measurement at 3 months taken in the same person.

t.test(bp_3m,bp_baseline,paired=TRUE) # p-value < 0.05, so, apparently, the drug makes a difference

# Note that the results are different if we do not take into account the paired nature of the variables.

t.test(bp_3m,bp_baseline,paired=FALSE)

## Tasks----
# 13. Perform a single sample 2-sided t-test to test whether the true mean of baseline BP is equal to 170.


# 14. Repeat for test of whether true mean of baseline BP is equal to 180.



# 15. Repeat for a 1-sided t-test of whether true mean of baseline BP is greater than 185.


# 16. Perform an unpaired t-test to compare mean BP at 3 months between Drug A and the control group. Hint: use the ! symbol to indicate a logical statement about intervention.



# 17. Do the same to compare mean BP at 3 months between Drug B vs control, and between Drug B vs Drug A.
 

# 18. Perform a paired t-test to test the null hypothesis that mean difference is 0 comparing BP at 6 months with BP at baseline.
 

 
# 19. Repeat to compare BP at 6 months with BP at 3 months for women (male=0) only.
 

# 4.8. ANOVA----

# We perform a one-way ANOVA (ANalysis Of VAriance test) to compare means across three or more groups. The null hypothesis is that the mean is equal across groups. For example, to compare mean BP at 3 months across Drug A, Drug B, Control:

oneway.drug <- aov(bp_3m ~ intervention)

summary(oneway.drug)

## Tasks----
# 20. Perform a one-way ANOVA to compare `age` across the three intervention groups. 
