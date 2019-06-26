# Instructions

Tonight we're going to be taking a look at classes, and the OOP paradigm in general. The problems in this assignment are designed to help you develop an intuition for both why we like object oriented programming **and** when we want to use it. The first part of this assignment will revolve around taking a problem that has been solved with functions (which will be given to you) and turning it into a class. The second part will have you write a class from scratch, starting from the mindset of functions. The last part will give you a problem that has been solved with a class; however, it will be a poor choice of using OOP. Here, you'll blow up the class and move the code back into a solely functional programming paradigm. Hopefully this will give you an idea of problems that still ought to be solved with functions.

# Assignment Questions

### Part 1 - Functions to Class

Imagine you are waiting tables. At the end of each night, you have to find all you're bills, and total the amount that you will be tipped; this will depend on what a client decided, or 18% if they didn't specify. You always end up spending an extra 10 minutes at the end of your shift calculating how much you made in tips, and as a result you decide to write a Python script to help automate the task.

After a little trial and error, you come up with the functions below. The `0.18` is for the standard tip your restaurant charges if none is specified.

```python
def get_tips(bills_n_tips):
    return [bill * tip for bill, tip in bills_n_tips]

def add_bill_update_tips(new_bill, bills_n_tips, tip_rate=0.18):
    bills_n_tips.append((new_bill, tip_rate))
    tip_out = sum(get_tips(bills_n_tips))
    return tip_out
```

You then test them out with the following function. Who doesn't like well tested code??

```python
def test_tip_out():
    waiter_bills_n_tips = []
    print(add_bill_update_tips(58.90, waiter_bills_n_tips, 0.15))
    print(add_bill_update_tips(31.58, waiter_bills_n_tips))
    print(add_bill_update_tips(81.44, waiter_bills_n_tips, 0.20))
    print(get_tips(waiter_bills_n_tips))
    print(len(waiter_bills_n_tips))
```

As everything appears to be working, you happily go to work and keep track of your tips. Everything works out, as expected. After all, you did your due diligence and tested your code. However, running the same function over and over (and having to make sure that you we're passing the correct things to your function while you were trying to work) quickly becomes a burden. In addition, some of your coworkers see what you were doing and want to try your code next time you work. You wonder to yourself if there is a simpler way to implement a solution to this problem, one where anyone could easily and intuitively use the program your wrote.

Luckily, you learned about classes in Python recently and realize that this is a great situation to employ them! The first thing you do is sit down and think about how you'd want to use a class in this scenario. You want a class that allows you to track and get information about the status of your tips. Here's an example usage of the class you're going to build:

```python
tot = TipOutTracker(0.18)
tot.add_bill(58.90, 0.15)
tot.add_bill(31.58)
print(tot.total_tip_out())
tot.add_bill(81.44, 0.20)
print(len(tot))
```

Here, when you get the length of your tracker, you are actually going to get the total number of bills you've served.

With this in mind, your task is to take the code from the function solution of this problem and write a class `TipOutTracker`. This class will operate in the way shown above. You should be thinking about the following as you start solving this problem:

* What are the attributes (data) that you are going to store on the class?
    * What data is being abstracted away from the user of your class?
* What are the methods (functions) that you are going to operate on the attributes with?
    * What are the ways that a user of your class will be able to interact with the data it stores?

### Part 2 - Classes from Scratch

Now that you have a little bit of practice working through a problem that takes moves functions into a class, you're going to get some practice solving a problem from scratch, using OOP.

This time you are going to create a class that allows you to keep track of a to-do list. The kinds of things that we'd want to be able to do with a to-do list (no pun intended) are:

* Add a to-do item.
* Mark a to-do item as completed and remove it.
* Have the length of the to-do list return the number of items you have to do.

As you work through this problem, a good place to start is by thinking about how you'd want to use this class. If you were to be given a `ToDoList` class, how would you want to use it? Go ahead and write up a test case where you "use" the class that you're about to write. This will help get you into the mindset of how the class will actually work.

With that in mind, you're going to want to answer the same questions that were posed before:

* What are the attributes (data) that you are going to store on the class?
* What are the methods (functions) that you are going to operate on the attributes with?

Once you have an idea about the answers to these two questions, you'll be in a great place to start writing some code!

### Part 3 - Times Not to Use Classes

One thing that should be addressed while you are learning about OOP is that the use of a class is not appropriate for solving every problem. To illustrate this point, consider the following code, and it's test in the main block.

```python
class BookWordCounter():
    def __init__(self, book_path):
        self.book_path = book_path
        self.has_counted = False
        self.num_words = 0

    def count_words(self):
        with open(self.book_path) as book:
            for line in book:
                self.num_words += len(line.split())

    def num_words_in_book(self):
        if not self.has_counted:
            self.count_words()
        return self.num_words

if __name__ == '__main__':
    flat_land_counter = BookWordCounter('misc/books/flatland.txt')
    print(flat_land_counter.num_words_in_book())
    programming_lang_counter = BookWordCounter('misc/books/programming_languages.txt')
    print(programming_lang_counter.num_words_in_book())
```

Now ask yourself:
* Is encapsulation being taken advantage of when using this class?
* Is there data that is being stored on the class as an attribute?
    * Is it changing?
* Does calling methods on the class allow me to interact with that data?
* Could this be done with a function???

Try writing a function to solve the same problem that the `BookWordCounter` class solves. Consider how you would want to use that function. Feel free to tear apart the code in `BookWordCounter` when you're making your function(s).

Once your done, consider the pros and cons of solving this problem with a class vs functions. This is an important consideration to make now that you know about the power of both paradigms.

### Extra Credit

1. What happens if the coworkers that you give your `TipOutTracker` to accidentally make two instances of the class when they are tracking their tips one night. How could you make it so you can add two `TipOutTracker` instances?

2. Add a list of completed to-do items to the `ToDoList` class. Then, write a method that moves an item from the to-do list to the completed list when you mark it completed.

3. Print all of your current to-do items in a pretty way when you pass an instance of the `ToDoList`

4. Add priority to the to-do list items, and have these priorities change the way your items are displayed.
