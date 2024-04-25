# R Training: Session 2
# Data Types and Structures

'
Date: August 2022
Author: T. Wacker
Adapted: Laura Roldan-Gomez
'

# 1. Set Working Directory----

setwd("C:/Users/YourUserName/OneDrive -University of Exeter/YourFolder")

# 2. Data Types - *The basis of it all*----

# *Data types* define how the values are stored in the computer. There are 3 core data types:

## 2.1. Numeric----

3 # This is a number
class(3) # you can check. The function class() and typeof() returns the datatype of an object
typeof(3) # another way of checking (double and numeric are the same thing)

15.5 # This is also a number
class(15.5)

#- complex:
1+4i # This is also a number
class(1+4i)

## 2.2. Characters or strings:----

# consists of letters, words, sentences or characters, such as:

"a" # note the quote marks
"datatypes"
"Learning R is fun"
"@%£$"

class("a") # Check

# Basically, anything within "" is a character or string, so... numbers can also be characters! 
3 # This is a number
2 # This is also a number

3-2 # I can treat them as numbers

# NOW...
"3" # This is not a number
"2" # This is not a number

"3"-"2" # I cannot treat them as numbers


## 2.3. Logical:----

# Logical values can either be TRUE or FALSE or sometimes 1 and 0. 

# That means that if you type:

z = as.logical(c(1,0,0,1))
typeof(z)

z = (c(1,0,0,1)) # if you don't use as.logical you get a set of numbers
typeof(z)


# 3. Data Structures----

# * vectors:
  ## * atomic vector
  ## * list
# * matrix
# * data frame
# * factors

## 3.1. Vectors----
# A vector is the most common and basic data structure in R. Technically, vectors can be one of two types:

### a. atomic vectors:----
# only holds elements (or atoms) of a single data type and each atom is a scalar, which means it “has length one”. It is *homogenous*.

# Examples:
x <- 3 # a vector of one number

y <- 1:5 # numbers from 1 to 5

y_times_two <- (y*2) # vector b multiplied by two

z <- letters[1:5] # the first 5 letters of the alphabet

v_log <- c(TRUE, FALSE, FALSE, TRUE, TRUE) # a logical vector


##---------------------------------------##

## THREE VERY IMPORTANT THINGS BEFORE WE GO ON: CONCATENATE, INDEXING AND COERCION

## Concatenate----
# The concatenate or combine c() function will construct a vector. We used it above to construct the logical vector. 

# The function c() can also be used to add elements to a vector.

v_name <- c("Sarah", "Tracy", "Jon")
v_name

v_name <- c(v_name, "Annette")
v_name

# 

v_name<- c("Greg", v_name)
v_name



# Let's put this together and create our first little data set. We'll work with data sets further down but I want to wrap up this section with one of the functions of vectors. 

# We use two functions: as.data.frame and cbind or column bind.

ourdata <- as.data.frame(cbind(v_name, x, y, y_times_two, z, v_log))

ourdata2 <- as.data.frame(rbind(v_name, x, y, y_times_two, z, v_log)) # we can also use rbind or row bind. Run this and see the difference.


## Indexing----

# Every atom in a vector has a 'location' represented by a number or index. Our vector x from the previous exercise has length one. So the index for 3 is 1.

# Likewise, vector z has 5 letters and therefore, 5 indexes.

# We can call this numbers by using []

x[1]

x[0] # index 0 doesn't exist in this vector

x[2] # index 2 doesn't exist in this vector

z[3] # running this line will give you the letter in position 3.

# You can also use index ranges:
z[2:3]

# You can also remove an element by using a negative number
z[-5] # removes the last element
z[-(1:3)] # removes the first three elements


# Indexing data frames: the positions in a data frame behave like a coordinate [row, column]. So you have

ourdata[1,1] # element in the first row and first column

# And you can also use indexing to get whole columns or rows. 

ourdata[2] # I get the second column 

ourdata[-2] # I removed the second column

ourdata[1,] # I get the first row

ourdata[,(2:3)] # I get columns 2 and 3

new_subset <- ourdata[(1:3),(2:4)] # we can even create a new data frame using this. It's great when you have huge data sets but you are interested in just a few variables.

new_subset[1,1] <- "Laura" # I can also change elements in my dataframe.


## Data type coercion----

# Even though R’s vectors have a specific data type, it’s quite easy to coerce them to another type.

# Let's look at our data set and see what type of data we have:

str(ourdata)

# Careful: coercion can also be triggered by other actions. When R joined our vectors to form a data frame, it read every element as a character. When you use real data, you must check this before running any analysis. And you need to coerce the data to whatever makes sense.

# For instance, we must coerce our variables x, y, y_times_two to numeric and variable v_log to logic

ourdata$x<-as.numeric(ourdata$x)

ourdata$y<-as.numeric(ourdata$y)

ourdata$y_times_two<-as.numeric(ourdata$y_times_two)

ourdata$v_log <- as.logical(ourdata$v_log)

str(ourdata) # This is making more sense

# If you need to change something to character, you use as.character


### b. lists:---- 
# lists are still vectors but can contain several datatypes (can be *heterogenous*) and each atom of the list can itself be composed of more than one atom (has a length > one). 

# Atomic vectors are very constrained: atoms are of a scalar/length 1 and need to be one data type. You might find yourself needing a vector that violates these constraints and that can have length greater than 1 and not be of the same type.

# We construct a list explicitly with list() but, like atomic vectors, most lists are created some other way in real life.

(a_list <- list(1:3, c("four", "five")))

# A more impressive one
(b_list <- list(logical = TRUE, integer = 4L, double = 4 * 1.2, character = "character"))

# A very impressive one
(c_list <- list(letters[26:22], transcendental = c(pi, exp(1)), f = function(x) x^2))


# You can also coerce other objects using as.list(). 
ourdata_as_list <- as.list(ourdata)


## List indexing----

# There are 3 ways to index a list and the differences are very important:

# 1.) With single square brackets, just like we indexed atomic vectors. Note this always returns a list, even if we request a single component.

a_list[c(FALSE, TRUE)]
b_list[2:3]
c_list["transcendental"]

ourdata_as_list[1]


# 2.) With double square brackets. This can only be used to access a single component and it returns the “naked” component. You can request a component with a positive integer or by name.

a_list[[2]]

b_list[["double"]]

ourdata_as_list[[1]]


# 3.) With the $ addressing named components. Like [[, this can only be used to access a single component, but it is even more limited: You must specify the component by name.

ourdata_as_list$v_name

## How can I use this?
# This is a bit advanced as it uses loops but a good example of where you can use lists...
why_lists <- list() # create an empty list

for (i in 1:5){
  why_lists[[i]] <- ourdata[(i-1):(i),]
} # loop over your data to create many data frames and keep them in a list. I'm currently using this as part of my PhD for which I am running over 13.000 models! So yes, lists can be useful.


# A very good and easy-to-grasp explanation of the difference between the list-preserving indexing provided by [ and the behaviour of [[ is given here: [the pepper shaker analogy on R for Data Science](https://r4ds.had.co.nz/vectors.html#lists-of-condiments).

#-----------------------------------------#
### Tasks----
#-----------------------------------------#

# 1. What is the class of ourdata_as_list[1]?

# 2. What is the class of ourdata_as_list[[1]]?

# 3. Consider 
my_vec <- c(a = 1, b = 2, c = 3)
my_list <- list(a = 1, b = 2, c = 3)
# Use [ and [[ to attempt to retrieve elements 2 and 3 from my_vec and my_list. What succeeds vs. fails? What if you try to retrieve element 2 alone? Does [[ even work on atomic vectors? Compare and contrast the results from the various combinations of indexing method and input object.

#-----------------------------------------##-----------------------------------------#

# 4. Data frames----
# Data frames are the data structure you will use the most for statistics or data management in general.

## 4.1. Get your data:

# To get your data in R, you can do one of three things:

## Create your own data set (we did that already with 'ourdata')

## Use a built-in data set like iris
iris

## Load your own data. There are multiple ways to load your data, for example using the command read.csv:

worms <- read.csv("/Users/roldix/Library/Mobile Documents/com~apple~CloudDocs/GitHub_Repos/r-training/r_training_session_2/data/worms.csv")

## 4.1 Create a data frame:----

# First, let's create a data frame by hand using the command data.frame (previously, we used a different method):
dat <- data.frame(id = letters[1:10], x = 1:10, y = 11:20)
dat

## 4.2. Explore a data frame:----

# Second, let's use several commands to explore a data frame:

head(dat) # shows first 6 rows
tail(dat)    # shows last 6 rows
dim(dat)     # returns the dimensions of data frame (i.e. number of rows and number of columns)
nrow(dat)    # number of rows
ncol(dat)    # number of columns
str(dat)     # structure of data frame - name, type and preview of data in each column

names(dat)
colnames(dat)# both show the names attribute for a data frame

sapply(dat, class) # shows the class of each column in the data frame



# Below we show that a data frame is actually a special list:

is.list(dat)
class(dat)


## 4.3. Indexing/slicing---- 

# As shown above, there are ways to retrieve specific elements from the data frame, the data frame can be *sliced* or *indexed* .
# Because data frames are rectangular, elements of data frame can be referenced by specifying the row and the column index in single square brackets.

dat[1, 3] # You know this already, this is a reminder

# As data frames are also lists, it is possible to refer to columns (which are elements of such list) using the list notation, i.e. either double square brackets or a $.

dat[["y"]]
dat$y


## 4.4. Restructure your data frame - *pimp up your data frame*----  

### a. Add and change names:----

# When you look at both the dat and iris data frames from earlier, they have no rownames
dat
head(iris)


# However, when we look at the mtcars data set, it does

head(mtcars) # *mtcars has rownames!*

# Let's assume we want to make dat a bit more fancy and we want to give each row a name. What could we do? 
# Albeit a bit non-sensical (but the entire data frame is just a generic example), we could name the rows as follows:

names<-c("first","second","third","fourth","fifth","sixth", "seventh","eighth","ninth","tenth") # we create a vector
rownames(dat)=names # we assign the vectors as rownames for dat
dat

# We can also rename columns. Let's assume we want to change the abbreviation of the first three columns of mtcars to the actual words:

colnames(mtcars)[1:3]<-c("miles per gallon","cylinders","displacement")
head(mtcars)

# By using [1:3] we only changed a subset of the column names. If you want to change them all, the vector with the column names must correspond to the number of columns (be of identical length/ have the same 1D dimension). 

### b. Append a column----
# You can also append a column of choice to your data frame. Remember, it needs to have the same length as the other columns:

# find out how many rows our mtcars actually has:
nrow(mtcars)
# generate new column
favorites=1:32
# append
mtcars$favorites=favorites
mtcars

### c. Subset your data:----
# We can also subset (or filter based on a conditional statement) a data frame using subset. The function takes two arguments subset(x, condition). X is the data frame to perform subset on, condition is the conditional statement to subset with:

subset(mtcars, cylinders>4)

#-----------------------------------------#
### Tasks ----
#-----------------------------------------#

# Load the dataset worms

# Try the command 'summary()'

# Try to selectively rename 2 rows of your choice in mtcars.

# Try out what happens if you try to add a new column of a length that is less than 32.
# Extract (using either [] or $) the columns Sepal.Length and Sepal.Width from the iris dataset and make a new data frame out of them using data.frame(). Subset the new data frame for Sepal.Length > 4.6.

#-----------------------------------------#
#-----------------------------------------#

# 5. Special section - Factors----
# Think about categories. 
# Factors are so-called *derived data types*. They are normally used to group variables into unique categories or levels. For example, a data set may be grouped by gender or month of the year. Such data are usually loaded into R as a numeric or character data type requiring that they be converted to a factor using the as.factor() function.

## 5.1. Create a factor:----
# In the following chunk of code, we create a factor from a character object.

mon <- c("March","February","February","November","February","March","March","March","February","November")
fact <- as.factor(mon)

# Note that a is of character data type and fact is the factor representation of a.

typeof(mon)

typeof(fact) # However, the derived object fact is now stored as an integer!
fact # Yet, when displaying the contents of fact we see character values.

# How can this be?
# Well, fact is a *more complicated object* than the simple objects created thus far in that the factor is storing additional information not seen in its output. This hidden information is stored in attributes. To view these hidden attributes, use the attributes() function.

attributes(fact)

# There are two attributes of the factor object fact : class and levels. 
class(fact)
levels(fact) # lists the three unique values in fact. The order reflects their *numeric* representation. In essence, fact is storing each value as an integer that points to one of the three unique levels.

## 5.2. Use of a factor:----
# To *appreciate the benefits of a factor we’ll first create a data frame*. One column will be assigned the fact factor and another will be assigned some random numeric values.

x <- c(166, 47, 61, 148, 62, 123, 232, 98, 93, 110)
dat_fact <- data.frame(min_sunshine = x, month = fact)
dat_fact

# The month column is now a factor with three levels: F, M and N. We can use the str()`` function to view the dataframe’s structure as well as its columns classes.

str(dat_fact)

# There are functions that recognize factor data types and allow you to split the output into groups defined by the factor’s unique levels. For example, to create three box plots of the value min_sunshine, one for each month group F, M and N:

boxplot(min_sunshine ~ month, dat_fact, horizontal = TRUE)

# The tilde ~ operator is used in the plot function to split (or condition) the data into separate plots based on the factor month.

## 5.3. Rearranging level order----

# *A factor will define a hierarchy for its levels*. When we invoked the levels function in the last example, you may have noted that the levels output were ordered F, M and N–this is the level hierarchy defined for months (i.e. F>M>N ). This means that regardless of the order in which the factors appear in a table, *anytime a plot or operation is conditioned by the factor, the grouped elements will appear in the order defined by the levels’ hierarchy*.

# If we wanted the box plots to be plotted in a different order we must modify the month column by *releveling* the factor object as follows:

dat_fact$month <- factor(dat_fact$month, levels=c("November","February","March"))
str(dat_fact)

boxplot(min_sunshine ~ month, dat_fact, horizontal = TRUE)

#-----------------------------------------#
### Tasks----
#-----------------------------------------#

# Load the dataset esoph. This data frame contains the data from a case-control study of (o)esophageal cancer in Ille-et-Vilaine, France.

# * remove the last column of the data frame.

# * rename the columns from agegp to Age_Group, from alcgp to Alcohol_consump, from tobgp to Tobacco_consump and leave the column name of ncases the same.

# * subset the dataframe to only contain rows that have an Alcohol_consump of 120+.

# * convert the agegp into a factor and assign it to a new variable. Assess the attributes of that variable.

# * What data type is Alcohol_consump?

#-----------------------------------------##-----------------------------------------#

# 6. Matrices----

# Matrices are atomic vectors with dimensions; the number of rows and columns. As with atomic vectors, the elements of a matrix must be of the same data type.

# To create an empty matrix, we need to define those dimensions:

m<-matrix(nrow=2, ncol=2)
m

# We can find out how many dimensions a matrix has by using

dim(m)

# You can check that matrices are vectors with a class attribute of matrix by using class() and typeof().

m <- matrix(c(1:3))
class(m)
typeof(m)

# While class() shows that m is a matrix, typeof() shows that in this case *fundamentally the matrix is an integer vector* (we will see later that they are not always integer vectors, but can be character vectors, too.

# When creating a matrix, it is important to remember that matrices *are filled column-wise*

m<-matrix(1:6, nrow=2, ncol=3)
m

# If that is not what you want, you can use the byrow argument (a logical: can be TRUE or FALSE) to specify how the matrix is filled

m<-matrix(1:6, nrow=2, ncol=3, byrow=TRUE)
m

# You can create a matrix from a vector:

m<-sample(1:100, size=10)
m
dim(m)<-c(2,5)
m

# *A lot is going on here. Let's dissect it*:

# * We generate a random integer vector using sample(). sample() in this case randomly draws 10 (size=10) numbers from 1 to 100 (1:100)^[if you want to get the same vector each time with the same parameters, you need to use set.seed() with a defined number first].

# * we assign the vector dimensions using dim() and c(2,5), with the later being c(rows, columns).

# All of the above takes the random integer vector and transforms it into a matrix with 2 rows and 5 columns. 

# You can also bind columns and rows using cbind() and rbind:

x <- 1:3
y <- 10:12
m<-cbind(x, y)
m
n<-rbind(x,y)
n


# If we want to retrieve an element we can do so by using: 

## 6.1. Matrix indexing----

# Akin to vectors, we revisit our square-brackets and can retrieve elements of a matrix by specifying the index along each dimension (e.g. “row” and “column”) in single square brackets.

m[3,2] # Note that it is [row,column].


#-----------------------------------------#
### Tasks ----
#-----------------------------------------#

# 1. Transform the built-in dataset iris into a matrix using as.matrix() and assign it to a new variable of your choice.

# 2. When you use class() and typeof(), what results do you get and why? What happened to the doubles in the data frame (hint: remember the coercion rules from earlier)?

#-----------------------------------------#
#-----------------------------------------#


#           THE END... for now.

# Congratulations! This was hard but do keep going. Join us for Session 3 - Manipulating and Plotting Data. Hopefully, you will find it easier than today.
