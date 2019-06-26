# Notes

This document will be present a framework for how to choose if/when to use OOP in Python. This is important because the programming problems that you will work on in the future might lend themselves to be solved procedurally, but also might lend themselves to be taught with OOP techniques. Frequently, you can solve a problem with either. However, it's better to use the right tool for the job. This means knowing how to reason about what the right tool is.

With this in mind, the rest of this document is devoted to presenting some programming tactics and discussing them from a more general perspective. This may not seem like "programming". However, learning these meta skills will both allow you to solve increasingly difficult problems in the future, and solve them in decreasing amounts of time.

## Making Proper Use of OOP

Now that you've learned about objects and how they intuitively provide a way for you to model the world with code via classes, you might be thinking about all the amazing use cases for this new paradigm. An important thing to note is that not every problem is suited to being solved with OOP. But, it is easy to think that every programming problem looks like a nail when you have a hammer as big as OOP. So, how can we tell whether to use functions or classes when we're writing a solution to a programming problem?

Unfortunately, there is no cut-and-dried answer to this question. However, there are some simple ways to think about how to make this choice in addition to some tools that will make transitioning from one solution (functions or classes) to the other. In addition, you can always use a mixture of functions and classes, so know that you're not making a mutually exclusive choice.  

The most straightforward way to determine if something should be a class is to ask yourself if that class would be making use of any of the design principles of OOP - *inheritance*, *encapsulation*, and *polymorphism*. The most frequent of these that will motivate the choice to use classes is encapsulation, and as a result we'll be focusing on that. (You can read about why inheritance isn't most people's favorite [here](https://en.wikipedia.org/wiki/Composition_over_inheritance), and we'll talk a little about leveraging polymorphism during lecture and see examples of it later in the course.)

## Thinking About Encapsulation

What encapsulation comes down to revolves entirely around how a class is composed. Remember that a class can have both data (*attributes*) and functions that act on/with that data (*methods*). It is the act on/with part that is important here. While we can have classes that simply group together data by making them attributes (see below), this isn't worth putting in a class, since the same result can be achieved with a data structure such as the [named tuple](https://docs.python.org/2/library/collections.html#collections.namedtuple).

```python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
from collections import namedtuple
NTPoint = namedtuple('Point', ['x', 'y'])

my_point = Point(3, 5)
nt_point = NTPoint(3, 5)
print('From Point class: ({}, {})'.format(my_point.x, my_point.y))
print('From namedtuple: ({}, {})'.format(nt_point.x, nt_point.y))
```

So, what is it that makes classes worthwhile? Much of the power in classes comes from the encapsulation, in that **both** the attributes and methods are housed within the class. This means that, as the writer of a class, we can provide easy ways for the user of our class to interact with it via methods. This is something that can't be done with just attributes or a named tuple.

So, when we're trying to decide if we should be using a class or a function to solve our problem, good questions to ask ourselves are:

* What data would be the attributes of our class?
* What ways would we provide to act on that data (what would be the class' methods)?

If we can't answer these questions, then it's probably better to just use functions.  If we can answer these questions, then we're probably justified in going down the OOP route. I frequently start writing solutions with functions, and if I find myself writing a lot of them that are acting on the same group of data, then I'll begin to think about moving to a class.

## What if We Make the "Wrong" Choice?

There will be plenty of times when we're working on a solution and we'll decide that using a different paradigm will be better than our current one. We can always refactor! **Refactoring** is the process of changing your current code (technically) without changing it's external behavior. Note that this is only really possible if we were writing modular, well abstracted code to begin with. This typically means code that used either functions or classes. What refactoring amounts to is changing the implementation within one or more layers of our abstracted solution. At the top layer, though, nothing looks different.

Refactoring functions into classes usually just looks like making the data we are  passing between each function an attribute on the class, making the functions methods , and adding `self` in a lot of places. Going from a class to functions usually looks like the exact opposite.

Because of the general lack of difficulty in moving between a class and functions and back (unless there are a lot of dependencies that you haven't modularized), it's generally not too painful to try if we're wondering what an implementation of your solution would look like in the other paradigm. If we start making the change and unforeseen complications arise, then we can always go back to our previous solution!

### Git to the Rescue

Considering that we will at some point want to undertake a refactoring of our code, it's good to know about the existence of branches in git. It turns out that we have the option to go through this process of changing, adding and committing without effecting the current state of our code. WHAT?? How is this possible? With branches.

Branches are a git tool that allow us to maintain our git repository in more than one state, aka on more than one branch. Our main branch is called `master`, and it is generally reserved for changes that we know we want to make. We can, however, add other branches, which will not effect `master`. When we initially make our new branch, it's state will be the same as master. However, the changes we make to it won't change master. Aka, we'll be committing to the new branch, not master.

Branches are a great way to test out something without changing a bunch of working code and putting it in a state that's potentially difficult to fix. The cool part comes in when we decide that the changes that we've made on our separate branch are good. At this point we would like master to have these changes. Luckily, it's very simple to put the branches changes into master. It's done with a merge.

The one thing that can make this process go wrong is when there are commits to the same file as are being changed in the new branch as on master. At this point, git doesn't know which changes we want master to have. This results in what's known as a merge conflict. Merge conflicts aren't fun, but they are fixable.

For a great intro to the ideas of branching and merging, check out [this](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) page of the git documentation.
