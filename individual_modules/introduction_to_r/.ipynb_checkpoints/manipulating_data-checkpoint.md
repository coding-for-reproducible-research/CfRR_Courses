# Manipulating Datasets

Often we need to manipulate or extract parts of our dataset prior to doing any analysis or plotting with it.



# Conditional Subsetting

We have already looked at slicing subsets, where we knew the indexs of the rows or columns of the entries we wanted. 
There may be times when, instead we want to select rows based on a specific condition. This would require a conditional 
statement. Conditional commands check if criteria is met and return either TRUE or FALSE in response.

Let's find which rows of ```iris``` have a ```Sepal.Length``` less than 7.


{% highlight r %}
iris$Sepal.Length < 6
{% endhighlight %}



{% highlight text %}
##   [1]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
##  [13]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
##  [25]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
##  [37]  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE  TRUE
##  [49]  TRUE  TRUE FALSE FALSE FALSE  TRUE FALSE  TRUE FALSE  TRUE FALSE  TRUE
##  [61]  TRUE  TRUE FALSE FALSE  TRUE FALSE  TRUE  TRUE FALSE  TRUE  TRUE FALSE
##  [73] FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE  TRUE FALSE
##  [85]  TRUE FALSE FALSE FALSE  TRUE  TRUE  TRUE FALSE  TRUE  TRUE  TRUE  TRUE
##  [97]  TRUE FALSE  TRUE  TRUE FALSE  TRUE FALSE FALSE FALSE FALSE  TRUE FALSE
## [109] FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE
## [121] FALSE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE
## [133] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE FALSE
## [145] FALSE FALSE FALSE FALSE FALSE  TRUE
{% endhighlight %}

Where is says TRUE means the criteria have been met and FALSE not. We can use this to subset the rows of iris


{% highlight r %}
iris[iris$Sepal.Length < 6,]
{% endhighlight %}



{% highlight text %}
##     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
## 1            5.1         3.5          1.4         0.2     setosa
## 2            4.9         3.0          1.4         0.2     setosa
## 3            4.7         3.2          1.3         0.2     setosa
## 4            4.6         3.1          1.5         0.2     setosa
## 5            5.0         3.6          1.4         0.2     setosa
## 6            5.4         3.9          1.7         0.4     setosa
## 7            4.6         3.4          1.4         0.3     setosa
## 8            5.0         3.4          1.5         0.2     setosa
## 9            4.4         2.9          1.4         0.2     setosa
## 10           4.9         3.1          1.5         0.1     setosa
## 11           5.4         3.7          1.5         0.2     setosa
## 12           4.8         3.4          1.6         0.2     setosa
## 13           4.8         3.0          1.4         0.1     setosa
## 14           4.3         3.0          1.1         0.1     setosa
## 15           5.8         4.0          1.2         0.2     setosa
## 16           5.7         4.4          1.5         0.4     setosa
## 17           5.4         3.9          1.3         0.4     setosa
## 18           5.1         3.5          1.4         0.3     setosa
## 19           5.7         3.8          1.7         0.3     setosa
## 20           5.1         3.8          1.5         0.3     setosa
## 21           5.4         3.4          1.7         0.2     setosa
## 22           5.1         3.7          1.5         0.4     setosa
## 23           4.6         3.6          1.0         0.2     setosa
## 24           5.1         3.3          1.7         0.5     setosa
## 25           4.8         3.4          1.9         0.2     setosa
## 26           5.0         3.0          1.6         0.2     setosa
## 27           5.0         3.4          1.6         0.4     setosa
## 28           5.2         3.5          1.5         0.2     setosa
## 29           5.2         3.4          1.4         0.2     setosa
## 30           4.7         3.2          1.6         0.2     setosa
## 31           4.8         3.1          1.6         0.2     setosa
## 32           5.4         3.4          1.5         0.4     setosa
## 33           5.2         4.1          1.5         0.1     setosa
## 34           5.5         4.2          1.4         0.2     setosa
## 35           4.9         3.1          1.5         0.2     setosa
## 36           5.0         3.2          1.2         0.2     setosa
## 37           5.5         3.5          1.3         0.2     setosa
## 38           4.9         3.6          1.4         0.1     setosa
## 39           4.4         3.0          1.3         0.2     setosa
## 40           5.1         3.4          1.5         0.2     setosa
## 41           5.0         3.5          1.3         0.3     setosa
## 42           4.5         2.3          1.3         0.3     setosa
## 43           4.4         3.2          1.3         0.2     setosa
## 44           5.0         3.5          1.6         0.6     setosa
## 45           5.1         3.8          1.9         0.4     setosa
## 46           4.8         3.0          1.4         0.3     setosa
## 47           5.1         3.8          1.6         0.2     setosa
## 48           4.6         3.2          1.4         0.2     setosa
## 49           5.3         3.7          1.5         0.2     setosa
## 50           5.0         3.3          1.4         0.2     setosa
## 54           5.5         2.3          4.0         1.3 versicolor
## 56           5.7         2.8          4.5         1.3 versicolor
## 58           4.9         2.4          3.3         1.0 versicolor
## 60           5.2         2.7          3.9         1.4 versicolor
## 61           5.0         2.0          3.5         1.0 versicolor
## 62           5.9         3.0          4.2         1.5 versicolor
## 65           5.6         2.9          3.6         1.3 versicolor
## 67           5.6         3.0          4.5         1.5 versicolor
## 68           5.8         2.7          4.1         1.0 versicolor
## 70           5.6         2.5          3.9         1.1 versicolor
## 71           5.9         3.2          4.8         1.8 versicolor
## 80           5.7         2.6          3.5         1.0 versicolor
## 81           5.5         2.4          3.8         1.1 versicolor
## 82           5.5         2.4          3.7         1.0 versicolor
## 83           5.8         2.7          3.9         1.2 versicolor
## 85           5.4         3.0          4.5         1.5 versicolor
## 89           5.6         3.0          4.1         1.3 versicolor
## 90           5.5         2.5          4.0         1.3 versicolor
## 91           5.5         2.6          4.4         1.2 versicolor
## 93           5.8         2.6          4.0         1.2 versicolor
## 94           5.0         2.3          3.3         1.0 versicolor
## 95           5.6         2.7          4.2         1.3 versicolor
## 96           5.7         3.0          4.2         1.2 versicolor
## 97           5.7         2.9          4.2         1.3 versicolor
## 99           5.1         2.5          3.0         1.1 versicolor
## 100          5.7         2.8          4.1         1.3 versicolor
## 102          5.8         2.7          5.1         1.9  virginica
## 107          4.9         2.5          4.5         1.7  virginica
## 114          5.7         2.5          5.0         2.0  virginica
## 115          5.8         2.8          5.1         2.4  virginica
## 122          5.6         2.8          4.9         2.0  virginica
## 143          5.8         2.7          5.1         1.9  virginica
## 150          5.9         3.0          5.1         1.8  virginica
{% endhighlight %}

# Matching

There are several circumstances we will need to check for matching and use that information. There are several ways 
we can do this using R depending on what we need.

Using identical(), we can check if values or collections of values are identical.


{% highlight r %}
# Checking if the first and second row values in the "Species" column of iris are identical
identical(iris$Species[1], iris$Species[2])
{% endhighlight %}



{% highlight text %}
## [1] TRUE
{% endhighlight %}



{% highlight r %}
# Checking if the first and 51st row values in the "Species" column of iris are identical
identical(iris$Species[1], iris$Species[51])
{% endhighlight %}



{% highlight text %}
## [1] FALSE
{% endhighlight %}

Using all.equal() is similar to identical(), but allows for some tolerance in how similar values can be. For example, we may want to check two numbers with lots of decimal places, but only need them to be within 0.01 of each other. Therefore we can give a tolerance of 0.01


{% highlight r %}
x1 <- 1.232529
x2 <- 1.23366
all.equal(x1, x2, tolerance=0.01)
{% endhighlight %}



{% highlight text %}
## [1] TRUE
{% endhighlight %}



{% highlight r %}
all.equal(x1, x2, tolerance=0.0001)
{% endhighlight %}



{% highlight text %}
## [1] "Mean relative difference: 0.0009176255"
{% endhighlight %}

We can use "==" as a selector to pull all matching entries. We can give a numeric value or a character in quotations.


{% highlight r %}
iris[iris$Species == "setosa", ]
{% endhighlight %}



{% highlight text %}
##    Sepal.Length Sepal.Width Petal.Length Petal.Width Species
## 1           5.1         3.5          1.4         0.2  setosa
## 2           4.9         3.0          1.4         0.2  setosa
## 3           4.7         3.2          1.3         0.2  setosa
## 4           4.6         3.1          1.5         0.2  setosa
## 5           5.0         3.6          1.4         0.2  setosa
## 6           5.4         3.9          1.7         0.4  setosa
## 7           4.6         3.4          1.4         0.3  setosa
## 8           5.0         3.4          1.5         0.2  setosa
## 9           4.4         2.9          1.4         0.2  setosa
## 10          4.9         3.1          1.5         0.1  setosa
## 11          5.4         3.7          1.5         0.2  setosa
## 12          4.8         3.4          1.6         0.2  setosa
## 13          4.8         3.0          1.4         0.1  setosa
## 14          4.3         3.0          1.1         0.1  setosa
## 15          5.8         4.0          1.2         0.2  setosa
## 16          5.7         4.4          1.5         0.4  setosa
## 17          5.4         3.9          1.3         0.4  setosa
## 18          5.1         3.5          1.4         0.3  setosa
## 19          5.7         3.8          1.7         0.3  setosa
## 20          5.1         3.8          1.5         0.3  setosa
## 21          5.4         3.4          1.7         0.2  setosa
## 22          5.1         3.7          1.5         0.4  setosa
## 23          4.6         3.6          1.0         0.2  setosa
## 24          5.1         3.3          1.7         0.5  setosa
## 25          4.8         3.4          1.9         0.2  setosa
## 26          5.0         3.0          1.6         0.2  setosa
## 27          5.0         3.4          1.6         0.4  setosa
## 28          5.2         3.5          1.5         0.2  setosa
## 29          5.2         3.4          1.4         0.2  setosa
## 30          4.7         3.2          1.6         0.2  setosa
## 31          4.8         3.1          1.6         0.2  setosa
## 32          5.4         3.4          1.5         0.4  setosa
## 33          5.2         4.1          1.5         0.1  setosa
## 34          5.5         4.2          1.4         0.2  setosa
## 35          4.9         3.1          1.5         0.2  setosa
## 36          5.0         3.2          1.2         0.2  setosa
## 37          5.5         3.5          1.3         0.2  setosa
## 38          4.9         3.6          1.4         0.1  setosa
## 39          4.4         3.0          1.3         0.2  setosa
## 40          5.1         3.4          1.5         0.2  setosa
## 41          5.0         3.5          1.3         0.3  setosa
## 42          4.5         2.3          1.3         0.3  setosa
## 43          4.4         3.2          1.3         0.2  setosa
## 44          5.0         3.5          1.6         0.6  setosa
## 45          5.1         3.8          1.9         0.4  setosa
## 46          4.8         3.0          1.4         0.3  setosa
## 47          5.1         3.8          1.6         0.2  setosa
## 48          4.6         3.2          1.4         0.2  setosa
## 49          5.3         3.7          1.5         0.2  setosa
## 50          5.0         3.3          1.4         0.2  setosa
{% endhighlight %}

We can use objects or parts of objects to select rows and columns within [ ] using the "%in%".   


{% highlight r %}
select <- "versicolor"
iris[iris$Species %in% select, ]
{% endhighlight %}



{% highlight text %}
##     Sepal.Length Sepal.Width Petal.Length Petal.Width    Species
## 51           7.0         3.2          4.7         1.4 versicolor
## 52           6.4         3.2          4.5         1.5 versicolor
## 53           6.9         3.1          4.9         1.5 versicolor
## 54           5.5         2.3          4.0         1.3 versicolor
## 55           6.5         2.8          4.6         1.5 versicolor
## 56           5.7         2.8          4.5         1.3 versicolor
## 57           6.3         3.3          4.7         1.6 versicolor
## 58           4.9         2.4          3.3         1.0 versicolor
## 59           6.6         2.9          4.6         1.3 versicolor
## 60           5.2         2.7          3.9         1.4 versicolor
## 61           5.0         2.0          3.5         1.0 versicolor
## 62           5.9         3.0          4.2         1.5 versicolor
## 63           6.0         2.2          4.0         1.0 versicolor
## 64           6.1         2.9          4.7         1.4 versicolor
## 65           5.6         2.9          3.6         1.3 versicolor
## 66           6.7         3.1          4.4         1.4 versicolor
## 67           5.6         3.0          4.5         1.5 versicolor
## 68           5.8         2.7          4.1         1.0 versicolor
## 69           6.2         2.2          4.5         1.5 versicolor
## 70           5.6         2.5          3.9         1.1 versicolor
## 71           5.9         3.2          4.8         1.8 versicolor
## 72           6.1         2.8          4.0         1.3 versicolor
## 73           6.3         2.5          4.9         1.5 versicolor
## 74           6.1         2.8          4.7         1.2 versicolor
## 75           6.4         2.9          4.3         1.3 versicolor
## 76           6.6         3.0          4.4         1.4 versicolor
## 77           6.8         2.8          4.8         1.4 versicolor
## 78           6.7         3.0          5.0         1.7 versicolor
## 79           6.0         2.9          4.5         1.5 versicolor
## 80           5.7         2.6          3.5         1.0 versicolor
## 81           5.5         2.4          3.8         1.1 versicolor
## 82           5.5         2.4          3.7         1.0 versicolor
## 83           5.8         2.7          3.9         1.2 versicolor
## 84           6.0         2.7          5.1         1.6 versicolor
## 85           5.4         3.0          4.5         1.5 versicolor
## 86           6.0         3.4          4.5         1.6 versicolor
## 87           6.7         3.1          4.7         1.5 versicolor
## 88           6.3         2.3          4.4         1.3 versicolor
## 89           5.6         3.0          4.1         1.3 versicolor
## 90           5.5         2.5          4.0         1.3 versicolor
## 91           5.5         2.6          4.4         1.2 versicolor
## 92           6.1         3.0          4.6         1.4 versicolor
## 93           5.8         2.6          4.0         1.2 versicolor
## 94           5.0         2.3          3.3         1.0 versicolor
## 95           5.6         2.7          4.2         1.3 versicolor
## 96           5.7         3.0          4.2         1.2 versicolor
## 97           5.7         2.9          4.2         1.3 versicolor
## 98           6.2         2.9          4.3         1.3 versicolor
## 99           5.1         2.5          3.0         1.1 versicolor
## 100          5.7         2.8          4.1         1.3 versicolor
{% endhighlight %}



# Merging and Binding 

We will often need to bring multiple two-dimensional objects together. We can do this multiple ways. 

Using rbind() and cbind(), we can combine objects together. rbind() allows us to bind together rows.


{% highlight r %}
# First we look at the dimension of "iris"
dim(iris)
{% endhighlight %}



{% highlight text %}
## [1] 150   5
{% endhighlight %}



{% highlight r %}
# Using rbind() to put together two copies of  causing double rows
rbind(iris, iris) -> iris.r
dim(iris.r)
{% endhighlight %}



{% highlight text %}
## [1] 300   5
{% endhighlight %}



{% highlight r %}
iris.r[ ,1]
{% endhighlight %}



{% highlight text %}
##   [1] 5.1 4.9 4.7 4.6 5.0 5.4 4.6 5.0 4.4 4.9 5.4 4.8 4.8 4.3 5.8 5.7 5.4 5.1
##  [19] 5.7 5.1 5.4 5.1 4.6 5.1 4.8 5.0 5.0 5.2 5.2 4.7 4.8 5.4 5.2 5.5 4.9 5.0
##  [37] 5.5 4.9 4.4 5.1 5.0 4.5 4.4 5.0 5.1 4.8 5.1 4.6 5.3 5.0 7.0 6.4 6.9 5.5
##  [55] 6.5 5.7 6.3 4.9 6.6 5.2 5.0 5.9 6.0 6.1 5.6 6.7 5.6 5.8 6.2 5.6 5.9 6.1
##  [73] 6.3 6.1 6.4 6.6 6.8 6.7 6.0 5.7 5.5 5.5 5.8 6.0 5.4 6.0 6.7 6.3 5.6 5.5
##  [91] 5.5 6.1 5.8 5.0 5.6 5.7 5.7 6.2 5.1 5.7 6.3 5.8 7.1 6.3 6.5 7.6 4.9 7.3
## [109] 6.7 7.2 6.5 6.4 6.8 5.7 5.8 6.4 6.5 7.7 7.7 6.0 6.9 5.6 7.7 6.3 6.7 7.2
## [127] 6.2 6.1 6.4 7.2 7.4 7.9 6.4 6.3 6.1 7.7 6.3 6.4 6.0 6.9 6.7 6.9 5.8 6.8
## [145] 6.7 6.7 6.3 6.5 6.2 5.9 5.1 4.9 4.7 4.6 5.0 5.4 4.6 5.0 4.4 4.9 5.4 4.8
## [163] 4.8 4.3 5.8 5.7 5.4 5.1 5.7 5.1 5.4 5.1 4.6 5.1 4.8 5.0 5.0 5.2 5.2 4.7
## [181] 4.8 5.4 5.2 5.5 4.9 5.0 5.5 4.9 4.4 5.1 5.0 4.5 4.4 5.0 5.1 4.8 5.1 4.6
## [199] 5.3 5.0 7.0 6.4 6.9 5.5 6.5 5.7 6.3 4.9 6.6 5.2 5.0 5.9 6.0 6.1 5.6 6.7
## [217] 5.6 5.8 6.2 5.6 5.9 6.1 6.3 6.1 6.4 6.6 6.8 6.7 6.0 5.7 5.5 5.5 5.8 6.0
## [235] 5.4 6.0 6.7 6.3 5.6 5.5 5.5 6.1 5.8 5.0 5.6 5.7 5.7 6.2 5.1 5.7 6.3 5.8
## [253] 7.1 6.3 6.5 7.6 4.9 7.3 6.7 7.2 6.5 6.4 6.8 5.7 5.8 6.4 6.5 7.7 7.7 6.0
## [271] 6.9 5.6 7.7 6.3 6.7 7.2 6.2 6.1 6.4 7.2 7.4 7.9 6.4 6.3 6.1 7.7 6.3 6.4
## [289] 6.0 6.9 6.7 6.9 5.8 6.8 6.7 6.7 6.3 6.5 6.2 5.9
{% endhighlight %}

cbind() allows us to bind together columns.


{% highlight r %}
# First we look at the dimension of "iris"
dim(iris)
{% endhighlight %}



{% highlight text %}
## [1] 150   5
{% endhighlight %}



{% highlight r %}
# Using cbind() to put together two copies of iris causing double columns
cbind(iris, iris) -> iris.c
dim(iris.c)
{% endhighlight %}



{% highlight text %}
## [1] 150  10
{% endhighlight %}



{% highlight r %}
iris.c[1,]
{% endhighlight %}



{% highlight text %}
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species Sepal.Length
## 1          5.1         3.5          1.4         0.2  setosa          5.1
##   Sepal.Width Petal.Length Petal.Width Species
## 1         3.5          1.4         0.2  setosa
{% endhighlight %}

Both rbind and cbind will work, if you try to combine vectors of different lengths. In this case it will recycle the shorted vector
until it matches the length of the longer vector. You will get a warning in this situation. 

Using merge(), we can merge objects together assigning what we bind by using "by =". For example, we can bind using the rownames of our objects using "by = row.names", we can merge by a specific column present in both objects (e.g. by = "Name"), or different columns in each object (by.x = "Species", by.y = "Name").


{% highlight r %}
# First we look at the dimension of "iris"
dim(iris)
{% endhighlight %}



{% highlight text %}
## [1] 150   5
{% endhighlight %}



{% highlight r %}
# Merging iris by row names
merge(iris, iris, by = "row.names") -> iris.double
dim(iris.double)
{% endhighlight %}



{% highlight text %}
## [1] 150  11
{% endhighlight %}



{% highlight r %}
iris.double[1, ]
{% endhighlight %}



{% highlight text %}
##   Row.names Sepal.Length.x Sepal.Width.x Petal.Length.x Petal.Width.x Species.x
## 1         1            5.1           3.5            1.4           0.2    setosa
##   Sepal.Length.y Sepal.Width.y Petal.Length.y Petal.Width.y Species.y
## 1            5.1           3.5            1.4           0.2    setosa
{% endhighlight %}

## Activity 

Create two objects, one containing numbers 1-10, one containing numbers 11-20

* Bind them together to make an object of two rows, row 1 being 1:10, row 2 being 11-20
* Bind them together to make an object of two columns, columns 1 being 11-20, column 2 being 1-10


# Paste

The function ```paste()``` is a way to concatenating together vectors. It can be applied to a characters or numbers, 
vector and column(s) of a data frame or matrix. You can define what you want the separator to be (sep =), or use 
```paste0()``` or ```paste()``` with the argument sep = "" for no space. You can also prodvide a string as an argument
to add the same component to a character or vector.


{% highlight r %}
# Adding text to a value in iris
paste("Species", iris$Species[1])
{% endhighlight %}



{% highlight text %}
## [1] "Species setosa"
{% endhighlight %}



{% highlight r %}
# Pasting together two columns of iris
paste(iris$Species[1:10], iris$Sepal.Length[1:10], sep = ":")
{% endhighlight %}



{% highlight text %}
##  [1] "setosa:5.1" "setosa:4.9" "setosa:4.7" "setosa:4.6" "setosa:5"  
##  [6] "setosa:5.4" "setosa:4.6" "setosa:5"   "setosa:4.4" "setosa:4.9"
{% endhighlight %}


# Renaming columns and rows 

By using rownames() and colnames(), we can look at what the rownames and colnames of an object are. We can also use this 
to replace the rownames and colnames of the object by assigning using ```<-```.


{% highlight r %}
# Renaming the colnames in iris
iris -> iris2
colnames(iris2)
{% endhighlight %}



{% highlight text %}
## [1] "Sepal.Length" "Sepal.Width"  "Petal.Length" "Petal.Width"  "Species"
{% endhighlight %}



{% highlight r %}
colnames(iris2) <- c("S.Length", "S.Width", "P.Length", "P.Width", "Type")
colnames(iris2)
{% endhighlight %}



{% highlight text %}
## [1] "S.Length" "S.Width"  "P.Length" "P.Width"  "Type"
{% endhighlight %}


# Adding and removing variables

Adding data to your objects can be very useful. Adding an extra column is very easy using the assignment operator
and giving the new column a name.


{% highlight r %}
# Adding a new column
iris -> iris2
iris2$new.column <- 1:nrow(iris2)

head(iris2)
{% endhighlight %}



{% highlight text %}
##   Sepal.Length Sepal.Width Petal.Length Petal.Width Species new.column
## 1          5.1         3.5          1.4         0.2  setosa          1
## 2          4.9         3.0          1.4         0.2  setosa          2
## 3          4.7         3.2          1.3         0.2  setosa          3
## 4          4.6         3.1          1.5         0.2  setosa          4
## 5          5.0         3.6          1.4         0.2  setosa          5
## 6          5.4         3.9          1.7         0.4  setosa          6
{% endhighlight %}

Removing a column can be done by assigning the relevant column the "NULL" value.


{% highlight r %}
# Removing a column
iris2$new.column <- NULL
{% endhighlight %}


# Generating a sequence of numbers

To generate regular sequences, we can use ```seq()```. We provide it a value to start from (from =), and where to 
end (to =) abd then a value to increase by (by =).


{% highlight r %}
# Create a sequence from 0 to 100 increasing by 5 each time
seq(from = 0, to = 100, by = 5)
{% endhighlight %}



{% highlight text %}
##  [1]   0   5  10  15  20  25  30  35  40  45  50  55  60  65  70  75  80  85  90
## [20]  95 100
{% endhighlight %}

***

## Activity

Create a copy of ```iris```

* Rename the columns of ```iris``` by prefixing with the word "flower" and the separator "_"
* In your copy, duplicate the ```Species``` column
* Add a column to your copy which contains the numbers from 4 to 600 increasing by 4 each time

