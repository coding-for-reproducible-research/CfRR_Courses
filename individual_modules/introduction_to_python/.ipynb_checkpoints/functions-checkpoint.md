# Functions
## Learning Objectives

At the end of this lesson you will be able to:

- Identify the built-in functions that we have used previously.
- Define a function that takes parameters.
- Return a value from a function.
- Test and debug a function.
- Set default values for function parameters.
- Explain why we should divide programs into small, single-purpose functions.

## Key points

- "Define a function using `def function_name(parameter)`."
- "The body of a function must be indented."
- "Call a function using `function_name(value)`."
- "Numbers are stored as integers or floating-point numbers."
- "Variables defined within a function can only be seen and used within the body of the function."
- "Variables created outside of any function are called global variables."
- "Within a function, we can access global variables."
- "Variables created within a function override global variables if their names match."
- "Use `help(thing)` to view help for something."
- "Put docstrings in functions to provide help for that function."
- "Specify default values for parameters when defining a function using `name=value`
   in the parameter list."
- "Parameters can be passed by matching based on name, by position,
   or by omitting them (in which case the default value is used)."
- "Put code whose parameters change frequently in a function,
   then call it with different parameter values to customize its behavior."

## Why use functions?

We are starting to write some more complex code, and things could get quite complicated. When we want to repeat a programming task, or check that everything is working correctly, we should use functions.

A function is a shorthand way of allowing us to re-execute longer pieces of code. We can test and verify these smaller blocks individually, and call them whenever we want.

## Built in functions

We have already used some built-in functions: `print()`, `type()`, `range()` and so on. We have also used functions that are associated with objects, such as `.append()`, `.keys()`, `.strip()`, and more. 

Using these functions allows us to create much more concise, readable code. Imagine if we had to write all the code that goes on behind the scenes each time we wanted to use `print()`! We will do the same with our own functions.

## Defining functions

Let's start by defining a function `fahr_to_celsius` that converts temperatures
from Fahrenheit to Celsius:

~~~
def fahr_to_celsius(temp):
    return ((temp - 32) * (5/9))
~~~
{: .language-python}


The function definition opens with the keyword `def` followed by the
name of the function (`fahr_to_celsius`) and a parenthesized list of parameter names (`temp`). The
body of the function --- the
statements that are executed when it runs --- is indented below the
definition line.  The body concludes with a `return` keyword followed by the return value.

![Labeled parts of a Python function definition](../fig/python-function.svg)

When we call the function,
the values we pass to it are assigned to those variables
so that we can use them inside the function.
Inside the function,
we use a return statement to send a result
back to whoever asked for it.

Let's try running our function.

~~~
fahr_to_celsius(32)
~~~
{: .language-python}

This command should call our function, using "32" as the input and return the function value.

In fact, calling our own function is no different from calling any other function:
~~~
print('freezing point of water:', fahr_to_celsius(32), 'C')
print('boiling point of water:', fahr_to_celsius(212), 'C')
~~~
{: .language-python}

~~~
freezing point of water: 0.0 C
boiling point of water: 100.0 C
~~~
{: .output}

We've successfully called the function that we defined,
and we have access to the value that we returned.


## Composing Functions

Now that we've seen how to turn Fahrenheit into Celsius,
we can also write the function to turn Celsius into Kelvin:

~~~
def celsius_to_kelvin(temp_c):
    return temp_c + 273.15

print('freezing point of water in Kelvin:', celsius_to_kelvin(0.))
~~~
{: .language-python}

~~~
freezing point of water in Kelvin: 273.15
~~~
{: .output}

What about converting Fahrenheit to Kelvin?
We could write out the formula,
but we don't need to.
Instead,
we can compose the two functions we have already created:

~~~
def fahr_to_kelvin(temp_f):
    temp_c = fahr_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k

print('boiling point of water in Kelvin:', fahr_to_kelvin(212.0))
~~~
{: .language-python}

~~~
boiling point of water in Kelvin: 373.15
~~~
{: .output}

This is our first taste of how larger programs are built:
we define basic operations,
then combine them in ever-larger chunks to get the effect we want.
Real-life functions will usually be larger than the ones shown here --- typically half a dozen
to a few dozen lines --- but they shouldn't ever be much longer than that,
or the next person who reads it won't be able to understand what's going on.

## Variable Scope

In composing our temperature conversion functions, we created variables inside of those functions,
`temp`, `temp_c`, `temp_f`, and `temp_k`.
We refer to these variables as local variables
because they no longer exist once the function is done executing.
If we try to access their values outside of the function, we will encounter an error:
~~~
print('Again, temperature in Kelvin was:', temp_k)
~~~
{: .language-python}

~~~
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-eed2471d229b> in <module>
----> 1 print('Again, temperature in Kelvin was:', temp_k)

NameError: name 'temp_k' is not defined
~~~
{: .error}

If you want to reuse the temperature in Kelvin after you have calculated it with `fahr_to_kelvin`,
you can store the result of the function call in a variable:
~~~
temp_kelvin = fahr_to_kelvin(212.0)
print('temperature in Kelvin was:', temp_kelvin)
~~~
{: .language-python}

~~~
temperature in Kelvin was: 373.15
~~~
{: .output}

The variable `temp_kelvin`, being defined outside any function,
is said to be global.

Inside a function, one can read the value of such global variables:
~~~
def print_temperatures():
  print('temperature in Fahrenheit was:', temp_fahr)
  print('temperature in Kelvin was:', temp_kelvin)

temp_fahr = 212.0
temp_kelvin = fahr_to_kelvin(temp_fahr)

print_temperatures()
~~~
{: .language-python}

~~~
temperature in Fahrenheit was: 212.0
temperature in Kelvin was: 373.15
~~~
{: .output}

## Readable functions

Consider these two functions:

~~~
def s(p):
    a = 0
    for v in p:
        a += v
    m = a / len(p)
    d = 0
    for v in p:
        d += (v - m) * (v - m)
    return np.sqrt(d / (len(p) - 1))
~~~
{: .language-python}

and:
~~~
def std_dev(sample):
    sample_sum = 0
    for value in sample:
        sample_sum += value

    sample_mean = sample_sum / len(sample)

    sum_squared_devs = 0
    for value in sample:
        sum_squared_devs += (value - sample_mean) * (value - sample_mean)

    return np.sqrt(sum_squared_devs / (len(sample) - 1))
~~~
{: .language-python}

The functions `s` and `std_dev` are computationally equivalent (they
both calculate the sample standard deviation), but to a human reader,
they look very different. You probably found `std_dev` much easier to
read and understand than `s`.

As this example illustrates, both documentation and a programmer's
_coding style_ combine to determine how easy it is for others to read
and understand the programmer's code. Choosing meaningful variable
names and using blank spaces to break the code into logical "chunks"
are helpful techniques for producing _readable code_. This is useful
not only for sharing code with others, but also for the original
programmer. If you need to revisit code that you wrote months ago and
haven't thought about since then, you will appreciate the value of
readable code!

## Exercises

## Combining Strings
>
> "Adding" two strings produces their concatenation:
> `'a' + 'b'` is `'ab'`.
> Write a function called `fence` that takes two parameters called `original` and `wrapper`
> and returns a new string that has the wrapper character at the beginning and end of the original.
> A call to your function should look like this:
>
> ~~~
> print(fence('name', '*'))
> ~~~
> {: .language-python}
>
> ~~~
> *name*
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > def fence(original, wrapper):
> >     return wrapper + original + wrapper
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Return versus print
>
> Note that `return` and `print` are not interchangeable.
> `print` is a Python function that *prints* data to the screen.
> It enables us, *users*, see the data.
> `return` statement, on the other hand, makes data visible to the program.
> Let's have a look at the following function:
>
> ~~~
> def add(a, b):
>     print(a + b)
> ~~~
> {: .language-python}
>
> What will we see if we execute the following commands?
> ~~~
> A = add(7, 3)
> print(A)
> ~~~
> {: .language-python}
>
> > ## Solution
> > Python will first execute the function `add` with `a = 7` and `b = 3`,
> > and, therefore, print `10`. However, because function `add` does not have a
> > line that starts with `return` (no `return` "statement"), it will, by default, return
> > nothing which, in Python world, is called `None`. Therefore, `A` will be assigned to `None`
> > and the last line (`print(A)`) will print `None`. As a result, we will see:
> > ~~~
> > 10
> > None
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

## Selecting Characters From Strings
>
> If the variable `s` refers to a string,
> then `s[0]` is the string's first character
> and `s[-1]` is its last.
> Write a function called `outer`
> that returns a string made up of just the first and last characters of its input.
> A call to your function should look like this:
>
> ~~~
> print(outer('helium'))
> ~~~
> {: .language-python}
>
> ~~~
> hm
> ~~~
> {: .output}
>
> > ## Solution
> > ~~~
> > def outer(input_string):
> >     return input_string[0] + input_string[-1]
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Rescaling a list
>
> Write a function `rescale` that takes a list as input
> and returns a corresponding list of values scaled to lie in the range 0.0 to 1.0.
> > ## Hint
> > If `L` and `H` are the lowest and highest values in the original list,
> > then the replacement for a value `v` should be `(v-L) / (H-L)`.
> {: .solution}
> > ## Solution
> > ~~~
> > def rescale(input_list):
> >     list_min = min(input_list)
> >     list_max = max(input_list)
> >     
> >     output_list = []
> >     for i in input_list:
> >         scaled_i = (float(i) - list_min) / (list_max - list_min)
> >         output_list.append(scaled_i)
> >     
> >     return output_list
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Improving our function with docstrings

Now that we have written a few functions, we should add  some docstrings. A docstring is a small explanation of the expected functionality of the function, as well as descriptions of the function parameters, and any returns. There are lots of styles of docstrings. See here for the Google style.

It is good habit to write a docstring for every single function you create. Even if noone reads your code, you will forget why you wrote this function in a years time. Dont be that person with no docstrings!


> Add a Google-style docstring to your rescale function. Include the expected types of the function parameters.
>
> > ## Solution
> > ~~~
> > def rescale(input_list):
> >        """Rescales a list between 0 and 1.
> >
> >        Given an input list, this function rescales each element between 0
> >        and 1. Please only provide lists containing numeric values. 
> >
> >        Args:
> >            input_list: A list containing numeric values
> >
> >        Returns:
> >            output_list: The input list, with all elements scaled
> >        """
> > 
> >     list_min = min(input_list)
> >     list_max = max(input_list)
> >     
> >     output_list = []
> >     for i in input_list:
> >         scaled_i = (float(i) - list_min) / (list_max - list_min)
> >         output_list.append(scaled_i)
> >     
> >     return output_list
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}



## Defining Defaults
>
> Rewrite the `rescale` function so that it scales data to lie between `0.0` and `1.0` by default,
> but will allow the caller to specify lower and upper bounds if they want.
> Compare your implementation to your neighbor's:
> do the two functions always behave the same way?
>
> > ## Solution
> > ~~~
> > def rescale(input_list, low_val=50, high_val=100):
> >     list_min = min(input_list)
> >     list_max = max(input_list)
> >     
> >     output_list = []
> >     for i in input_list:
> >         intermediate_i = (float(i) - list_min) / (list_max - list_min)
> >         scaled_i = intermediate_i * (high_val - low_val) + low_val
> >         output_list.append(scaled_i)
> > 
> >     return output_list
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## Variables Inside and Outside Functions
>
> What does the following piece of code display when run --- and why?
>
> ~~~
> f = 0
> k = 0
>
> def f2k(f):
>     k = ((f - 32) * (5.0 / 9.0)) + 273.15
>     return k
>
> print(f2k(8))
> print(f2k(41))
> print(f2k(32))
>
> print(k)
> ~~~
> {: .language-python}
>
> > ## Solution
> >
> > ~~~
> > 259.81666666666666
> > 278.15
> > 273.15
> > 0
> > ~~~
> > {: .output}
> > `k` is 0 because the `k` inside the function `f2k` doesn't know
> > about the `k` defined outside the function. When the `f2k` function is called, 
> > it creates a [local variable]({{ page.root }}/reference.html#local-variable)
> > `k`. The function does not return any values 
> > and does not alter `k` outside of its local copy. 
> > Therefore the original value of `k` remains unchanged.
> > Beware that a local `k` is created because `f2k` internal statements
> > *affect* a new value to it. If `k` was only `read`, it would simply retrieve the
> > global `k` value.
> {: .solution}
{: .challenge}

## Mixing Default and Non-Default Parameters
>
> Given the following code:
>
> ~~~
> def numbers(one, two=2, three, four=4):
>     n = str(one) + str(two) + str(three) + str(four)
>     return n
>
> print(numbers(1, three=3))
> ~~~
> {: .language-python}
>
> what do you expect will be printed?  What is actually printed?
> What rule do you think Python is following?
>
> 1.  `1234`
> 2.  `one2three4`
> 3.  `1239`
> 4.  `SyntaxError`
>
> Given that, what does the following piece of code display when run?
>
> ~~~
> def func(a, b=3, c=6):
>     print('a: ', a, 'b: ', b, 'c:', c)
>
> func(-1, 2)
> ~~~
> {: .language-python}
>
> 1. `a: b: 3 c: 6`
> 2. `a: -1 b: 3 c: 6`
> 3. `a: -1 b: 2 c: 6`
> 4. `a: b: -1 c: 2`
>
> > ## Solution
> > Attempting to define the `numbers` function results in `4. SyntaxError`.
> > The defined parameters `two` and `four` are given default values. Because
> > `one` and `three` are not given default values, they are required to be
> > included as arguments when the function is called and must be placed
> > before any parameters that have default values in the function definition.
> >
> > The given call to `func` displays `a: -1 b: 2 c: 6`. -1 is assigned to
> > the first parameter `a`, 2 is assigned to the next parameter `b`, and `c` is
> > not passed a value, so it uses its default value 6.
> {: .solution}
{: .challenge}
