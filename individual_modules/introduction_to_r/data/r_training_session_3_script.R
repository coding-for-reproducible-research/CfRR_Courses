# SESSION 3 - Manipulating and Plotting Data

# 1. Set up----
'
Descripition: R Course Sessioon 2
Date: November 2022
Author: Rebecca G. Smith and Emma Walker 
Adapted by: Laura Roldan-Gomez
'

# Set up 

setwd("C:/Users/rgs212/OneDrive - University of Exeter/R Training/R workshop UoE")


#' Create and save a new script and name it "R training session 3".
 
# Data
data(iris)


# 1. Data exploration----

#' When we have our data loaded in, we may need to explore and manipulate it to get it into the format we require, remove sample, subset, match etc. There are several easy to use tools within R which can help us with these tasks. 
 
## **Subsetting** ----

#' Depending on the type of data you have (vector, data frame, matrix etc.), you can use tools to select parts of it using square bracket i.e. [ ]. These brackets have a lot of utility and allow us to select based on position and name. In order to know how to use them, we need to know how many dimensions the data has. If it is a vector, it has one dimension, if it is a data frame or matrix, it has two. This also informs how many arguments (separated by a comma) the brackets require for selection.
#' 

# Using a vector, we only need to give one selection and no comma
test <- 1:10
# Select the first value in the vector "test"
test[1]

# Using a matrix or data frame, we need to give two selections with a comma separating
# The number before the column is the row, the number after the comma is the column
# To select the value in the first row and second column
iris[1, 2]


#' We can also leave one of the values blank, to select all values which meet the criteria.

# By leaving the column argument empty, we will select all columns which are in the first row
iris[1, ]

# By leaving the row argument empty, we will select all rows which are in the first columns
iris[, 3]

#' We can also use square brackets to select more than one value. Using "c()" and ":", we can select more than one value. 

# Using ":" to select several values
# Below we select the values in the 5th, 6th, 7th and 8th row and the first three columns
iris[5:8, 1:3]
# Using "c()" to select several values
# Below we select the values in the 3th, 8th and 10th row and the 2nd and 4th
iris[c(3, 8, 10), c(2, 4)]

 
#' We can also use names to select rows or columns, although this is most useful using column names.

# Using "c()" to select several values
# Using column name "Sepal.Width" to select values in this column, in the first three rows
iris[1:3, "Sepal.Width"]


#' In data frames, we can use the "$" to select values in individual columns. important to note that this will not work in matrices. 

# Using "$" and the column name "Petal.Length", we can select the values in this column
iris$Petal.Length


## **Matching** ----

#' There are several circumstances we will need to check for matching and use that information. There are several ways we can do this using R depending on what we need.

#' Using identical(), we can check if values or collections of values are identical.
 
# Checking if the first and second row values in the "Species" column of iris are identical
identical(iris$Species[1], iris$Species[2])
# Checking if the first and 51st row values in the "Species" column of iris are identical
identical(iris$Species[1], iris$Species[51])

 
#' Using all.equal() is similar to identical(), but allows for some tolerance in how similar values can be. For example, we may want to check two numbers with lots of decimal places, but only need them to be within 0.01 of each other. Therefore we can give a tolerance of 0.01
 
x1 <- 1.232529
x2 <- 1.23366
all.equal(x1, x2, tolerance=0.01)
all.equal(x1, x2, tolerance=0.0001)

 
#' We can use "==" as a selector to pull all matching entries. We can give a numeric value or a character in quotations.

iris[iris$Species == "setosa", ]


#' We can use objects or parts of objects to select rows and columns within [ ] using the "%in%".   
 
select <- "versicolor"
iris[iris$Species %in% select, ]

## **Merging and binding**----
 
#' We will often need to bring multiple two-dimensional objects together. We can do this multiple ways. 

#' Using rbind() and cbind(), we can combine objects together. rbind() allows us to bind together rows.
 
# First we look at the dimension of "iris"

dim(iris)

# Using rbind() to put together two copies of  causing double rows
rbind(iris, iris) -> iris.r
dim(iris.r)
iris.r[ ,1]

 
#' cbind() allows us to bind together columns.

# First we look at the dimension of "iris"

dim(iris)

# Using cbind() to put together two copies of iris causing double columns
cbind(iris, iris) -> iris.c
dim(iris.c)
iris.c[1,]


#' Using merge(), we can merge objects together assigning what we bind by using "by =". For example, we can bind using the rownames of our objects using "by = row.names", we can merge by a specific column present in both objects (e.g. by = "Name"), or different columns in each object (by.x = "Species", by.y = "Name").
 
# First we look at the dimension of "iris"

dim(iris)

# Merging iris by row names
merge(iris, iris, by = "row.names") -> iris.double
dim(iris.double)
iris.double[1, ]

### Tasks
#' 
#' 1. Display the following from "iris"
#'     a. 14th row
#'     b. 4th column
#'     c. 120th row of 2nd column
#'     d. 4th, 6th, 10th and 12th row
#'     e. 111th, 112th and 113th row of "Species" column  
#' <p>&nbsp;</p>
#' 
#' 2. Work out if the following match
#'     a. 9th and 13th row of "Petal.Length"
#'     b. 145th and 146th row of "Sepal.Length"
#'     c. 150th row of "Sepal.Length" and 103rd row of "Petal.Length"
#'     d. 13th and 108th row of "Sepal.Width"
#'     e. 50 divided by 55 and 10 divided by 12
#'     f. 50 divided by 55 and 10 divided by 12 to a tolerance of 0.1
#' <p>&nbsp;</p>
#' 
#' 3. Create two objects, one containing numbers 1-10, one containing numbers 11-20
#'     a. Bind them together to make an object of two rows, row 1 being 1:10, row 2 being 11-20
#'     b. Bind them together to make an object of two columns, columns 1 being 11-20, column 2 being 1-10

# 5.2 Data manipulation----
 
## **Paste**----
#' 
#' The function paste() is a way to concatenating together vectors. It can be applied to a characters or numbers, vector and column(s) of a data frame or matrix. You can define what you want the separator is (sep =), or use paste0() or paste() with sep = "" for no space. You can also give text to add to a character or vector.
#' 
## ----echo=T----------------------------------------------
# Adding text to a value in iris
paste("Species", iris$Species[1])
# Pasting together two columns of iris
paste(iris$Species[1:10], iris$Sepal.Length[1:10], sep = ":")

#' 
#' ***
#' 
#' **Renaming columns and rows**
#' 
#' By using rownames() and colnames(), we can look at what the rownames and colnames of an object are. We can also use this to replace the rownames and colnames of the object by assigning using "<-".
#' 
## ----echo=T----------------------------------------------
# Renaming the colnames in iris
iris -> iris2
colnames(iris2)
colnames(iris2) <- c("S.Length", "S.Width", "P.Length", "P.Width", "Type")
colnames(iris2)

#' 
#' ***
#' 
#' **Adding and removing variables**
#' 
#' Adding data to your objects can be very useful. Adding an extra column is very easy by assigning what you want to a new column.
#' 
## ----echo=T----------------------------------------------
# Adding a new column
iris -> iris2
iris2$new.column <- 1:nrow(iris2)

#' 
#' Removing a column can be done by using the "NULL" value. on the column of interest.
#' 
## ----echo=T----------------------------------------------
# Removing a column
iris2$new.column <- NULL

#' 
#' ***
#' 
#' **seq()**
#' 
#' To generate regular sequences, we can use seq(). We provide it a value to start from (from =), and where to end (to =) abd then a value to increase by (by =).
#' 
## ----echo=T----------------------------------------------
# Create a sequence from 0 to 100 increasing by 5 each time
seq(from = 0, to = 100, by = 5)

#' 
#' ***
#' 
#' ### <a id="tasks2"></a>Tasks
#' 
#' 1. Create a copy of "iris"
#'     a. Rename the columns of "iris" by prefixing with the word "flower" and the separator "_"
#'     b. In your copy, duplicate the "Species" column
#'     c. Add a column to your copy which contains numbers between 4 and 600 increased by 4 each time
#' 
#' ***
#' 
#' ## <a id="bv"></a>5.3 Basic visualisations
#' 
#' **Types of plots**
#' 
#' R is capable of plotting many different types of plots and many are possible through simple plotting techniques. Depending on the data we are attempting to visualize, the type of plot we may want to use will vary. R will automatically try and plot the most appropriate plot for the data provided. You can also define to make box plots (boxplot()), histograms (hist()) and bar plots (barplot()).
#' 
#' There are also many arguments we can give to R for the plots we want to make.
#' 
## ----plot, include=TRUE----------------------------------
# Plotting all the iris data
plot(iris, col = c("red", "blue", "#ddaa33")[as.numeric(iris$Species)], 
     pch = c(1, 2, 3)[as.numeric(iris$Species)], cex = 0.8)

#' 
#' Box plots can be made using the boxplot() function. It uses a lot of the standard plotting functions.
#' 
## ----echo=T----------------------------------------------
plot(iris$Sepal.Length ~ iris$Species, ylab = "Sepal Length (cm)", xlab = "Species", 
     col =  c("red", "blue", "#ddaa33"))

#' 
#' Histograms are plotted using the function hist(), which allows us to plot the frequency of a vector. You can use standard plotting arguments such as col, but also used the argument breaks to adjust the amount of bins.
#' 
## ----echo=T----------------------------------------------
# Plotting "Sepal.Length" with increased bins
hist(iris$Sepal.Length, breaks = 16)

#' 
#' Below you can see a table containing a lot of basic plotting arguments. Also, for colour selection, making colour themes and looking for colour blind options, you can use https://www.colorhexa.com/ which will give you R friendly colour codes.
#' 
## ----echo=F----------------------------------------------
read.csv("plotting table.csv", header = T)->plots
knitr::kable(plots, col.names = gsub("[.]", " ", names(plots)))

#' 
#' ***
#' 
#' **Plots on plots**
#' 
#' Once you have created a plot, there are various methods which allow us to add more data on top. For example, we may want to add a individual data points on top of a box plot, or extra points to a plot. To do this we can use functions such as points(), lines() or abline().
#' 
#' Using points() and lines(), you can add more data to your plot. They use similar arguments to plot(), such as col, lty, pch, cex etc.
#' 
## ----echo=T----------------------------------------------
# Plot "Sepal.Length" on a plot, then add "Sepal.Width" data as points and "Petal.Length" as lines
plot(iris$Sepal.Length, ylim = c(0, 8), ylab = "Size (cm)", xlab = "Sample")
points(iris$Sepal.Width, col = "red", pch = 19, cex = 0.8)
lines(iris$Petal.Length, lty = 2, col = "blue")

#' 
#' using abline(), you can add horizontal lines (h=), vertical lines (v=), diagonal or correlations (x, y). It can also be wrapped around a linear regression (lm()) to add a line of best fit.
#' 
## ----echo=T----------------------------------------------
# Adding a horizontal line at 6 and a vertical line at 60
plot(iris$Sepal.Length)
abline(h = 6, col = "red")
abline(v = 60, col = "blue")
# Plotting "Sepal.Length" against "Petal.Length" and adding a line of best fit
plot(iris$Sepal.Length ~ iris$Petal.Length)
abline(lm(iris$Sepal.Length ~ iris$Petal.Length), lty = 3, col = "green", lwd = 3)

#' 
#' ***
#' 
#' **Plot additions**
#' 
#' We can make many additions to our plots. As there are so many, we will only explore the most common ones here but will list additional ones which may be useful in the future. 
#' 
#' 
#' We often need to add a legend to our plot, and can do this using legend(). The legend() function allows us to define position, either by using x, y coordinates or position such as "topleft". We also provide the text, colours and background.
#' 
## ----echo=T----------------------------------------------
# Plotting "Sepal.Length" and colouring and using different points by "Species", then adding a legend
plot(iris$Sepal.Length, col = c("red", "blue", "#ddaa33")[as.numeric(iris$Species)], 
     pch = c(1, 2, 3)[as.numeric(iris$Species)])
legend("topleft", legend = c("Setosa", "Versicolor", "Virginica"), 
       pch = c(1,2,3), col = c("red", "blue", "#ddaa33"))

#' 
#' We can add additional text to a plot by using text() or mtext() for putting text in the margin. To use text(), we provide x, y coordinates, the text to be written (labels =), size (cex =), and colour (col =) and font (font =). 
#' 
#' Using mtext() requires different arguments as it is relation to the margin side we put the text in. It requires the text (text = ), the side of the plot the text will go (side =) with 1 = bottom, 2 = left, 3 = top, 4 = right, the margin line to put the text on (line = ).
#' 
## ----echo=T----------------------------------------------
# Adding text to a plot
plot(iris$Sepal.Length)
text(20, 6, "text", cex = 0.7, col = "blue", font = 2)
mtext("text", side = 4, line = 1, col = "red")

#' 
#' There are incidences when we may want to add additional axes or move and adjust the axes of a plot. For this, we use axis(), and may add the argument to plot() to remove axes from our plot (axes = F) so we can draw them. Arguments for axis() are which side you want the axis (side =) using 1 = below, 2 = left, 3 = above and 4 = right, the point at which tick-marks are drawn (at =), what the labels are (labels =), how far from the axis the ticks should extend (line =), the position of the axis (pos =) and if tick marks should be drawn (tick =). You can also change the line width (lwd =), colour (col =) and type of line (lty =).
#' 
## ----echo=T----------------------------------------------
# Plotting "Sepal.Length" without axes and adding them with adjustment
plot(iris$Sepal.Length, axes = F, ylab="Sepal Length (cm)")
axis(1)
axis(2, pos = 50, at = 1:8, lwd = 2, col = "blue")

#' 
#' Additional functions to add to your plots are segments(), arrows(), curve(), rect(), polygon() and grid().
#' 
#' ***
#' 
#' **Margins ** 
#' 
#' Using par(), mar() and mgp() before the plot, we can adjust the margins of our plot. Using mar() allows us to adjust the margins giving the number of lines of margin, with the default being c(5, 4, 4, 2) + 0.1 relating to bottom, left, top and right respectively. 
#' 
#' Using mgp() sets the axis label locations relative to the edge of the inner plot window. The first value represents the location the axis label, the 2nd the tick-mark labels, and 3rd the tick marks. The default is c(3, 1, 0).
#' 
#' Using las() allows us to define the orientation of the tick mark labels and any other text added to a plot. The options are parallel to the axis (the default, 0), always horizontal (1), always perpendicular to the axis (2), and always vertical (3).
#' 
## ----echo=T----------------------------------------------
par(mar = c(4, 4, 2, 1), mgp = c(2, 0.5, 0), las = 1)
plot(iris$Sepal.Length, ylab="Sepal Length (cm)")

#' 
#' ***
#' 
#' **Composites **
#' 
#' There are two options for making composite plots, or plots with multiple plots as panels. These are par(mfrow/mfcol =) and layout().
#' 
#' The arguments for par(mfrow/mfcol =), allows us to define how many rows and columns to make the composite of. Using mfcol draws by columns and mfrow draws by rows.
#' 
## ----echo=T----------------------------------------------
par(mar = c(4, 4, 2, 1))
par(mfrow = c(1, 2))
plot(iris$Sepal.Length, ylab="Sepal Length (cm)")
plot(iris$Sepal.Width, ylab="Sepal Width (cm)")

#' 
#' The arguments for layout() are more complicated but allows for unequal sizes of composite sections. The matrix argument allows you to define what plots (in the order of plotting under the layout function). The following two numbers are the number of rows and columns in our composite, respectively. The byrow argument, if true, will add plots by row, if false, it will add by column.
#' 
## ----echo=T----------------------------------------------
par(mar = c(4, 4, 2, 1))
layout(matrix(c(1, 1, 2, 3), 2, 2, byrow = TRUE))
plot(iris$Sepal.Length, ylab = "Sepal Length (cm)")
plot(iris$Sepal.Width, ylab = "Sepal Width (cm)")
plot(iris$Petal.Length, ylab = "Petal Length (cm)")

#' 
#' ***
#' 
#' **Saving and exporting plot**
#' 
#' We can save our plots as various formats using the appropriate function. These include pdf (pdf()), jpeg (jpeg()), png (png()) and tiff (tiff()). These functions, with their arguments, will appear before the plot information, and will be succeeded by dev.off(). The first argument for any of these functions should be the path and file name to save the file under. You can also define the size of the image (width =, height =, units =), background colour (bg =) and resolution (res =).  
#' 
## ----message = FALSE-------------------------------------
# Saving a plot as a jpeg file
jpeg("exampleplot.jpg", width = 300, height = 300, units = "mm", bg = "white", res = 200)
plot(iris$Sepal.Length, ylab = "Sepal Length (cm)")
dev.off()

#' 
#' ***
#' 
#' ### <a id="tasks3"></a>Tasks
#' 
#' 1. Make two objects, one object containing values 1-20, and another object containing values 40-21
#'     a. Using your objects, create a plot with the object containing 1:20 on the x-axis and the object containing 40-21 on y-axis
#'     b. Change the x-axis label to "Independent Variable" and y-axis label to "Dependent Variable"
#'     c. Expand both axes to show values 1-40
#'     d. Increase the data point size, change their style and make them repeat between five colours
#'     e. Add a legend top the top right of the plot showing the five colours you have chosen and labelling them A, B, C, D, and E
#'     f. Add a horizontal line at 30, choose a colour, weight and style
#'     g. Add a vertical line at 10, choose a different colour, weight and style
#'     h. Add text saying "Cross Point" to the top right of the intersection of the two lines. Adjust the colour and size
#' <p>&nbsp;</p>
#' 
#' 2. Using "iris", create a scatter plot with "Sepal.Length" on x-axis, labelled "Sepal length (cm)", and the other three variables plotted on y-axis, with the label being "Size (cm)"
#'     a. Colour the three species differently and make the three measures different style of points 
#'     b. Add a legend to show all the groups, and make sure it doesn't cover any points
#'     c. Make sure the x-axis limits are 0-8 and y-axis limit is 4-8
#'     d. Adjust the margins to give a larger space around the edge of the plot and move the axis labels a little away from the axes
#'     e. Export the image as a pdf
#' <p>&nbsp;</p>
#' 
#' 3. Create a composite plot with the following panels using "iris". Make the plots colourful and variable, that all points are visible in plotting window, axes have labels and measurement units. Export the plot as a high resolution (200) jpeg. Make sure the points and text are readable, and all info is visible. You may need to adjust margins
#'     a. Box plot of "Petal.Length" by species coloured by species
#'     b. Histogram of "Petal.Length" with 6 breaks, each one coloured differently, with a line added for the mean (hint: mean), coloured and labelled "Mean = X" where "X" is the mean value. Make this panel take more space
#'     c. "Petal.Length" against "Petal.Width" for just "virginica" species, with a line of best fit (hint: subsetting)
#' 
#' ***
#' 
#' # <a id="next"></a>6. _Next on R Workshops_: topics covered in next workshop
#' 
#' In Session 4 - Introduction to Statistical Analysis, you will learn...
#' 
#' + Summary statistics
#' + Normal and other distributions
#' + Confidence Intervals
#' + Random Sampling
#' + Basic analysis
#'   + Correlation
#'   + T-test
#'   + ANOVA
#'   
#' ***
#' 
#' # <a id="res"></a>7. Resources
#' 
#' * [Basic R cheat sheet](https://www.datasciencecentral.com/r-and-python-cheatsheets/)
#' * [Data Carpentry Introduction to R](https://datacarpentry.org/R-ecology-lesson/01-intro-to-r.html)
#' * [Software Carpentry: Programming with R.](https://github.com/swcarpentry/r-novice-inflammation)
#' * [R for Data Science](https://r4ds.had.co.nz)
#' * [ColorHexa](https://www.colorhexa.com/)
#' * [R Base Graphics Cheatsheet](http://publish.illinois.edu/johnrgallagher/files/2015/10/BaseGraphicsCheatsheet.pdf)
#' 
#' ***
#' 
#' # <a id="ack"></a>8. Acknowledgements 
#' Inspired by and adopted from: 
#' 
#' * John Blischak, Daniel Chen, Harriet Dashnow, and Denis Haine (eds): "Software Carpentry: Programming with R."  Version 2016.06, June 2016, https://github.com/swcarpentry/r-novice-inflammation, 10.5281/zenodo.57541.
#' * Jenny Bryan: https://jennybc.github.io/purrr-tutorial 
#' * Manuel Gimond: https://mgimond.github.io/ES218/Week02a.html
#' * Damaris Zurell (Ecology & Macroecology Lab, Univ. Potsdam 2020-2022): https://damariszurell.github.io/EEC-R-prep/index.html
#' 
#' ***
#' 
#' # <a id="license"></a>9. License 
#' Licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
