# Introduction to Programming

## What is a Programming Language?

## Why Are There So Many Programming Languages?

## Why Do People Choose Python?

## What's It Like to Learn to Program?


# Introduction to Python

## Three Ways to Use Python

There are three popular ways to use python:

If we would like to use Python **interactively**, there are two options.

  - `ipython`: An interactive environment where you can type short pieces of python code which immediately get executed.  This is useful for quick exploratory experiments.
  - `jupyter notebook`: An interactive environment that runs in a web-browser.  This is more permanent than using `ipython`.  Notebooks are very popular in the scientific community, as they allow embedding images and text.

If we would like to **compose a longer program**, the workflow is different.  We use a **text editor** to compose files containing python code.  The files are always named like `name_of_file.py`, and they can be **run** with the command:

```
python name_of_file.py
```

I'll show some examples in the future.

Today I'll be using `ipython`, since most of our work will be exploratory.


## Numeric Data Types

Programming languages are primarily tools for doing **computation**.  Our meaning of the word "computation" will expand over time, it definitely means something very different to an experienced programmer compared to, say, a high school student.

To begin, we will discuss how to use python as a glorified calculator (it makes a really god one, and once you know a bit of python there is really no reason to every buy an actual calculator again).

### The Two Numeric Data Types

Python knows about both integer and decimal numbers.  These are two two primary types of numeric data in python.

This is an integer:

```python
In [1]: 2
Out[1]: 2
```

That's a pretty silly action.  I entered the number `2` to python, and it spit it back to me.  Here's something a bit more interesting:

```python
In [2]: 2 + 3
Out[2]: 5
```

I'm using python interactively here.  I typed in an **expression**, and python **evaluated it** and then informed me of the resulting value.

We can also do this with decimals:

```python
In [3]: 2.0 + 3.0
Out[3]: 5.0
```

This is a different type of number to python.  Notice that when I added two *integer* numbers, the result was an integer, and when I added two *decimal* numbers the result was a decimal.

**Note:** In the context of programming decimal numbers are often called **floating point numbers**, or **floats**.  There is a technical reason this is done, but it's not important for now.

**Note:** There are some other numeric data types supported by python (complex numbers for example), but they are not worth worrying about at the moment.

### Arithmetic

There are many arithmetic operations supported by python.

```python
In [4]: 2 - 3
Out[4]: -1

In [5]: 2 * 3
Out[5]: 6

In [6]: 2 / 3
Out[6]: 0.6666666666666666
```

The two are pretty clear, but the third is a bit more interesting.  Even though we divided two *integers* we got back a *decimal*.  This is in contrast to the other two examples, where we got back the same type of numbers as we put in.

We may suspect that if the division comes out evenly, they python will give us an integer, but this is not the case:

```python
In [7]: 4/2
Out[7]: 2.0
```

### Exponentiation

There are two more arithmetic operations that are encountered more rarely.  **Exponentiation** is spelled with two stars `**`:

```python
In [8]: 2**4
Out[8]: 16

In [9]: 2**0.5
Out[9]: 1.4142135623730951
```

Exponentiation can result in some massive numbers, but python handles them just fine:

```python
In [10]: 2**100
Out[10]: 1267650600228229401496703205376

In [11]: 2**250
Out[11]: 1809251394333065553493296640760748560207343510400633813116524750123642650624

In [12]: 2**1000
Out[12]: 10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```

There's an interesting quirk to this large number thing though:

```python
In [13]: 2.0**1000
Out[13]: 1.0715086071862673e+301
```

While integers can have as many digits as needed, **decimals cannot, you only get (about) seventeen decimal digits to work with**.  So if you end up with really large decimal number, some of the digits will get truncated.  There is not much you can do about this, it's a pretty fundamental quirk of programming languages.

### Modular Division

The final arithmetic operation is called **modular division**.  This sounds gnarly, but it's actually really simple.

```python
In [15]: 10 % 2
Out[15]: 0

In [16]: 10 % 3
Out[16]: 1

In [17]: 10 % 4
Out[17]: 2

In [18]: 10 % 5
Out[18]: 0
```

The `%` operator does division, but returns the **remainder** of the division (instead of the quotient).  This is a lot more useful than you may guess if you are not an experienced programmer, it allows for the clean solution to a surprising number of problems.

### Organization

If you end up with more complex mathematical expressions, you can use parentheses to organize them:

```python
In [20]: (2 + (3/2) + (5/4)) * ((15 - 6)**2 - (14 + 2)**2) + 5
Out[20]: -826.25
```

This works just like it should: the innermost parentheses are evaluated first, and then python works outwards.

### Review:

Here's a quick summary of what we learned.

  - Python is a damn good calculator.
  - There are two types of numeric data commonly used in python: **integers** and **Decimals**.
  - Doing arithmetic on numbers generally gives back the same type of number, except for division, which always gives back a decimal!
  - To organize work, you can use parentheses.


## Giving Things Names

Our last example got a bit out of hand:

```python
In [20]: (2 + (3/2) + (5/4)) * ((15 - 6)**2 - (14 + 2)**2) + 5
Out[20]: -826.25
```

There's enough there that it's getting a bit hard to read.  Programs that are hard to read are **the worst**.  A lot of effort in programming is making sure that your code is not an impossible to understand pit of symbols.

The first line of defense for understandability is **giving things names**. Here's a reworked version of this example where I give names to the different components of the expression:

```python
In [24]: first_factor = (2 + (3/2) + (5/4))

In [25]: second_factor = ((15 - 6)**2 - (14 + 2)**2)

In [26]: first_factor * second_factor + 5
Out[26]: -826.25
```

The `=` sign is used a bit differently in python than in mathematics, it is called the **assignment operator**, and it is used to give things names.  Giving things names is one of the **most important** things to learn to do well in programming, good names are the most effective way to help you and others understand your code.

An important quirk is that **names are given to values not to expressions**.  If we ask python to tell us what is stored under the name `second_factor` we just get a number:

```python
In [27]: second_factor
Out[27]: -175
```

This is the same number we would have seen if we had just computed the value of the expression:

```python
In [28]: ((15 - 6)**2 - (14 + 2)**2)
Out[28]: -175
```

You may have expected python to report `((15 - 6)**2 - (14 + 2)**2)` when we asked it to tell us what we had named `second_factor`, but that's not how it works.  When we do:

```python
In [25]: second_factor = ((15 - 6)**2 - (14 + 2)**2)
```

python first *evaluates* the expression on the right hand side, and then gives the resulting value the name `second_factor`.  There is **no way** to give a name to an expression, only values.


### Review:

Here's a summary of what we learned:

  - To organize calculation, you can give names to values.
  - Names are only assigned to values, you cannot name expressions.


## The Logical Data Type (Booleans)

The second type of data we will study today is used to represent logical truth (or falseness).  It is called the **boolean** data type (after [George Boole](https://en.wikipedia.org/wiki/George_Boole) who wrote an influential book on logical deduction), and it has only two values: `True` and `False`.

```python
In [29]: True
Out[29]: True

In [30]: False
Out[30]: False
```

### Using Comparisons to Create Booleans

Booleans are usually created in a program by **comparisons** between values.  

There are many different types of comparisons.  The simplest is probably **equality**, the `==` operator is used to test if two values are equal:

```python
In [33]: 2.0 == 2.0
Out[33]: True

In [34]: 2.0 == 2.1
Out[34]: False
```

Note how this works, we're essentially asking a question:

> Is the value 2.0 equal to the value 2.1?

and python is giving us the answer `False`.

There are many other comparisons in python, all of the usual numeric comparisons are supported:

```python
In [34]: 2.0 == 2.1
Out[34]: False

In [35]: 2.0 <= 2.1
Out[35]: True

In [36]: 2.0 >= 2.1
Out[36]: False

In [37]: 2.0 < 2.1
Out[37]: True

In [38]: 2.0 < 2.0
Out[38]: False
```

There's also a **not equals** comparison, though it would be hard to guess how to spell it:

```python
In [39]: 2.0 != 2.0
Out[39]: False

In [40]: 2.0 != 2.1
Out[40]: True
```

#### Exercise:

How would you use these ideas to check if a number is even?  Odd?

### And, Or, and Not

To *create* booleans we can use the comparison operators `==, !=, <, <=, >`, and `>=`, to *combine* booleans we use the logical operators `and`, `or`, and `not`.

```python
In [41]: (2.0 < 3.0) and (-2.0 < -3.0)
Out[41]: False

In [42]: (2.0 > 3.0) and (-2.0 < -3.0)
Out[42]: False

In [43]: (2.0 > 3.0) and (-2.0 > -3.0)
Out[43]: False

In [44]: (2.0 < 3.0) and (-2.0 > -3.0)
Out[44]: True
```

Notice that the `and` of two booleans is only `True` when **both** the left-hand and right-hand booleans are `True`, anything else gives `False`.

The `or` operator gives a `True` result when *either* the left-hand or the right-hand boolean is `True` (or both):

```python
In [45]: (2.0 < 3.0) or (-2.0 < -3.0)
Out[45]: True

In [46]: (2.0 > 3.0) or (-2.0 < -3.0)
Out[46]: False

In [47]: (2.0 > 3.0) or (-2.0 > -3.0)
Out[47]: True

In [48]: (2.0 < 3.0) or (-2.0 > -3.0)
Out[48]: True
```

The `not` operator reverses the `True`thinness of a boolean:

```python
In [49]: 3.14159 > 2.71828
Out[49]: True

In [50]: not (3.14159 > 2.71828)
Out[50]: False

In [51]: 3.14159 < 2.71828
Out[51]: False

In [52]: not (3.14159 < 2.71828)
Out[52]: True
```

### Working with Booleans

Booleans are not so different from numerics in python, you can name them just like you can numbers.

```python
In [56]: x = 4

In [57]: y = 7

In [58]: x_is_odd = (x % 2 == 1)

In [59]: y_is_odd = (y % 2 == 1)

In [60]: x_is_odd
Out[60]: False

In [61]: y_is_odd
Out[61]: True

In [62]: x_is_odd or y_is_odd
Out[62]: True

In [63]: x_is_odd and y_is_odd
Out[63]: False
```

I always tend to use the word `is` when I name booleans, to emphasise their nature as the answer to a question.


## If Statements (Conditionals)

We now have the power to work with numbers, and ask and answer yes or no questions.  The next step is to learn how to **make decisions** based on the outcome of some question.

The fundamental construct used to choose actions based on conditions in python is the **if statement**.  It looks like this, schematically:

```python
if CONDITION:
    DO FIRST THING
    DO SECOND THING
    DO LAST THING
else:
    DO A DIFFERENT FIRST THING
    DO A DIFFERENT SECOND THING
    DO A DIFFERENT LAST THING
```

We'll spend a bit of time deconstructing this.

### If Statements: The Basics

```python
In [65]: if x % 2 == 0:
    ...:     print("x is even!")
    ...:
x is even!
```

Ok, there is a LOT of new things going on here.  Let's take them step by step.

  - The `if` statement checks if a condition is `True` or `False` and decides what action to take based on the result.
  - If the condition is `True` we run the code under the `if`.  **Note that the code we run when the condition is true is indented four spaces!**

That last point is really important, so I'm going to repeat it.

**Note that the code we run when the condition is true is indented four spaces!**.  **You must indent the code to run if the condition is true four spaces, always four spaces, and only four spaces!**.

This is important, because we may want to do *multiple* things when the condition is true:

```python
In [66]: if x % 2 == 0:
    ...:     print("x is even!")
    ...:     print("for real, I'm telling you that x is even!")
    ...:     print("why aren't you listening to me?")
    ...:
x is even!
for real, I'm telling you that x is even!
why aren't you listening to me?
```

Since `x` is equal to four:

```python
In [67]: x
Out[67]: 4
```

The expression `x % 2 == 0` evaluates to `True`:

```python
In [68]: x % 2 == 0
Out[68]: True
```

So the `if` statement decides to execute the **block** of code under the `if`.  There are three `print` statements in this block, which just spit a message back out at the user.

In case the condition in the `if` statement is *not* `True`, the block of code does *not* get executed.

```python
In [70]: if x % 2 == 0:
    ...:     print("x is even!")
    ...:     print("for real, I'm telling you that x is even!")
    ...:     print("why aren't you listening to me?")
    ...:
```

**Nothing happened!**

### If Statements: The Else Clause

Sometimes you would like to supply an alternate action in case the condition is `False`.  This can be accomplished with the `else` clause:

```python
In [71]: x = 15

In [72]: if x % 2 == 0:
    ...:     print("x is even!")
    ...:     print("for real, I'm telling you that x is even!")
    ...:     print("why aren't you listening to me?")
    ...: else:
    ...:     print("x is odd!")
    ...:     print("for real, I'm telling you that x is odd!")
    ...:     print("thanks for listening to this very important message!")
    ...:
    ...:
x is odd!
for real, I'm telling you that x is odd!
thanks for listening to this very important message!
```

Notice again, **the code inside the else block is indented four spaces, it must always be indented four spaces!**

### If Statements: Multiple Conditions

Occasionally things are more complicated, and you would like to check multiple conditions in sequence until you find one that evaluated to `True`.  The `elif` (pronounced "else if") construct solves this problem:

```python
In [73]: x = 5

In [74]: if x < 10:
    ...:     print("x is smaller than ten!")
    ...: elif x < 20:
    ...:     print("x is bigger than or equal to ten, and less than twenty!")
    ...: else:
    ...:     print("x is bigger than or equal to twenty!")
    ...:
x is smaller than ten!

In [75]: x = 15

In [76]: if x < 10:
    ...:     print("x is smaller than ten!")
    ...: elif x < 20:
    ...:     print("x is bigger than or equal to ten, and less than twenty!")
    ...: else:
    ...:     print("x is bigger than or equal to twenty!")
    ...:
x is bigger than or equal to ten, and less than twenty!

In [77]: x = 22

In [78]: if x < 10:
    ...:     print("x is smaller than ten!")
    ...: elif x < 20:
    ...:     print("x is bigger than or equal to ten, and less than twenty!")
    ...: else:
    ...:     print("x is bigger than or equal to twenty!")
    ...:
x is bigger than or equal to twenty!
```

### Review.

What have we learned?

  - If statements allow us to choose what code to run based on a condition.
  - When we have multiple conditions to test, use the `elif` (else if) construct.
  - The `while` construct will run code when none of our conditions is fulfilled.

### The First Assignment Question.

```
Write a script that takes a user inputted number and prints whether it is positive, negative or zero, with "The inputted number is (positive/negative/zero)" depending.
```

We now have enough information to solve this problem, so let's do it.

New things here:

  - Getting user input.
  - Putting our code in a file.
  - Running the code in the file.


## Repeating Actions: While Loops

Our final topic for the day is how to repeat tasks until some condition is true.

Consider using python to calculate [triangular numbers](https://en.wikipedia.org/wiki/Triangular_number):

```python
In [79]: first_triangular_number = 1

In [80]: second_triangular_number = 1 + 2

In [81]: third_triangular_number = 1 + 2 + 3

In [82]: fourth_triangular_number = 1 + 2 + 3 + 4
```

This is all well and good, but what if you were tasked with calculating the millionth triangular number.  You couldn't really type all that out in any reasonable amount of time, and even if you could, aren't computers supposed to *save* us work?

Luckily there is a way out.  Notice that the three lines of code above show a lot of repetition:

```python
In [84]: first_triangular_number = 1

In [85]: second_triangular_number = first_triangular_number + 2

In [86]: third_triangular_number = second_triangular_number + 3

In [87]: fourth_triangular_number = third_triangular_number + 4
```

This doesn't really seem like much of a simplification, but it highlights an important *pattern*:

> The n-th triangular number is equal to the previous (n-1-st one) triangular number plus n.

This pattern allows us to use a **while loop** to compute the n-th triangular number.

```python
In [88]: counter = 1

In [89]: triangular_number = 1

In [90]: n = 4

In [91]: while counter < n:
    ...:     counter = counter + 1
    ...:     triangular_number = triangular_number + counter
    ...:

In [92]: triangular_number
Out[92]: 10
```

The **while loop** repeats the indented lines of code **until the condition is true**. Let's map out what is happening in a table.

| counter | triangular_number | n | counter < n |
|---------|-------------------|---|-------------|
| 1       | 1                 | 4 | True        |
| 2       | 3                 | 4 | True        |
| 3       | 6                 | 4 | True        |
| 4       | 10                | 4 | False       |

The code inside the loop is called the *body*, it gets run every time the loop executes.  Notice though, that the values of our variables change each time we execute the code, as we have tracked in the table.  In particular:

  - The `counter` is increased by one each time.  Since we stop when `counter >= 4`, this gruarentees that the body is run exactly four times.
  - The `triangular_number` is increased by the counter each time.  So the first time through it's increased by 1, the second time its increased by 2, the third time by 3, and the final by 4.

| counter | triangular_number | n | counter < n |
|---------|-------------------|---|-------------|
| 1       | 1                 | 4 | True        |
| 2       | 1 + 2             | 4 | True        |
| 3       | 1 + 2 + 3         | 4 | True        |
| 4       | 1 + 2 + 3 + 4     | 4 | False       |
