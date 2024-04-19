# Data Types and Structures




# Inbuilt Datasets

R has a number of datasets included for you to practice with. 
We can get a list of these by running the command ```data()```


{% highlight r %}
data()
{% endhighlight %}

This command won't produce any output but open a file in the scripts pane that lists the available datasets.

(Alt text!)["../images/r_data.png"]

In this session, we will be using the built-in R data sets stored in the variables ```iris``` & ```mtcars```. 
By having our data stored in a variable means we can easily use it with R functions and start to
manipulate or process it. Note that we are using the word data very loosely, it can refer to any form of 
information we want to store.

# Exploring datasets

Let's take a closer look at the `iris` data.

First, let's ask what type of thing `iris` is using the function ```class()```


{% highlight r %}
class(iris)
{% endhighlight %}



{% highlight text %}
## [1] "data.frame"
{% endhighlight %}

The output tells us that it is a data frame. A data frame is an example of R object, and can be defined by certain properties.
A data frame is comparable to a spreadsheet in MS Excel as it is a 2 dimensional object (i.e. has rows and columns).
Data frames are very useful for storing data, especially if you are used to work with your data in tables. 
A typical data frame of experimental data contains individual observations in rows and variables in columns.

We can see the shape, or dimensions, of the data frame with the function ```dim()```:


{% highlight r %}
dim(iris)
{% endhighlight %}



{% highlight text %}
## [1] 150   5
{% endhighlight %}

This tells us that our data frame, `iris`, has 150 rows and 5 columns.


To explore data frames, there are a number of relevant functions:

* ```head()``` - shows first 6 rows
* ```tail()``` - shows last 6 rows
* ```dim()``` - returns the dimensions of data frame (i.e. number of rows and number of columns)
* ```nrow()``` - number of rows
* ```ncol()```- number of columns
* ```str()``` - structure of data frame - name, type and preview of data in each column
* ```names()``` or ```colnames()``` - both show the names attribute for a data frame



# Subsetting Data

There are many occasions we want to "look" at some part of the data. Extract a subset is known as slicing.
If we want to get a single value from the data frame, we can index a specific position using square brackets.
If you are familiar with matrices we index in the same way. For example, to get the element in the top left corner, i.e.
in the first row and first column we run:


{% highlight r %}
iris[1, 1]
{% endhighlight %}



{% highlight text %}
## [1] 5.1
{% endhighlight %}

We can use this principle to extract any entry of the matrix. For example the 30th row and 3rd column


{% highlight r %}
iris[30, 3]
{% endhighlight %}



{% highlight text %}
## [1] 1.6
{% endhighlight %}

An index like ``[30, 3]``` selects a single element of a data frame, but we can select larger sections as well.
For example, we can select the first three columns of values for the first four rows like this:


{% highlight r %}
iris[1:4, 1:3]
{% endhighlight %}



{% highlight text %}
##   Sepal.Length Sepal.Width Petal.Length
## 1          5.1         3.5          1.4
## 2          4.9         3.0          1.4
## 3          4.7         3.2          1.3
## 4          4.6         3.1          1.5
{% endhighlight %}

The slice ```1:4``` means, "Start at index 1 and go to index 4."

The slice does not need to start at 1, e.g. the line below selects rows 5 through 10:


{% highlight r %}
iris[5:10, 1:3]
{% endhighlight %}



{% highlight text %}
##    Sepal.Length Sepal.Width Petal.Length
## 5           5.0         3.6          1.4
## 6           5.4         3.9          1.7
## 7           4.6         3.4          1.4
## 8           5.0         3.4          1.5
## 9           4.4         2.9          1.4
## 10          4.9         3.1          1.5
{% endhighlight %}

We can use the function ```c()```, which stands for **c**ombine, to select non-contiguous entries:


{% highlight r %}
iris[c(3, 8, 37, 56), c(1,3)]
{% endhighlight %}



{% highlight text %}
##    Sepal.Length Petal.Length
## 3           4.7          1.3
## 8           5.0          1.5
## 37          5.5          1.3
## 56          5.7          4.5
{% endhighlight %}

We also don't have to provide a slice for either the rows or the columns.
If we don't include a slice for the rows, R returns all the rows; if we don't include a slice for the columns, 
R returns all the columns.
If we don't provide a slice for either rows or columns, e.g. `iris[, ]`, R returns the full data frame.


{% highlight r %}
# All columns from row 5
iris[5, ]
{% endhighlight %}



{% highlight text %}
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
## 5            5         3.6          1.4         0.2  setosa
{% endhighlight %}



{% highlight r %}
# All rows from column 2
iris[, 2]
{% endhighlight %}



{% highlight text %}
##   [1] 3.5 3.0 3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 3.7 3.4 3.0 3.0 4.0 4.4 3.9 3.5
##  [19] 3.8 3.8 3.4 3.7 3.6 3.3 3.4 3.0 3.4 3.5 3.4 3.2 3.1 3.4 4.1 4.2 3.1 3.2
##  [37] 3.5 3.6 3.0 3.4 3.5 2.3 3.2 3.5 3.8 3.0 3.8 3.2 3.7 3.3 3.2 3.2 3.1 2.3
##  [55] 2.8 2.8 3.3 2.4 2.9 2.7 2.0 3.0 2.2 2.9 2.9 3.1 3.0 2.7 2.2 2.5 3.2 2.8
##  [73] 2.5 2.8 2.9 3.0 2.8 3.0 2.9 2.6 2.4 2.4 2.7 2.7 3.0 3.4 3.1 2.3 3.0 2.5
##  [91] 2.6 3.0 2.6 2.3 2.7 3.0 2.9 2.9 2.5 2.8 3.3 2.7 3.0 2.9 3.0 3.0 2.5 2.9
## [109] 2.5 3.6 3.2 2.7 3.0 2.5 2.8 3.2 3.0 3.8 2.6 2.2 3.2 2.8 2.8 2.7 3.3 3.2
## [127] 2.8 3.0 2.8 3.0 2.8 3.8 2.8 2.8 2.6 3.0 3.4 3.1 3.0 3.1 3.1 3.1 2.7 3.2
## [145] 3.3 3.0 2.5 3.0 3.4 3.0
{% endhighlight %}

<details>
	<summary> Addressing Columns by Name </summary>
	<pre>

    Columns can also be addressed by name, with either the ```$``` operator (i.e. ```iris$Petal.Length```) 
    or square brackets (ie. ```iris[,'Petal.Length']```).
 
    </pre>
</details>



# Data Types 

One key feature of a data frame is each column is classed as a specific data type. 

*Data types*, or modes, define what the values are and how they can be used. 

There are __*5 core data types*:__

* Numeric - all real numbers e.g. 7.5
* Integer - e.g. 2
* Complex - numbers with real and imaginary parts e.g. 1+4i
* Character - consists of letters or numbers or symbols or a combination of these e.g. "a", "f5", "datatypes", "Learning R is fun".
* Logical - only takes TRUE or FALSE


These data types are also used to characterise other one dimensional R objects such as individual values or vectors 
(more on these later). R provides a number of functions to examine the features of variables or objects. 

Some examples:

* ```typeof()``` - what is the object’s data type (on the data storage level ("what the computer sees"))?
* ```class()``` - what is the object's data type (on the abstract type level("what R sees"))?
* ```mode()``` - what is the object's data type (on the data storage level ("what the computer sees"))?
* ```length()```- how long is it? 
* ```attributes()``` - does it have any metadata? 
* ```str``` - display the internal structure of an object.
* ```is.numeric()```, ```is.character()```, ```is.complex()```, ```is.logical()``` - returns TRUE when an object is the datatype queried, FALSE if not

Let's define some variables we can use R to profile the charateristics of


{% highlight r %}
x <- "dataset"
typeof(x)
{% endhighlight %}



{% highlight text %}
## [1] "character"
{% endhighlight %}


{% highlight r %}
y <- 1:10
y
{% endhighlight %}



{% highlight text %}
##  [1]  1  2  3  4  5  6  7  8  9 10
{% endhighlight %}

{% highlight r %}
typeof(y)
{% endhighlight %}



{% highlight text %}
## [1] "integer"
{% endhighlight %}



{% highlight r %}
class(y)
{% endhighlight %}



{% highlight text %}
## [1] "integer"
{% endhighlight %}


{% highlight r %}
length(y)
{% endhighlight %}



{% highlight text %}
## [1] 10
{% endhighlight %}


# Converting Between Datatypes

It can be critical that R has correctly assigned the right data type to your variable. If it has not you may run into 
errors when processing it. You therefore may want to convert between different data types. This can be done with the 
series of functions ```as.numeric```, ```as.character``` etc. 

For example, let's convert our numeric variable `y` into a character. 


{% highlight r %}
y <- as.character(y)
typeof(y)
{% endhighlight %}



{% highlight text %}
## [1] "character"
{% endhighlight %}

## Activity: Determining Data Yypes

Create a variable with the numbers 9,2,200, and 14.
What class do you predict this variable to be? Use an R function to confirm your answer.
If it is not the data type you expected, can you force R to convert it to an integer?
Divide each element of the variable in half. Does this change the type of variable?


# Data Structures

R has a number of inbuilt structures that can be used to store datasets. We have encountered one of these already 
the data.frame. Other include: 

* strings
* vectors 
* data frames
* matrices
* arrays
* lists
* factors

### Strings

A string is a run of characters. e.g. "hello". or "a189jde2mjo". They are enclosed in quotes.

### Vectors

A vector is the most common and basic data structure in R. They are an ordered collection of basic data types of 
a given length. They are one-dimensional. We can think of each column of a data frame as a vector. 

The concatenate or combine ```c()``` function will explicitly __construct__ a vector. 


{% highlight r %}
v_num <- c(9,20,12)
v_log <- c(TRUE, FALSE, FALSE, TRUE)
{% endhighlight %}

As we create these vectors you should see them listed in your environment pane. We can then call the name of the varible to see what the value is at that point in time. 


{% highlight r %}
v_num 
{% endhighlight %}



{% highlight text %}
## [1]  9 20 12
{% endhighlight %}



{% highlight r %}
v_log 
{% endhighlight %}



{% highlight text %}
## [1]  TRUE FALSE FALSE  TRUE
{% endhighlight %}

The function ```c()``` can also be used to __add elements__ to a vector.



{% highlight r %}
v_name <- c("Sarah", "Tracy", "Jon")
v_name <- c(v_name, "Annette")
v_name
{% endhighlight %}



{% highlight text %}
## [1] "Sarah"   "Tracy"   "Jon"     "Annette"
{% endhighlight %}

If we want to create a series of numbers, like 1 to 140, we can bypass the `c()` constructor and just write



{% highlight r %}
(v_int <- 1:4)
{% endhighlight %}



{% highlight text %}
## [1] 1 2 3 4
{% endhighlight %}


When we call a vector *atomic*, we mean that the vector only holds data of a single data type.

### Data Frame

A data frame is a two dimensional structure consisting of rows and columns. 

We can create a data frames using the function `data.frame()`. We will use the predefined vector `letter` 
to get the first ten letters in the alphabet.


{% highlight r %}
dat <- data.frame(id = letters[1:10], x = 1:10, y = 11:20)
dat
{% endhighlight %}



{% highlight text %}
##    id  x  y
## 1   a  1 11
## 2   b  2 12
## 3   c  3 13
## 4   d  4 14
## 5   e  5 15
## 6   f  6 16
## 7   g  7 17
## 8   h  8 18
## 9   i  9 19
## 10  j 10 20
{% endhighlight %}

Columns are variables, and each column will have a specified data type, which all entries must adhere to. 
Rows are observations. Rows and columns will have `rownames` and `colnames` that you can use to extract 
specific rows or columns respectively. 

If you read in a table of data from a file, it will typically be represented by a data.frame.

<details>
	<summary> Functions to explore data frames </summary>
	<pre>
		
* ```head()``` - shows first 6 rows
* ```tail()``` - shows last 6 rows
* ```dim()``` - returns the dimensions of data frame (i.e. number of rows and number of columns)
* ```nrow()``` - number of rows
* ```ncol()```- number of columns
* ```str()``` - structure of data frame - name, type and preview of data in each column
* ```names()``` or ```colnames()``` - both show the names attribute for a data frame

    </pre>
</details>


### Matrices

A matrix is another two dimensional object, but it differs to a data.frame as all columns/entries must be of the same type. 
It is more efficient memory wise than a data.frame, but can not be used as a substitute to all data.frames.

We can construct a matrix as follows:


{% highlight r %}
m<-matrix(1:6, nrow=2, ncol=3)
m
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    3    5
## [2,]    2    4    6
{% endhighlight %}

When creating a __matrix__, it is important to remember that matrices __*are filled column-wise*__ If that is not what you want, you can use the ```byrow``` argument (a logical: can be ```TRUE``` or ```FALSE```) to specify how the matrix is filled


{% highlight r %}
m<-matrix(1:6, nrow=2, ncol=3, byrow=TRUE)
m
{% endhighlight %}



{% highlight text %}
##      [,1] [,2] [,3]
## [1,]    1    2    3
## [2,]    4    5    6
{% endhighlight %}

We can confirm the data type of a matrix with the function `class`.


{% highlight r %}
class(m)
{% endhighlight %}



{% highlight text %}
## [1] "matrix" "array"
{% endhighlight %}

### Arrays

Arrays are n dimensional storage structures. A one dimensional array is a vector, a two dimensional array is a matrix. 

We will not be using this type of object, but it is included for completeness.

### Lists

A list in R is a collection of objects and elements, which themselves can be a heterogeneous mix of other objects 
including vectors, matrices, data.frames, functions, strings, numbers. They tend to be used to collate different 
data types connected in some way. 

We can create a list of the vectors, data.frames we have already constructed as follows.



{% highlight r %}
l <- list(v_log, v_num, v_it, iris)
{% endhighlight %}



{% highlight text %}
## Error in eval(expr, envir, enclos): object 'v_it' not found
{% endhighlight %}



{% highlight r %}
l
{% endhighlight %}



{% highlight text %}
## Error in eval(expr, envir, enclos): object 'l' not found
{% endhighlight %}


### Factors

Sometimes considered as a data type, as confusingly it is a possible response to the function `type`, and therefore
a valid option for columns in a data frame. A factor is designed for categorical variables. They have a finite number of 
"levels", which are the options that any element of that vector can take. They are actually stored as integers 
which can make them quite powerful for subsetting. 

It is very easy for character vectors to be inappropriately stored as factors and vice versa. In fact, R's default 
when loading data is to store a string as a factor. Conversely if we define a vector we have to explicit convert 
it to a vector

For example, if we define a vector of months, the default is to class it as a vector of characters. We have to actively 
coerce it into a factor. 


{% highlight r %}
a      <- c("March","February","February","November","February","March","March","March","February","November")
class(a)
{% endhighlight %}



{% highlight text %}
## [1] "character"
{% endhighlight %}



{% highlight r %}
fact <- as.factor(a)
class(a)
{% endhighlight %}



{% highlight text %}
## [1] "character"
{% endhighlight %}



## Activity: Data Exploration

Use these functions to explore the mtcars dataset

* How large is the dataset?
* What type is the object?
* What value is in the 6th row of the 4th column?
