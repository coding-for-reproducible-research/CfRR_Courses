# Loading Data From Files




More often than not you will need to load data from a file into R that you want to analyse. We are going to use a 
dataset in the file [worms.csv]("../data/worms.csv") which you can download from the course webpage. 
This is a comma-separated values (CSV) format which means that a comma is used to indicate the end of a column.

We need to tell our computer where is the file that contains the values - if we forget this step we'll get an error message when trying to read the file. We can load the data into R using `read.csv`.

Assuming you have downloaded the file into your current working directory, you can execute the following


{% highlight r %}
read.csv(file = "worms.csv", header = TRUE)
{% endhighlight %}



{% highlight text %}
## Warning in file(file, "rt"): cannot open file 'worms.csv': No such file or
## directory
{% endhighlight %}



{% highlight text %}
## Error in file(file, "rt"): cannot open the connection
{% endhighlight %}

We have provided two arguments to this function: 
1. __file__ - the name of the file we want to read,
2. __header__ - whether the first line of the file contains names for the columns of data.

The filename needs to be a character string (or string for short), so we put it in quotes. 
The header argument needs to be a logical, we have set `TRUE` indicating that the data file does have column headers. 


Since we didn't tell it to do anything else with the function's output, the console will display the full contents of the file `worms.csv`.
Try it out.

`read.csv` reads the file, but we can't easily use data unless we assign it to a variable. Let's re-run `read.csv` and 
save the result:


{% highlight r %}
df <- read.csv(file = "worms.csv", header = TRUE)
{% endhighlight %}



Use some of the functions we have introduced earlier can be used to summarise the properties of the worms dataset

<details>
	<summary> Other Options for Reading CSV Files </summary>
	<pre>
		
 `read.csv` actually has many more arguments that you may find useful when
 importing your own data in the future. You can learn more about these
 options [here](http://swcarpentry.github.io/r-novice-inflammation/11-supp-read-write-csv/).

    </pre>
</details>



<details>
	<summary> Loading Data with Headers </summary>
	<pre>
		
 What happens if you forget to put `header = FALSE`? The default value is `header = TRUE`, which you can check 
 with `?read.csv` or `help(read.csv)`. What do you expect will happen if you leave the default value? Before you 
 run any code, think about what will happen to the first few rows of your data frame, and its overall size. Then 
 run the following code and see if your expectations agree:


    </pre>
</details>
