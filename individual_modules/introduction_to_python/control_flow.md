# Control Flow 

## Learning Objectives

At the end of this lesson you will be able to:

- Discuss the benefits of thinking about a problem before starting to code
- Understand the basics of control flow
- Explain the basic conditional statements, such as `if`, `else`, `and`, `not`, and `or`
- Write some simple expressions using these statements

## Key points
- "Use `if condition` to start a conditional statement, `elif condition` to
   provide additional tests, and `else` to provide a default."
- "The bodies of the branches of conditional statements must be indented."
- "Use `==` to test for equality."
- "`X and Y` is only true if both `X` and `Y` are true."
- "`X or Y` is true if either `X` or `Y`, or both, are true."
- "Zero, the empty string, and the empty list are considered false;
   all other numbers, strings, and lists are considered true."
- "`True` and `False` represent truth values."

## Conditionals

We can ask Python to take different actions, depending on a condition, with an `if` statement:

~~~
num = 37
if num > 100:
    print('greater')
else:
    print('not greater')
print('done')
~~~
{: .language-python}

~~~
not greater
done
~~~
{: .output}

The second line of this code uses the keyword `if` to tell Python that we want to make a choice.
If the test that follows the `if` statement is true,
the body of the `if`
(i.e., the set of lines indented underneath it) is executed, and "greater" is printed.
If the test is false,
the body of the `else` is executed instead, and "not greater" is printed.
Only one or the other is ever executed before continuing on with program execution to print "done":

![A flowchart diagram of the if-else construct that tests if variable num is greater than 100](../fig/python-flowchart-conditional.png)

Conditional statements don't have to include an `else`.
If there isn't one,
Python simply does nothing if the test is false:

~~~
num = 53
print('before conditional...')
if num > 100:
    print(num, 'is greater than 100')
print('...after conditional')
~~~
{: .language-python}

~~~
before conditional...
...after conditional
~~~
{: .output}

We can also chain several tests together using `elif`,
which is short for "else if".
The following Python code uses `elif` to print the sign of a number.

~~~
num = -3

if num > 0:
    print(num, 'is positive')
elif num == 0:
    print(num, 'is zero')
else:
    print(num, 'is negative')
~~~
{: .language-python}

~~~
-3 is negative
~~~
{: .output}

Note that to test for equality we use a double equals sign `==`
rather than a single equals sign `=` which is used to assign values.

## Comparing in Python

> Along with the `>` and `==` operators we have already used for comparing values in our
> conditionals, there are a few more options to know about:
>
> - `>`: greater than
> - `<`: less than
> - `==`: equal to
> - `!=`: does not equal
> - `>=`: greater than or equal to
> - `<=`: less than or equal to
{: .callout}

We can also combine tests using `and` and `or`.
`and` is only true if both parts are true:

~~~
if (1 > 0) and (-1 >= 0):
    print('both parts are true')
else:
    print('at least one part is false')
~~~
{: .language-python}

~~~
at least one part is false
~~~
{: .output}

while `or` is true if at least one part is true:

~~~
if (1 < 0) or (1 >= 0):
    print('at least one test is true')
~~~
{: .language-python}

~~~
at least one test is true
~~~
{: .output}

> ## `True` and `False`
> `True` and `False` are special words in Python called `booleans`,
> which represent truth values. A statement such as `1 < 0` returns
> the value `False`, while `-1 < 0` returns the value `True`.
{: .callout}

## How Many Paths?

> Consider this code:
>
> ~~~
> if 4 > 5:
>     print('A')
> elif 4 == 5:
>     print('B')
> elif 4 < 5:
>     print('C')
> ~~~
> {: .language-python}
>
> Which of the following would be printed if you were to run this code?
> Why did you pick this answer?
>
> 1.  A
> 2.  B
> 3.  C
> 4.  B and C
>
> > ## Solution
> > C gets printed because the first two conditions, `4 > 5` and `4 == 5`, are not true,
> > but `4 < 5` is true.
> {: .solution}
{: .challenge}

## What Is Truth?

> `True` and `False` booleans are not the only values in Python that are true and false.
> In fact, *any* value can be used in an `if` or `elif`.
> After reading and running the code below,
> explain what the rule is for which values are considered true and which are considered false.
>
> ~~~
> if '':
>     print('empty string is true')
> if 'word':
>     print('word is true')
> if []:
>     print('empty list is true')
> if [1, 2, 3]:
>     print('non-empty list is true')
> if 0:
>     print('zero is true')
> if 1:
>     print('one is true')
> ~~~
> {: .language-python}
{: .challenge}

## That's Not Not What I Meant

> Sometimes it is useful to check whether some condition is not true.
> The Boolean operator `not` can do this explicitly.
> After reading and running the code below,
> write some `if` statements that use `not` to test the rule
> that you formulated in the previous challenge.
>
> ~~~
> if not '':
>     print('empty string is not true')
> if not 'word':
>     print('word is not true')
> if not not True:
>     print('not not True is true')
> ~~~
> {: .language-python}
{: .challenge}

## Close Enough

> Write some conditions that print `True` if the variable `a` is within 10% of the variable `b`
> and `False` otherwise.
> Compare your implementation with your partner's:
> do you get the same answer for all possible pairs of numbers?
>
> > ## Hint
> > There is a [built-in function `abs`][abs-function] that returns the absolute value of
> > a number:
> > ~~~
> > print(abs(-12))
> > ~~~
> > {: .language-python}
> > ~~~
> > 12
> > ~~~
> > {: .output}
> {: .solution}
>
> > ## Solution 1
> > ~~~
> > a = 5
> > b = 5.1
> >
> > if abs(a - b) <= 0.1 * abs(b):
> >     print('True')
> > else:
> >     print('False')
> > ~~~
> > {: .language-python}
> {: .solution}
>
> > ## Solution 2
> > ~~~
> > print(abs(a - b) <= 0.1 * abs(b))
> > ~~~
> > {: .language-python}
> >
> > This works because the Booleans `True` and `False`
> > have string representations which can be printed.
> {: .solution}
{: .challenge}
