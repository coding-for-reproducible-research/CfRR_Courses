# Statistical Analysis





R is synomous with data analysis. Here we will learn how to perform a number of common statistical tests with R. Please note that the focus here is on how
to perform a given test in R, it is not to discuss the merits of or scenarios in which you would use a specific test.

## Loading the dataset

To do statistics we need some observed data. We will use a dataset contained in the csv file [bp_dataset.csv](../data/bp_dataset_session4.csv). This dataset is based on a clinical trial to test the effect of two 
drugs (Drug A and Drug B), compared with an inactive control drug (placebo), on blood pressure in people who have high blood pressure. The purpose of the 
drugs is to reduce blood pressure. Some additional information about the people in the trial, such as their age and sex, is also provided (see 
[codebook](../data/bp_dataset_codebook_session4.xlsx) for further information about the variables).

Let's start by loading the dataset. You need to ensure that the dataset is located in your current working directory. 
We will read in the csv file and assign it to a variable called ```bp_dataset```. The ```header=TRUE``` argument means R will take the entries in the first row 
 and use these to set the column headings. 


{% highlight r %}
bp_dataset<-read.csv(file="bp_dataset_session4.csv", header=TRUE)
{% endhighlight %}

Take a look at the first six rows to get a sense of the dataset.


{% highlight r %}
head(bp_dataset)
{% endhighlight %}



{% highlight text %}
##   ptid male age intervention bp_baseline bp_3m bp_6m
## 1    1    1  41       Drug B         218   153   163
## 2    2    0  46       Drug B         200   162   177
## 3    3    0  37       Drug A         198   122   166
## 4    4    0  46       Drug A         202   148   128
## 5    5    1  44      Control         142   196   231
## 6    6    1  36       Drug B         148   191   164
{% endhighlight %}

Let's find out how many rows (observations) and variables (columns) are in this dataset using the ```dim``` command (for dimensions).


{% highlight r %}
dim(bp_dataset)
{% endhighlight %}



{% highlight text %}
## [1] 100   7
{% endhighlight %}


<details>
	<summary> Data Organisation </summary>
	<pre>
		
When it comes to programming how you organise/store your data becomes important to facilitate efficient processing. This is beyond the
remit of this course - but you can find out more about the principles of [tidy data here](https://r4ds.had.co.nz/tidy-data.html).

    </pre>
</details>

We also want to check the types of variable in the dataframe. The ```str()``` command allows us to check the structure of the dataframe and tells us 
about the types of variables in our dataset.


{% highlight r %}
str(bp_dataset)
{% endhighlight %}



{% highlight text %}
## 'data.frame':	100 obs. of  7 variables:
##  $ ptid        : int  1 2 3 4 5 6 7 8 9 10 ...
##  $ male        : int  1 0 0 0 1 1 0 0 1 1 ...
##  $ age         : int  41 46 37 46 44 36 65 69 58 65 ...
##  $ intervention: chr  "Drug B" "Drug B" "Drug A" "Drug A" ...
##  $ bp_baseline : int  218 200 198 202 142 148 166 201 206 140 ...
##  $ bp_3m       : int  153 162 122 148 196 191 140 141 173 125 ...
##  $ bp_6m       : int  163 177 166 128 231 164 152 113 164 115 ...
{% endhighlight %}

In this dataset we have both integer and character variables. Gender is provided as a binary variable 
(also known as an indicator or dummay variable called ```male``` coded as 0 
(for female) and 1 (for male). This is not nessecary, if it was coded as a factor with the levels 
"Female" and "Male" R would be happy to use in the 
statistical functions. Coding it in this way however, is more aligned with how it is used in statistics, 
and may make interpetation easier. 

The variable `intervention` is a character variable, although arguably should be coded as a factor. However,
in most cases R will convert it to a factor within the function calls if it is needed.


## Summary statistics

In this dataset, there are 4 numeric variables. These are ```age```, and blood pressure measured at three timepoints (```bp_baseline```, 
```bp_3m```, ```bp_6m```).

We want to find the mean, median, standard deviation and variance for these variables. Let's start with the mean. To find the mean for ```age``` we can use:


{% highlight r %}
mean(bp_dataset$age)
{% endhighlight %}



{% highlight text %}
## [1] 49.03
{% endhighlight %}

We can attach the dataframe ```bp_dataset```, so we don't need to use the ```$``` notation for each command. Remember to use the ```detach()``` 
command when you wish to detach the dataframe.


{% highlight r %}
attach(bp_dataset)
mean(age)
{% endhighlight %}



{% highlight text %}
## [1] 49.03
{% endhighlight %}

We can also calculate the median, standard deviation, variance, minimum, maximum, range and sum fairly easily using base R functions. 



{% highlight r %}
sd(age)
{% endhighlight %}



{% highlight text %}
## [1] 12.31116
{% endhighlight %}



{% highlight r %}
median(age)
{% endhighlight %}



{% highlight text %}
## [1] 47
{% endhighlight %}



{% highlight r %}
var(age)
{% endhighlight %}



{% highlight text %}
## [1] 151.5647
{% endhighlight %}



{% highlight r %}
min(age)
{% endhighlight %}



{% highlight text %}
## [1] 26
{% endhighlight %}



{% highlight r %}
max(age)
{% endhighlight %}



{% highlight text %}
## [1] 81
{% endhighlight %}



{% highlight r %}
range(age)
{% endhighlight %}



{% highlight text %}
## [1] 26 81
{% endhighlight %}



{% highlight r %}
sum(age)
{% endhighlight %}



{% highlight text %}
## [1] 4903
{% endhighlight %}

*Note* The commands 'sd' and 'var' calculate the sample sd and variance, not the population sd and variance.

We can also calculate percentiles. Using the ```quantile()``` command we need to specify which quantiles ( as proportions) that we want to calculate,
where the 0.5 quantile would represent the median.


{% highlight r %}
quantile(age, probs = c(.25, .5, .75))
{% endhighlight %}



{% highlight text %}
##   25%   50%   75% 
## 40.00 47.00 56.25
{% endhighlight %}

To get the inter-quartile range (75th percentile minus 25th percentile) we can do this with the ```IQR()``` function.


{% highlight r %}
IQR(age)
{% endhighlight %}



{% highlight text %}
## [1] 16.25
{% endhighlight %}

We can also calculate multiple descriptive summary statistics of a numeric variable simultaneously using the function ```summary()```.


{% highlight r %}
summary(age)
{% endhighlight %}



{% highlight text %}
##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
##   26.00   40.00   47.00   49.03   56.25   81.00
{% endhighlight %}

## Activity

Find the means, medians and range for the variable ```bp_baseline``` and ```bp_3m```.

# Summary statistics by groups

We can calculate statistics for different subsets or groups of the data by using R command ```tapply()```. The ```tapply()``` 
command requires 3  arguments :

 + a numeric variable which we want to summarise (in the example below this is ```age```) 
 + a categorical variable indicating the subgroups,which we want to group by (in the example below this is ```male```)
 + the function we wish to call on each subgroup (in the example below this is ```mean```)


{% highlight r %}
tapply(age, male, mean)
{% endhighlight %}



{% highlight text %}
##        0        1 
## 51.94595 47.31746
{% endhighlight %}

If we want to calculate a summary statistics for a sub group, by subsetting it and providing the subset to the ```mean()``` function. For example 
to calucate the mean of just the means (i.e where male==1). 
Note the use of ```==``` for specifiying an equality condition.



{% highlight r %}
mean(age[male==1])
{% endhighlight %}



{% highlight text %}
## [1] 47.31746
{% endhighlight %}


We can use the ```tapply()``` function to calculate the medians for the intervention groups.


{% highlight r %}
tapply(age, intervention, median)
{% endhighlight %}



{% highlight text %}
## Control  Drug A  Drug B 
##    49.5    49.5    42.5
{% endhighlight %}

If we want to calculate summary statistics for combinations of groups for example by sex and intervention group, we can use the ```aggregate()```
 command. We use the formula method to specify which variables we want summarise (on the left hand side of the ~) and which we want to group by
 (on the right hand side of the ~).  If all the variables are included in
 single data.frame, we can construct the formula using just the column names, and include the argument ```data``` to specify which object these are found
 in. The ```FUN``` argument specfies which function you want to apply to these data, which is the mean in this example. 
 Note that we need to include the dataset as an argument, even though we have attached ```bp_dataset```.



{% highlight r %}
aggregate(age ~ male + intervention, data=bp_dataset, FUN=mean)
{% endhighlight %}



{% highlight text %}
##   male intervention      age
## 1    0      Control 53.84615
## 2    1      Control 49.33333
## 3    0       Drug A 56.63636
## 4    1       Drug A 47.73913
## 5    0       Drug B 46.07692
## 6    1       Drug B 45.72000
{% endhighlight %}

## Activity

1. Calculate the mean, SD, median, 10th and 90th percentiles for `bp_baseline` for each intervention group. 
2. Calculate the 25th centile, 50th centile (median) and 75th centile for `age`, for each combination of sex and intervention group. 


# Summary statistics for categorical data

We can create a frequency table for categorical variables using the ```table()``` command.


{% highlight r %}
table(male)
{% endhighlight %}



{% highlight text %}
## male
##  0  1 
## 37 63
{% endhighlight %}

We can also produce cross-tabulations for two categorical variables. The first variable will form the rows, and The
second variable the columns. 


{% highlight r %}
table(male, intervention)
{% endhighlight %}



{% highlight text %}
##     intervention
## male Control Drug A Drug B
##    0      13     11     13
##    1      15     23     25
{% endhighlight %}


In fact we can produce tables for more than 2 categorical variables. R will print these as a series of 2 dimensional
tables for fixed values of the other variables.

If we also wish to calculate proportions or percentages, we can use the ```prop.table()``` command. We first need to create the 
table and then pass to ```prop.table()```. You can either do this in two stages:


{% highlight r %}
table.male<-table(male)
prop.table(table.male)
{% endhighlight %}



{% highlight text %}
## male
##    0    1 
## 0.37 0.63
{% endhighlight %}

Or as a nested function call:


{% highlight r %}
prop.table(table(male, intervention))
{% endhighlight %}



{% highlight text %}
##     intervention
## male Control Drug A Drug B
##    0    0.13   0.11   0.13
##    1    0.15   0.23   0.25
{% endhighlight %}

We can also create a table for a subgroup of the data by providing just a subset of the data to the ```table()``` function.
 For example to count the number of each sex, only for people aged over 50:


{% highlight r %}
table(male[age>50])
{% endhighlight %}



{% highlight text %}
## 
##  0  1 
## 17 19
{% endhighlight %}


## Activity 
1. Create table of frequencies of the number of indivduals in each intervention group. Convert this into 
and a table of percentages.

2. Create table of frequencies of each intervention group stratified by whether individual's baseline blood pressure is 
greater than or equal to 180.

# Common statistical tests: One-sample t-test

There are several types of t-test. We will start with the simplest: a one-sample two-sided t-test to test the null hypothesis that the true mean 
value of a continuous variable is equal to a pre-specified value. The default behaviour, and the most common application is to compare to a value of 0.


{% highlight r %}
t.test(age)
{% endhighlight %}



{% highlight text %}
## 
## 	One Sample t-test
## 
## data:  age
## t = 39.826, df = 99, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 95 percent confidence interval:
##  46.5872 51.4728
## sample estimates:
## mean of x 
##     49.03
{% endhighlight %}


We can see in the console, we get a more verbose output than we have seen before. Mainly because the result of statistical test often includes multiple
statistics, and the orginial writers of the ```t.test()``` function have made an effort to present these back to the user in an easy to intepret way. 

We can see there is a statement at the top of the output reminding or confirming which statistical test we have performed, and underneath this a confirmation
of which variable/data this was performed on. 

We then have a line of multiple test statistics, including the p-value. Here we can see our test result is highly significant with p < 2.2e-16. Given 
we are analysing a population of adults, they are all a lot older than 0 so it is not surprising. The function writers have take the executive decision
to report the p-value as < 2.2e-16 rather than give the specific value. In some fields/journals/research group, this approximation is not good enough. 
Later we will show you how to extract a more precise p-value. 

Underneath this we have a confirmation of the alternative hypothesis the statistic was considered against, we then have the confidence interval and the 
estimated mean of the sample.

We can vary the width of the confidence interval provided as part of the t-test output, by including the argument ```conf.int```. The default is the 95% CI.
For the 90% confidence interval, we can run


{% highlight r %}
t.test(age, conf.level=0.90)
{% endhighlight %}



{% highlight text %}
## 
## 	One Sample t-test
## 
## data:  age
## t = 39.826, df = 99, p-value < 2.2e-16
## alternative hypothesis: true mean is not equal to 0
## 90 percent confidence interval:
##  46.98587 51.07413
## sample estimates:
## mean of x 
##     49.03
{% endhighlight %}

Here we can see that the majority of the output is unchanged, it is just the confidence interval which is different. 

The default behaviour is to perform a two-sided t-test. We can specify a one-sided t-test testing whether the true mean of the variable is greater than 
or less than the specified value  by including the argument ```alternative``` and setting it to either ```greater``` or ```less```. To test 
whether the true mean `age` is greater than 0 we use:


{% highlight r %}
t.test(age, alternative="greater")
{% endhighlight %}



{% highlight text %}
## 
## 	One Sample t-test
## 
## data:  age
## t = 39.826, df = 99, p-value < 2.2e-16
## alternative hypothesis: true mean is greater than 0
## 95 percent confidence interval:
##  46.98587      Inf
## sample estimates:
## mean of x 
##     49.03
{% endhighlight %}

Although this is a very uncommon application (due to the need to justify the choice of value), you can perform a one sample t-test against a value 
other than 0 by including the argument ```mu```. For example, we can use a t-test to test if true mean ```age```=50.


{% highlight r %}
t.test(age, mu=50)
{% endhighlight %}



{% highlight text %}
## 
## 	One Sample t-test
## 
## data:  age
## t = -0.7879, df = 99, p-value = 0.4326
## alternative hypothesis: true mean is not equal to 50
## 95 percent confidence interval:
##  46.5872 51.4728
## sample estimates:
## mean of x 
##     49.03
{% endhighlight %}

If you are only performing one (or a few) statistical tests, and you are working interatively then you might be ok to manually copy the result from the 
console. However, there are likely times when you want to extract the result from the test for further processing, for example enter it into a table to 
save to your computer. We can save the output of a t.test (or indeed any other statistical test or function) to a variable, meaning we can manipulate it 
further.



{% highlight r %}
t.out<-t.test(age, mu=50)
t.out
{% endhighlight %}



{% highlight text %}
## 
## 	One Sample t-test
## 
## data:  age
## t = -0.7879, df = 99, p-value = 0.4326
## alternative hypothesis: true mean is not equal to 50
## 95 percent confidence interval:
##  46.5872 51.4728
## sample estimates:
## mean of x 
##     49.03
{% endhighlight %}

As before, when we defined or created a variable, there is no output to the console. We can see the output by entering the name of the object. Let's 
explore the object that we have created. If we use ```class()``` we can learn what type of object it is.


{% highlight r %}
class(t.out)
{% endhighlight %}



{% highlight text %}
## [1] "htest"
{% endhighlight %}

```htest``` - that's a new one. This is a type of object that has been specfying defined to hold the result of a t-test. It consists of different objects
or slots where didferent parts of the result are stored. We can get a list of this elements with the function ```names()```


{% highlight r %}
names(t.out)
{% endhighlight %}



{% highlight text %}
##  [1] "statistic"   "parameter"   "p.value"     "conf.int"    "estimate"   
##  [6] "null.value"  "stderr"      "alternative" "method"      "data.name"
{% endhighlight %}

We can see 10 items listed. All of these are named elements stored within our ```htest``` object which we can extract by name using the ```$```. For example 
we can get just the p-value as follows:


{% highlight r %}
t.out$p.value
{% endhighlight %}



{% highlight text %}
## [1] 0.432636
{% endhighlight %}

We can get the estimated mean:


{% highlight r %}
t.out$estimate
{% endhighlight %}



{% highlight text %}
## mean of x 
##     49.03
{% endhighlight %}

We can get the confidence interval:


{% highlight r %}
t.out$conf.int
{% endhighlight %}



{% highlight text %}
## [1] 46.5872 51.4728
## attr(,"conf.level")
## [1] 0.95
{% endhighlight %}

While the p-value and estimated mean were single values, the confidence interval has returned a vector of length 2. The ```htest```
object contains a range of different elements. 



# Common statistical tests: Two-sample unpaired t-test

The two-sample unpaired t-test, also known as an independent sample t-test, is used to compare the mean values of a continuous variable for two independent 
groups where the data points across the two groups are not matched or paired in any way. 

In this example, we want to compare the mean age between males and females, or in other words we want to test whether the true mean age is equal 
for males and females.

As we have all the data for our response variable (also called outcome variable or dependent variable), age in one object and we have a second object 
which indicates which entries are female and which are male, we will use the formula method (signalled by the ```~```)
for specifying the comparision we want to make. 


{% highlight r %}
t.test(age~male)
{% endhighlight %}



{% highlight text %}
## 
## 	Welch Two Sample t-test
## 
## data:  age by male
## t = 1.739, df = 63.594, p-value = 0.08687
## alternative hypothesis: true difference in means between group 0 and group 1 is not equal to 0
## 95 percent confidence interval:
##  -0.6891826  9.9461538
## sample estimates:
## mean in group 0 mean in group 1 
##        51.94595        47.31746
{% endhighlight %}

The output looks very similar to the output for the one sample t-test, with a couple of differences. 

1. The name of the test has changed to "Welch Two Sample t-test".
2. The alternative hypothesis is different.
3. There are two samples estimates, one for each group. 

Instead of using the formula method, we can code a two sample test where the data for each group is stored in a separate object. To demonstrate this
we will create two numeric vectors, one with the ages of the female participants, and one with the ages of the male partipicants. We then provide the 
two vectors as the first two argument in the ```t.test()``` function. 


{% highlight r %}
age.males<-age[male==1]
age.females<-age[male==0]

t.test(age.males, age.females)
{% endhighlight %}



{% highlight text %}
## 
## 	Welch Two Sample t-test
## 
## data:  age.males and age.females
## t = -1.739, df = 63.594, p-value = 0.08687
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -9.9461538  0.6891826
## sample estimates:
## mean of x mean of y 
##  47.31746  51.94595
{% endhighlight %}

We can perform a one-side test using the ```alternative``` argument as shown above. 


{% highlight r %}
t.test(age.males, age.females, alternative = "less")
{% endhighlight %}



{% highlight text %}
## 
## 	Welch Two Sample t-test
## 
## data:  age.males and age.females
## t = -1.739, df = 63.594, p-value = 0.04343
## alternative hypothesis: true difference in means is less than 0
## 95 percent confidence interval:
##        -Inf -0.1859434
## sample estimates:
## mean of x mean of y 
##  47.31746  51.94595
{% endhighlight %}

The default behaviour the ```t.test()``` function is to assumes unequal variance. If we wish to repeat the t-test using the assumption of equal variance
we can include the argument ```var.equal``` and set it to TRUE. 


{% highlight r %}
t.test(age~male, var.equal=TRUE)
{% endhighlight %}



{% highlight text %}
## 
## 	Two Sample t-test
## 
## data:  age by male
## t = 1.8368, df = 98, p-value = 0.06927
## alternative hypothesis: true difference in means between group 0 and group 1 is not equal to 0
## 95 percent confidence interval:
##  -0.3721683  9.6291395
## sample estimates:
## mean in group 0 mean in group 1 
##        51.94595        47.31746
{% endhighlight %}

If you are unsure whether you can assume equal variance, you can run a statistical test called an F test to confirm using the function ```var.test()```.
 The null hypothesis for this test is that variances are equal. So a significant result means that the assumption of equal variances is rejected. To compare the variances in age by gender:


{% highlight r %}
var.test(age ~ male)
{% endhighlight %}



{% highlight text %}
## 
## 	F test to compare two variances
## 
## data:  age by male
## F = 1.5248, num df = 36, denom df = 62, p-value = 0.1431
## alternative hypothesis: true ratio of variances is not equal to 1
## 95 percent confidence interval:
##  0.8663612 2.8110952
## sample estimates:
## ratio of variances 
##           1.524841
{% endhighlight %}

An alternative statistical test to test for equal variances is Bartlett's test (again, the null hypothesis is that the variances are equal for each group):


{% highlight r %}
bartlett.test(age ~ male)
{% endhighlight %}



{% highlight text %}
## 
## 	Bartlett test of homogeneity of variances
## 
## data:  age by male
## Bartlett's K-squared = 2.0664, df = 1, p-value = 0.1506
{% endhighlight %}


# Common statistical tests: Paired t-test

A paired t-test is used to compare two variables that are matched or paired in some way, for examples, measurements made on the same person at 
two different times. The paired t-test uses the differences between matched pairs of measurements to test whether the true means are equal or the 
difference between them is 0. Therefore, the length of both vectors needs to be the same.

For example, we may want to perform a paired t-test to test whether the true mean values for BP at baseline (```bp_baseline```) and BP at 
3 months (```bp_3m```) are the same, taking into account that the blood pressure measurements come from the same individual, i.e. for every
baseline measurement, there is a 'matched' measurement taken at 3 months. To do a paired t-test we need to include the argument ```paired``` and 
set it to TRUE.



{% highlight r %}
t.test(bp_3m,bp_baseline, paired=TRUE)
{% endhighlight %}



{% highlight text %}
## 
## 	Paired t-test
## 
## data:  bp_3m and bp_baseline
## t = -4.5608, df = 99, p-value = 1.462e-05
## alternative hypothesis: true mean difference is not equal to 0
## 95 percent confidence interval:
##  -23.707166  -9.332834
## sample estimates:
## mean difference 
##          -16.52
{% endhighlight %}

We can see the output is similar to before but with the following differences

1. Test title is changed to "Paired t-test"
2. The alternative hypothesis is different
3. We have a single sample estimate which is the mean difference between the groups. 

Note that the results are different if we do not
take into account the paired nature of the variables.


{% highlight r %}
t.test(bp_3m,bp_baseline,paired=FALSE)
{% endhighlight %}



{% highlight text %}
## 
## 	Welch Two Sample t-test
## 
## data:  bp_3m and bp_baseline
## t = -4.8468, df = 197.48, p-value = 2.534e-06
## alternative hypothesis: true difference in means is not equal to 0
## 95 percent confidence interval:
##  -23.241544  -9.798456
## sample estimates:
## mean of x mean of y 
##    165.88    182.40
{% endhighlight %}


## Activity 
1. Perform a single sample 2-sided t-test to test whether the true mean of baseline BP is equal to 170. 
2. Perform an unpaired t-test to compare mean BP at 3 months between Drug A and the control group. 
3. Perform a paired t-test to test the null hypothesis that mean difference is 0 comparing BP at 6 months with BP at baseline.

# Common statistical tests: Mann-Whitney test

An non-parametric alternative to a t-test is a a Mann-Whitney U test, which is performed using by function ```wilcox.test()```. 
It works in a very similar way to the two sample t- test, and many of the arguments are shared.


{% highlight r %}
wilcox.test(age~male, alternative = "greater")
{% endhighlight %}



{% highlight text %}
## 
## 	Wilcoxon rank sum test with continuity correction
## 
## data:  age by male
## W = 1374, p-value = 0.06865
## alternative hypothesis: true location shift is greater than 0
{% endhighlight %}

The output is shorter (as the test has less components) but it follows a similar format the that of the t-test.

We can save this output as a variable and extract the p-value in the same way as the t-test. The elements within 
the variable are different to the t-test output but they are accessed in the same way.


{% highlight r %}
m.out<-wilcox.test(age~male, alternative = "greater")
m.out$p.value
{% endhighlight %}



{% highlight text %}
## [1] 0.06865345
{% endhighlight %}



{% highlight r %}
names(m.out)
{% endhighlight %}



{% highlight text %}
## [1] "statistic"   "parameter"   "p.value"     "null.value"  "alternative"
## [6] "method"      "data.name"
{% endhighlight %}

# Common statistical tests: ANOVA

We perform a one-way ANOVA (ANalysis Of VAriance test) to compare means across three or more groups. The null hypothesis is that the mean 
is equal across groups. There are two ways to perform an ANOVA in R, both use the formula method to specify the comparision we want to make.

For example, to compare mean BP at 3 months across Drug A, Drug B, Control, first using the ```aov() ``` function:


{% highlight r %}
aov(bp_3m ~ intervention)
{% endhighlight %}



{% highlight text %}
## Call:
##    aov(formula = bp_3m ~ intervention)
## 
## Terms:
##                 intervention Residuals
## Sum of Squares      12718.47  41840.09
## Deg. of Freedom            2        97
## 
## Residual standard error: 20.76875
## Estimated effects may be unbalanced
{% endhighlight %}



{% highlight r %}
summary(aov(bp_3m ~ intervention))
{% endhighlight %}



{% highlight text %}
##              Df Sum Sq Mean Sq F value   Pr(>F)    
## intervention  2  12718    6359   14.74 2.57e-06 ***
## Residuals    97  41840     431                     
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
{% endhighlight %}

Note, that the ```aov()``` call doesn't output the complete test result we want. We have to additionally use the function ```summary()``` to extract and 
print the required test result. This is not an uncommon approach for performing statistical tests in R.

We can get the same result using the ```anova()``` function (give a rounding difference). This version of the anova requires a linear model to be fit first using the 
```lm()``` function.


{% highlight r %}
anova(lm(bp_3m ~ intervention))
{% endhighlight %}



{% highlight text %}
## Analysis of Variance Table
## 
## Response: bp_3m
##              Df Sum Sq Mean Sq F value    Pr(>F)    
## intervention  2  12718  6359.2  14.743 2.567e-06 ***
## Residuals    97  41840   431.3                      
## ---
## Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1
{% endhighlight %}

## Activity
Perform a one-way ANOVA to compare `age` across the three intervention groups. 


# Common statistical tests: Chi-square test

Chi square tests are used to test for a relationship between two categorical variables. 
The function is ```chisq.test()``` and requires a cross tabulation of the two variables as the input.



{% highlight r %}
chisq.test(table(male, intervention))
{% endhighlight %}



{% highlight text %}
## 
## 	Pearson's Chi-squared test
## 
## data:  table(male, intervention)
## X-squared = 1.5097, df = 2, p-value = 0.4701
{% endhighlight %}

# Common statistical tests: Correlation

When you have two continuous variables, it is likely a correlation statistics that you want to calculate. We can do this with the function ```cor()```.
For example to calculate the correlation between age and BP at baseline we can run:


{% highlight r %}
cor(age, bp_baseline)
{% endhighlight %}



{% highlight text %}
## [1] 0.01138201
{% endhighlight %}

The output of this function is very simple compared to the tests we looked at before, it is just a simple value. If you compare the function name to 
the names o fthe other functions to perform statistical tests, this doesn't have the suffix ```.test```. This function simply caluclated the value of
the correlation statistic and does not perform any hypothesis testing with it. To do that we need the ```cor.test()``` function. 

We can use ```cor.test``` to find the  correlation between `age` and `bp_baseline`


{% highlight r %}
cor.test(age, bp_baseline)
{% endhighlight %}



{% highlight text %}
## 
## 	Pearson's product-moment correlation
## 
## data:  age and bp_baseline
## t = 0.11268, df = 98, p-value = 0.9105
## alternative hypothesis: true correlation is not equal to 0
## 95 percent confidence interval:
##  -0.1854507  0.2073366
## sample estimates:
##        cor 
## 0.01138201
{% endhighlight %}

The output here is now more similar to what we had before in that it reports a number of statistics relating to the test. 

The default method for calculating the correlation is Pearson's, we can instead calculate Spearman's rank correlation coefficient, with the argument 
```method```:

{% highlight r %}
cor.test(age, bp_baseline, method="spearman")
{% endhighlight %}



{% highlight text %}
## Warning in cor.test.default(age, bp_baseline, method = "spearman"): Cannot
## compute exact p-value with ties
{% endhighlight %}



{% highlight text %}
## 
## 	Spearman's rank correlation rho
## 
## data:  age and bp_baseline
## S = 165406, p-value = 0.9412
## alternative hypothesis: true rho is not equal to 0
## sample estimates:
##         rho 
## 0.007464794
{% endhighlight %}
