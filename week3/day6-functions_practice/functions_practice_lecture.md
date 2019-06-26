## Getting Our Hands Dirty with Functions

### Top-Down Programming

Up until now we've only written one-off functions (ones that operate independently of one another). A great use for functions is building them so that they work together.  We can write functions to solve small pieces of a larger problem. This programming strategy is known as **top-down**. The idea behind the top-down approach to programming is to start out at the definition of the problem, and break it out into smaller problems. We then distribute these smaller problems to functions. Each function we write may rely on other functions. As you go to subsequently deeper layers of your program, the functions will perform increasingly specific tasks.  At the lowest level, there is a specific problem that a single function can perform (often called a base task).

One difficulty with this approach is that it requires full vision about how a problem should be broken down before you get into the nitty-gritty implementation of any base tasks. This is a problem that is often discussed during software design. For most of the problems that we will solve, we can take an iterative approach to implementing top-down.

The top-down approach involves writing code to solve the first part of the problem. Once the code becomes its own independent piece, we put it into a function. We begin writing more code that will become its own function. With practice, this approach to solving problems will become more natural. We will illustrate this approach today. Along the way, we will learn about a few more Python tools, be able to see how the solution to a problem can evolve over time, and see how functions in action are such a powerful tool (both in taking advantage of employing a DRY methodology and seeing the power of abstraction).

### Let's Do Python

Consider the following problem:

Your boss comes to you and asks you to write a function, call it `create_report`, that takes the path for a text file and tells you the number of sentences, words, and characters in that file.

#### Starting Slow

There are obvious use cases for the function; therefore, we will want to bundle up the function in a reusable form. Let's start off by opening a new Python script file, `txt_file_processing.py`. Throughout the rest of this lecture, we will update the code in this `.md` file. The final version of this script will be in the `misc` folder. It is important to understand the way that our solution evolves in the iterative manner discussed above. What's the first thing that we put in `txt_file_processing.py`? The function that we want to write! In order for the code to run and not throw us any errors, we'll use a `pass` whenever we set up a skeleton for a function that isn't actually implemented yet (i.e. we haven't fully written). Our script begins in the following way:

```python
def create_report():
    pass
```

For the next step, consider our first input. We were told that `create_report()` should take the path to a text file.

```python
def create_report(file_path):
    pass
```

Now, how are we going to get at the contents in the text file located at `file_path`? There's actually a Python function for exactly this problem (you'll come to learn that many, many things you want to do in Python are available to you via built-in functions). Here we want to use the appropriately named `open()` function with a `with` statement.

```python
def create_report(file_path):
    with open(file_path) as txt_file:
        pass
```

Let's talk about what this line does. The `open()` (docs [here](https://docs.python.org/3/library/functions.html#open)), takes a file path and returns a "file object" which we are storing in the variable `txt_file`. Notice that we're in an indented block for the body of the `with` - when we end that block, the file will automatically be closed for us.  For this reason, this is considered the Pythonic way to handle files.

At this point, we now have access to the contents of the file via the variable `txt_file` within the scope of the `with` block.  Let's now consider next steps. Step one is reading the documentation for [file objects](https://docs.python.org/3/library/stdtypes.html#bltin-file-objects). Developing the ability to read and interpret the documentation is an important part of any role as a programmer. Next, we might create a small example that allows us to test our function.  This will use a test file, which is a great thing to have in general so that we can verify whether the code we are writing is working as we move through solving the problem.

Check out the included `test_text.txt` file, also located in the `misc` folder, which is filled with a small amount of text. We can use it to test out some of the code we've written inside of IPython. Frequently, we will use `print()` to understand pieces of our code.  In other situations, it's necessary to inspect objects using `type()`, or by calling other functions. Let's take a closer look at the file object obtained using the `with` statement.

```python
In [1]: with open('test_text.txt') as txt_file:
   ...:     print(txt_file)
   ...:     
<_io.TextIOWrapper name='test_text.txt' mode='r' encoding='UTF-8'>
```

The print statement did not return what we might have expected.  Taking a look at the documentation linked above for file objects, we see an example where we use a `for` loop to see the lines in our file.

```python
In [2]: with open('test_text.txt') as txt_file:
   ...:     for line in txt_file:
   ...:         print(line)
   ...:         
This is a test

text file.

The quick red fox

jumped over the

lazy brown dog.
```

Awesome! We now know how to access the contents of a text file! Let's add this new-found information to our script.

```python
def create_report(file_path):
    with open(file_path) as txt_file:
        for line in txt_file:
            pass
```

#### Let's Put the FUN in Functions!

Now, we need to take these lines and get the number of sentences, words, and characters contained within each. At this point, we should realize that we need to aggregate these counts. One way would be to have each count stored in its own variable, but here we're going to do it with a dictionary (we'll see why this is a good idea very soon). Let's initialize one now.

```python
def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            pass
```

Now that we have a place to store the counts that we come across while looping through our lines, we can start writing the body of our loop. Here's a place where our workflow may diverge.

Option 1: We may choose to write code inside the body of our loop and later figure out how to convert to a function.

Option 2: We may recognize that what we're about to do in the loop is its own distinct task and begin writing a function.

Let's illustrate the latter option, since we've seen plenty of examples of turning existing code into a function.
Understand the 'bigger picture' for this example - we're updating our counts with the information from the current line.

Let's start a function with an appropriate name.  Our function will need a `line` and `counts_dict` passed as arguments. The first argument, `line`, is necessary because the line we're analyzing changes in each iteration of the loop; the second argument, `counts_dict`, is necessary because it will keep track of the counts as we iterate through each line.  If we did not use a dictionary, we would need to pass three arguments to store the counts in three separate variables. Using a dictionary allows us to pass a single argument to keep track of all three counts.  We can initialize our function, and provide it within our for loop as shown below:

```python
def update_counts(line, counts_dict):
    pass


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
```

**Note**: While the names of the variables that we're passing to `update_counts()` are the same as the names of the parameters we defined in the function definition, this is not necessary. There are occasions where it is useful so that it's easier to follow the flow of variables being passed between functions.  In other cases, parameter names need to be more general because the function is performing a more general task.

Now we need to define what `update_counts()` will do with each line. We need to count the number of words and the number of characters in each line. As for the number of sentences, this is a fairly difficult problem. One way that we might hack together a solution is by counting the number of periods, `.`.  We are then assuming each sentence will end in a period. Admittedly, this is a fairly naive way to solve the problem; sentences may end with other punctuation (ellipses, exclamation points, question marks, etc.).

For now, we will neglect these obvious defects in our solution - we can always go back later to provide a more robust solution. This type of practice is very regular when solving programming problems. As we've discussed, solutions are often built up in an iterative, testing as you go, manner. In addition, there may be other edge cases that we haven't considered. That's part of the beauty of using functions. Since functions abstract away the implementation of counting sentences, words, and characters, we can later go back and change this single piece of our solution.

Let's set up a small test case so that we can verify the functionality of `update_counts()`. Consider the string `'This is a test string. Only for testing'`. We can see that it has 1 well defined sentence, 8 words, and 39 characters (counting spaces). Let's set up a counts dictionary and test this string in an IPython environment.

```python
In [1]: test_string = 'This is a test string. Only for testing'

In [2]: counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
```

We can obtain the number of characters in this string using the `len()` function.

```python
In [3]: len(test_string)
Out[3]: 39

In [4]: counts_dict['characters'] += len(test_string)
```

As for counting the words, we can call `len()` on the results of the `split()` method, which will separate our string into individual words.

```python
In [5]: test_string.split()
Out[5]: ['This', 'is', 'a', 'test', 'string.', 'Only', 'for', 'testing']

In [6]: len(_)
Out[6]: 8

In [7]: counts_dict['words'] += len(test_string.split())
```

**Note**: The underscore, `_`, can be used in IPython to access the most recent output.

As for finding the number of periods within our string, there happens to be a very useful string method called `count()`.

```python
In [8]: test_string.count('.')
Out[8]: 1

In [9]: counts_dict['sentences'] += test_string.count('.')

In [10]: counts_dict
Out[10]: {'characters': 39, 'sentences': 1, 'words': 8}
```

Now that we have verified our results,  let's implement what we've found in `update_counts()`. The major difference here is that we are considering each line of the file, rather than the entire file at once.

```python
def update_counts(line, counts_dict):
    counts_dict['sentences'] += line.count('.')
    counts_dict['words'] += len(line.split())
    counts_dict['characters'] += len(line)


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict
```

**Note**: We don't need to return anything from `update_counts()` because it is directly altering the state of `counts_dict`.

One way that we could see if our function is working correctly is by adding some code to our script that calls the function as shown below.

```python
def update_counts(line, counts_dict):
    counts_dict['sentences'] += line.count('.')
    counts_dict['words'] += len(line.split())
    counts_dict['characters'] += len(line)


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict


print(create_report('test_text.txt'))
```

If we then run our script, we can see how or function is working.

```python

In [1]: run txt_file_processing.py
{'words': 16, 'sentences': 2, 'characters': 76}
```

#### Importing Detour

While testing like this works, it turns out that this method is generally considered bad practice. The reason has to do with what happens when we do something called **importing**. The `import` statement allows us to access code (generally functions and classes) from existing scripts. Some scripts have to be written by the creators of Python.  We can then access these scripts as libraries included with Python distributions. We can also create our own scripts and then access them in the same way we would access the libraries written by the creators. Let's see what happens when we try to import the script we've just saved.

```python
In [1]: import txt_file_processing
{'words': 16, 'sentences': 2, 'characters': 76}

In [2]: txt_file_processing.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}
```

We can see importing in action here. First, focus your attention on the first line. When we import a script, Python runs the code that is contained in the imported script. While this is a very useful concept to understand, we can see a  potential downfall in this example. The `print` function that we included in our `txt_file_processing` script was run when the import happened. In general we want to import to gain access to code from other libraries/scripts, but we do not want output upon importing.

Luckily, we have a way to avoid this unwanted output, and it's known as a **main-block**. Any code that is defined within a main-block will only be executed when the script is run, as opposed to when it is imported. We can see a main-block defined below.

```python
def update_counts(line, counts_dict):
    counts_dict['sentences'] += line.count('.')
    counts_dict['words'] += len(line.split())
    counts_dict['characters'] += len(line)


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict


if __name__ == '__main__':
    print(create_report('test_text.txt'))
```

Now, if we import the script we will see that the main-block is not run. However, we still have access to the library contents. Magic!

```python
In [1]: import txt_file_processing

In [2]: txt_file_processing.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}
```

Consider the second line here (it's the same as above). Via importing, we gained access to `create_report()`, as it is stored in the `txt_file_processing.py` script. We may choose to import a library or access the contents of a library in a number of different ways.  Let's look at a few of the most common ways:

```python
In [1]: import txt_file_processing as tfp

In [2]: tfp.create_report('test_text.txt')
Out[2]: {'characters': 76, 'sentences': 2, 'words': 16}

In [3]: from txt_file_processing import create_report

In [4]: create_report('test_text.txt')
Out[4]: {'characters': 76, 'sentences': 2, 'words': 16}

In [5]: from txt_file_processing import create_report as cr

In [6]: cr('test_text.txt')
Out[6]: {'characters': 76, 'sentences': 2, 'words': 16}
```

In Python, you will see examples of importing all the time. For now, know that you can and often want to import from within a script to get access to functions from other scripts/libraries to use the code they contain. This way we don't have to re-invent the wheel each time we go to solve a programming problem.

#### Abstraction Illustration

We've now verified the accuracy of our solution, and so you use `create_report()` to help your boss. He uses your solution on a couple of text files and is pleased with the results. Happy, you take the rest of the day off of work. The next day you come into work, and you have an email in your inbox from your boss. It says that they tried to use `create_report()` overnight on a bunch of files, and it took way too long - it was still running when they came back in the morning. You are told to make `create_report()` run faster.

Alright, I guess we didn't think about speed too much (if at all) while we were writing `create_report()`. So, what are we going to do to make it faster? Well, it might not be obvious at first, so let's walk though the code.

Notice our steps in `update_counts`:

1. We count the number of periods in `line` and add that to the 'sentence' entry in `counts_dict`.

2. We take `line`, split it apart on spaces, and add the number of words that come out to the 'words' entry of `counts_dict`.

3. We count the number of characters in `line` with `len()` and add that to the 'characters' entry of `counts_dict`.

How can we make our code run faster? Notice this approach is actually going over the contents of `line` 3 separate times to perform our updates. This is very inefficient.

How can we make all of the necessary updates in fewer passes? We can write a loop to go over the line, character by character, and perform updates to the `sentences`, `words`, and `characters` entries of `counts_dict` within a single loop. Our assumptions being that a space follows the completion of a word and a period completes a sentence. We have no changes necessary to the `characters`. Let's see how this works in IPython.

```python
In [1]: test_string = 'This is a test string. Only for testing'

In [2]: counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}

In [3]: for char in test_string:
   ...:     counts_dict['characters'] += 1
   ...:     if char == '.':
   ...:         counts_dict['sentences'] += 1
   ...:     elif char == ' ':
   ...:         counts_dict['words'] += 1
   ...:

In [4]: counts_dict
Out[4]: {'characters': 39, 'sentences': 1, 'words': 7}
```

This looks like it worked...wait! Does that say we only got 7 words? We know that we're supposed to have 8 words. What happened? Fixing these problems, either when our programs don't work and we're trying to make them functional, or ones that work but aren't giving us the expected output, is a process called **debugging**. Debugging can be very time consuming and frustrating. Often we have a small error that is causing the problem. I find one good approach to debugging is isolating the problem. We then step through the logic step-by-step. It is necessary to consider the state of your program at each stage of execution, and then verify that each state provides the expected value. Let's consider this approach to debug our current problem.

| Character  | sentences |  words  | characters |
| ---------- |:---------:|:-------:|:----------:|
| T          |  0        |    0    |     1      |
| h          |  0        |    0    |     2      |
| i          |  0        |    0    |     3      |
| s          |  0        |    0    |     4      |
|            |  0        |    1    |     5      |
| i          |  0        |    1    |     6      |
| s          |  0        |    1    |     7      |
|            |  0        |    2    |     8      |
| a          |  0        |    2    |     9      |
| ...        |  ...      |    ...  |     ...    |
| n          |  0        |    4    |     20     |
| g          |  0        |    4    |     21     |
| .          |  1        |    4    |     22     |
|            |  1        |    5    |     23     |
| O          |  1        |    5    |     24     |
| n          |  1        |    5    |     25     |
| ...        |  ...      |    ...  |     ...    |
| t          |  1        |    7    |     36     |
| i          |  1        |    7    |     37     |
| n          |  1        |    7    |     38     |
| g          |  1        |    7    |     39     |

Alright, that was straightforward, and we can now see the problem. We don't see a space after the last word in a line, so our algorithm doesn't add another word!! Alright, a simple solution to this is to add one to our word count after our loop. While it's fair to say that this solution fails in the case that the last character of a line is a space, we're going to ignore that edge case for now.  

```python
def update_counts(line, counts_dict):
    for char in line:
        counts_dict['characters'] += 1
        if char == '.':
            counts_dict['sentences'] += 1
        elif char == ' ':
            counts_dict['words'] += 1
    counts_dict['words'] += 1


def create_report(file_path):
    counts_dict = {'sentences': 0, 'words': 0, 'characters': 0}
    with open(file_path) as txt_file:
        for line in txt_file:
            update_counts(line, counts_dict)
    return counts_dict


if __name__ == '__main__':
    print(create_report('test_text.txt'))
```

```python
In [1]: run txt_file_processing.py
{'words': 16, 'characters': 76, 'sentences': 2}
```

Success!!!

The above is a very realistic approach to problem solving as a programmer.

I want to quickly draw your attention to how easy it was to speed up our program by changing the implementation of `update_counts()`. This is abstraction in action! Since we've wrapped up the functionality of our program in the `create_report()` function, extending our function to create a report for a list of file paths is easily extendable! We'd just make a new function that would loop through the list of file paths and call `create_report()`, passing the current file path in that iteration of the loop as the argument.

This example has demonstrated a good workflow to follow when designing programs, and you've learned how to think about problems in an iterative top-down framework.
