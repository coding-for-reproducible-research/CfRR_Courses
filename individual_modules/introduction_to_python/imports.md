# Imports
## Learning Objectives

At the end of this lesson you will be able to:

- Import some key Python modules from the Python Standard Library
- Understand how to use the functions they include
- Identify some of the main packages available on PyPi, an online repository
- Install these, and check they work

## The Python standard library

So far, we have only used a tiny portion of the Python Standard Library. This is a collection of modules that are installed when you install Python. However, the Standard Library contains many more modules that will be of use to us. Lets jump right in.

## Importing a module

We can import modules included with the standard library immediately. For example, the `math` module gives access to the underlying C library functions for floating point math. Lets import it using the `import` function.

~~~
import math
~~~
{: .language-python}

For standard library modules, you do not need to get the package from an external repository. As such, you shouldnt get an error when importing them.

Try importing a module with an incorrect name:

~~~
import thisisanincorrectmodulename
~~~
{: .language-python}
~~~
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'thisisanincorrectmodulename'
~~~
{: .output}

We might run into a few of these errors when we try to install from external repositories. But dont panic! Usually it means that something has been placed in a strange location, and cant be found.

## Using a module

Now that we have imported the `math` module, we can access the functions contained within it. This is done using the prefix `math.something`

But how do we know what is there for us to use?

The first thing to do is to check the documentation. For the `math` module, this can be found [here](https://docs.python.org/3/library/math.html).

Lets do a quick calculation with the cosine function and the `pi` constant.

~~~
math.cos(math.pi / 4)
~~~
{: .language-python}
~~~
0.70710678118654757
~~~
{: .output}

In addition to reading the documentation, you can type `math.` and then hit the tab key. This should give you a list of everything available to use.

## Exercise: generate random numbers

> Write a function that returns a list of n random integers between 0 and 100.
> n should be a function parameter, and you should use the standard library module `random`. The `random` documentation can be found [here](https://docs.python.org/3/library/random.html).
>
> > ## Solution
> > ~~~
> > import random
> > 
> > def generate_random(n):
> >     """Generates n random numbers between 0 and 100, and places them in a list."""
> >     
> >     output_list = []
> >     for i in range(0, n):
> >         rand_int = random.randrange(100)
> >         output_list.append(rand_int)
> >         
> >     return output_list
> > ~~~
> > {: .language-python}
> {: .solution}
{: .challenge}

## External Python libraries

There are some very common libraries that you will come across very soon into your Python journey. Some of these have been listed below:

* [NumPy](https://numpy.org/): Used for array computation, GPU processing, and generally running things really, really fast.
* [SciPy](https://scipy.org/): Contains many more complex algorithms, for optimisation, geometry, algebra, statistics, and much more.
* [Pandas](https://pandas.pydata.org/): Table-like data structures, and vectorised table operations. Think Excel for millions of rows.
* [Matplotlib](https://matplotlib.org/): Plotting library for Python.

We will use the following syntax for each of these libraries. This is unfortunately just convention!

* `import numpy as np`. Access functions using `np.XXX`.
* `import scipy`. Access functions using `scipy.XXX`.
* `import pandas as pd`. Access functions as `pd.XXX`.
* `import matplotlib.pyplot as plt`. Access functions as `plt.XXX`.

## Installing these manually

We have asked you to install Anaconda because it contains many packages commonly used for data science and visualisation, including those above. If you have problems importing these (receive error messages when trying to import them), we will do our best to help you out here. However, this troubleshooting will involve reading error messages: please be patient with us!

If you want to install these packages manually, we can use various installers.

The most common is `pip`. For example, to install `numpy` using `pip`, we type in the shell/terminal/command prompt:

~~~
pip install numpy
~~~
{: .language-shell}

If we have installed Anaconda, this contains an installer as well. We can use the following. Note that `numpy` is included with `conda`.

~~~
conda install numpy
~~~
{: .language-shell}

## Virtual environments

**Note**: This is an intermediate/advanced topic, and something that even proficient Python developers struggle with.

By default, the shell commands above will install packages into the base Python environment on your machine. In the future (beyond the scope of Intro to Python), we will try to create a "clean room" for each project that we create where we can install things that we need. This clean room is called a virtual environment. This helps us to minimise conflicts between different packages, and keep in control of things like our Python and package versions.

Virtual environment management in Python could easily take two sessions to go through, and takes a while to get the hang of. At this stage, you should be aware that:

- Virtual environments exist, and should be used per project, to keep project dependencies separate.
- They allow you to keep your base Python environment clean.
- They can be managed with tools such as Anaconda, Poetry, Virtualenv, Pipenv, and others.
- For more information, please start [here](https://docs.python.org/3/tutorial/venv.html).
