# Notes

There are no iPython notebooks for you to work through before the next class. The reason for this is that the next lecture will not be covering new programming ideas, per se. It will be presenting a framework for problem solving in Python. This is important because the programming problems that you will work on in the future will not have small, one-off functions as solutions. It's much more likely that they will be problems that require a lot of code. However, if you have the right tools and mindset, all problems can be solved with very similar tactics.

With this in mind, the rest of the document is devoted to presenting some programming tactics and discussing them in a general framework. This may not seem like "programming"; however, learning these meta skills will both allow you to solve increasingly difficult problems and solve them in decreasing amounts of time.

## Pieces of a Programming Solution

The aforementioned programming tactics take root in a very simple and natural idea, and break down the problem into smaller pieces. One of the most common, and best ways, that programming is described is as follows: programming is the art of taking a seemingly unsolvable problem and turning it into a series of solvable ones.

With this in mind, you've already been presented one of the key ideas that we will leverage when trying to break our problems up - **abstraction**. Abstraction allows us to break up our larger problem into a number of smaller subproblems, and have each of those subproblems is solved separately from the other ones. By *abstracting* away parts of a programming solution, we can naturally break up a problem into pieces (functions) that perform their own separate part of the overall solution.

This view of leveraging abstraction naturally begs the question of where one begins solving the problem?

## Problem Solving Strategy

The strategy that we are going to teach you for solving larger scale programming problems is called **top-down**. Top-down design is a strategy for iteratively breaking up your problems. It is particularly powerful because it leverages abstraction in a clever way.

The idea is that when breaking up a problem, you can directly do it in code by calling functions that don't yet exist. This uses abstraction because we can think about what we'd want to pass to those functions, and what we'd want them to return, without them needing to exist yet. This gives us a very tangible way to begin coding; simply take what you have, and imagine you had a function that accepts that as input and gives what you want as output. Take a look at [this](http://bactra.org/weblog/950.html) description of top-down if you want to read it in different words.

Once we call this imaginary function in an abstract way, we need to solidify how it works. So, we go and write a function definition and think about the first thing that you'd need to do for the function to work. Once we've thought about this, we can call our not yet implemented function to do this task, thinking about what we'd pass to it and what it would return. Then, we take the "output" of that function and use as input to another, not yet implemented, function. And so on.

Here's where the top-down name starts making sense. We now get to go implement those functions we called. Within them we will need to break up that function's particular piece of the problem. As a result, we may call not yet implemented functions, and the process will repeat itself. Eventually, a function that we're trying to implement will be easy to solve, and we won't need to call any functions that don't exist yet. In general, we try to keep the length of functions less than 10 lines, but this isn't a hard and fast rule.

Lets take a look at what some code at this level might look like. Say we time trying to write a program to load some data, and then transform it and save it. How would the first set of functions look? Maybe something as simple as:

```python
data = load_data()
transformed_data = transform_data(data)
save_data(data)
```

Now, we haven't yet implemented `load_data()`, `transform_data()` or `save_data()`. But, now we have three smaller problems. We can go and start writing a solution to each of them separately. E.g. the `load_data()` function may need to prompt the user for a location to load the data from, then check that that location is valid, then "load" it.

```python
def load_data():
    data_location = get_data_location()
    good_data = check_good_location(data_location) # Here we imagine that a Bool is returned
    if good_data:
        get_data(data_location)
    else:
        print("File location not found.")
```

One step at a time we can solve this problem, from the top down.

### Naming Detour

There is one thing worth noting at this step. See how the code in `load_data()` almost reads like English? This happened because of two reasons. First, functions that do abstract tasks were used to abstract away complicated ideas. Second, good names were given to those functions so that the task they accomplish is very clear.

We should always strive to have readable code. Part of this originates in giving variables meaningful names. But, part of it also lies in using functions to split up and abstract away parts of our solution, and then giving a name to the function that accurately captures what task it performs.

## Iterative Top-Down

Sometimes we won't know how many steps will be involved in implementing a particular function. How are we to use the top-down strategy in these situations?? It turns out that immediately breaking up a function into smaller pieces isn't always feasible or sensible. There's nothing wrong with just writing some code that doesn't call imaginary functions when you start to implement a function. If you end up with a solution quickly, then all the better!

If we don't find ourself at a solution quickly, though, we'll end up writing a bunch of lines of code. This isn't a bad thing. It just means that we should take a step back and try to figure out what it is that that chunk of code is trying to accomplish. Once we put your finger on that idea, we should make a function with a name that describes that task and put the code we've written into it. Now we can call that function from the previous one we were working on and top-down continues.

The great thing about this more iterative, ad-hoc top-down approach is that we may not have had any idea what that function we just described was going to do before we tried to write it. If we were strict in enforcing a top-down strategy, we wouldn't have the luxury of just writing some code to figure it out. We should never feel confined by any strategy we use; they should be tools to help us program better, not impediments that hold us back.

## Further Readings

Here are a couple of wikipedia articles about the ideas that we've discussed so far. They might be a little more technical than we've found here. In addition, they might talk about/link to other ideas. Feel free to read about other strategies and view points surrounding coding techniques; the more you know, the better equipped you'll be in the future to tackle problems. The top-down link is actually an article about both top-down and bottom-up design. While we embrace the top-down strategy, it's worth knowing that it's not the only one out there!

* [Abstraction Principle](https://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming))
* [Abstraction](https://en.wikipedia.org/wiki/Abstraction_(computer_science))
* [Top-Down Design](https://en.wikipedia.org/wiki/Top-down_and_bottom-up_design)
