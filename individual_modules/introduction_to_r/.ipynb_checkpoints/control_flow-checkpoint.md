# Control Flow

R is just another programming language and here we are going to introduce some common programming paradigms that
empower you to write code efficiently and control the flow of information. 

### For Loops

Code is often focused around highly repetative tasks. 
Suppose we want to print each word in a sentence.
One way is to use six `print` statements:


{% highlight r %}
best_practice <- c("Let", "the", "computer", "do", "the", "work")
print_words <- function(sentence) {
  print(sentence[1])
  print(sentence[2])
  print(sentence[3])
  print(sentence[4])
  print(sentence[5])
  print(sentence[6])
}

print_words(best_practice)
{% endhighlight %}



{% highlight text %}
## [1] "Let"
## [1] "the"
## [1] "computer"
## [1] "do"
## [1] "the"
## [1] "work"
{% endhighlight %}

but that's a bad approach for two reasons:

 1. It doesn't scale: if we want to print the elements in a vector that's hundreds long, we'd be better off just typing them in.

 2. It's fragile: if we give it a longer vector, it only prints part of the data, and if we give it a shorter input, it returns `NA` values because we're asking for elements that don't exist!


{% highlight r %}
best_practice[-6]
{% endhighlight %}



{% highlight text %}
## [1] "Let"      "the"      "computer" "do"       "the"
{% endhighlight %}



{% highlight r %}
print_words(best_practice[-6])
{% endhighlight %}



{% highlight text %}
## [1] "Let"
## [1] "the"
## [1] "computer"
## [1] "do"
## [1] "the"
## [1] NA
{% endhighlight %}


<details>
	<summary> Not Available </summary>
	<pre>
		
 R has has a special variable, `NA`, for designating missing values that are
**N**ot **A**vailable in a data set. See `?NA` and (An Introduction to R)[http://cran.r-project.org/doc/manuals/r-release/R-intro.html#Missing-values]
for more details.

    </pre>
</details>



Here's a better approach:


{% highlight r %}
print_words <- function(sentence) {
  for (word in sentence) {
    print(word)
  }
}

print_words(best_practice)
{% endhighlight %}



{% highlight text %}
## [1] "Let"
## [1] "the"
## [1] "computer"
## [1] "do"
## [1] "the"
## [1] "work"
{% endhighlight %}

This is shorter---certainly shorter than something that prints every character in a hundred-letter string---and more robust as well:


{% highlight r %}
print_words(best_practice[-6])
{% endhighlight %}



{% highlight text %}
## [1] "Let"
## [1] "the"
## [1] "computer"
## [1] "do"
## [1] "the"
{% endhighlight %}

The improved version of `print_words` uses a for loop to repeat an operation---in this case, printing---once for each thing in a collection.
The general form of a loop is:


{% highlight r %}
for (variable in collection) {
  do things with variable
}
{% endhighlight %}

We can name the loop variable anything we like (with a few (restrictions)[http://cran.r-project.org/doc/manuals/R-intro.html#R-commands_003b-case-sensitivity-etc], e.g. the name of the variable cannot start with a digit).
`in` is part of the `for` syntax.
Note that the body of the loop is enclosed in curly braces `{ }`.
For a single-line loop body, as here, the braces aren't needed, but it is good practice to include them as we did.


Here's another loop that repeatedly updates a variable:


{% highlight r %}
len <- 0
vowels <- c("a", "e", "i", "o", "u")
for (v in vowels) {
  len <- len + 1
}
# Number of vowels
len
{% endhighlight %}



{% highlight text %}
## [1] 5
{% endhighlight %}

It's worth tracing the execution of this little program step by step.
Since there are five elements in the vector `vowels`, the statement inside the loop will be executed five times.
The first time around, `len` is zero (the value assigned to it on line 1) and `v` is `"a"`.
The statement adds 1 to the old value of `len`, producing 1, and updates `len` to refer to that new value.
The next time around, `v` is `"e"` and `len` is 1, so `len` is updated to be 2.
After three more updates, `len` is 5; since there is nothing left in the vector `vowels` for R to process, the loop finishes.

Note that a loop variable is just a variable that's being used to record progress in a loop.
It still exists after the loop is over, and we can re-use variables previously defined as loop variables as well:


{% highlight r %}
letter <- "z"
for (letter in c("a", "b", "c")) {
  print(letter)
}
{% endhighlight %}



{% highlight text %}
## [1] "a"
## [1] "b"
## [1] "c"
{% endhighlight %}



{% highlight r %}
# after the loop, letter is
letter
{% endhighlight %}



{% highlight text %}
## [1] "c"
{% endhighlight %}

Note also that finding the length of a vector is such a common operation that R actually has a built-in function to do it called `length`:


{% highlight r %}
length(vowels)
{% endhighlight %}



{% highlight text %}
## [1] 5
{% endhighlight %}

`length` is much faster than any R function we could write ourselves, and much easier to read than a two-line loop; it will also give us the length of many other things that we haven't met yet, so we should always use it when we can.

## Activity: 

Can you edit the for loop to print the sentance backwards?


# Control Flow

As well as repeating tasks, it's possible we want R to only perform certain tasks in certain situations.
To do this we need to write code that automatically decides between multiple options.
The tool R gives us for doing this is called a conditional statement, and looks like this:


{% highlight r %}
num <- 37
if (num > 100) {
  print("greater")
} else {
  print("not greater")
}
print("done")
{% endhighlight %}



{% highlight text %}
## [1] "not greater"
## [1] "done"
{% endhighlight %}

The second line of this code uses an `if` statement to tell R that we want to make a choice.
If the following test is true, the body of the `if` (i.e., the lines in the curly braces underneath it) are executed.
If the test is false, the body of the `else` is executed instead.
Only one or the other is ever executed:

<img src="../images/python-flowchart-conditional.svg" alt="Executing a Conditional" />

In the example above, the test `num > 100` returns the value `FALSE`, which is why the code inside the `if` block was skipped and the code inside the `else` statement was run instead.


{% highlight r %}
num > 100
{% endhighlight %}



{% highlight text %}
## [1] FALSE
{% endhighlight %}

And as you likely guessed, the opposite of `FALSE` is `TRUE`.


{% highlight r %}
num < 100
{% endhighlight %}



{% highlight text %}
## [1] TRUE
{% endhighlight %}

Conditional statements don't have to include an `else`.
If there isn't one, R simply does nothing if the test is false:


{% highlight r %}
num <- 53
if (num > 100) {
  print("num is greater than 100")
}
{% endhighlight %}

We can also chain several tests together when there are more than two options.
This makes it simple to write a function that returns the sign of a number:


{% highlight r %}
sign <- function(num) {
  if (num > 0) {
    return(1)
  } else if (num == 0) {
    return(0)
  } else {
    return(-1)
  }
}

sign(-3)
{% endhighlight %}



{% highlight text %}
## [1] -1
{% endhighlight %}



{% highlight r %}
sign(0)
{% endhighlight %}



{% highlight text %}
## [1] 0
{% endhighlight %}



{% highlight r %}
sign(2/3)
{% endhighlight %}



{% highlight text %}
## [1] 1
{% endhighlight %}

Note that when combining `else` and `if` in an `else if` statement (similar to `elif` in Python), the `if` portion still requires a direct input condition.  This is never the case for the `else` statement alone, which is only executed if all other conditions go unsatisfied.
Note that the test for equality uses two equal signs, `==`.

<details>
	<summary> Other Comparisons </summary>
	<pre>
		
 Other tests include greater than or equal to (`>=`), less than or equal to
 (`<=`), and not equal to (`!=`).

    </pre>
</details>


We can also combine tests.
An ampersand, `&`, symbolizes "and".
A vertical bar, `|`, symbolizes "or".
`&` is only true if both parts are true:


{% highlight r %}
if (1 > 0 & -1 > 0) {
    print("both parts are true")
} else {
  print("at least one part is not true")
}
{% endhighlight %}



{% highlight text %}
## [1] "at least one part is not true"
{% endhighlight %}

while `|` is true if either part is true:


{% highlight r %}
if (1 > 0 | -1 > 0) {
    print("at least one part is true")
} else {
  print("neither part is true")
}
{% endhighlight %}



{% highlight text %}
## [1] "at least one part is true"
{% endhighlight %}

In this case, "either" means "either or both", not "either one or the other but not both".

## Activity: Combining for loops and control flow

Write a for loop that iterates through numbers 1 to 10 but only prints numbers greater than 3 and less than 7.

