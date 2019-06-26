# Strings and Lists

Last week, we learned about how to use Python's power with `while` loops and conditionals, operating on some simple built in numeric types. Today, we are going to learn about a couple of data structures that will continue to build up your power in Python, and we'll learn about a new type of loop.

### Strings

First, we are going to learn about another common data type, strings. From a high-level perspective, a string is just a bit of text. This could be text that you have read in from a file, html that you have pulled from the Internet, or any other text. From Python's perspective, a string (type `str`) is simply a collection of encoded characters. Wait, what's an encoding...?

An encoding is just a fancy way of us saying that the characters in our string follow a certain format, or structure. The reason it matters for us in terms of our Python programs, though, is that Python expects our strings to be in one of a couple of different encodings (either `ASCII`, `utf-8`, or `unicode`). This isn't something you will run into often, and especially not when defining your own strings (it's probably most prevalent when pulling text from the Internet). However, it's worth noting because there is a good chance that sometime in your Python career, you will end up with Python telling you it doesn't recognize a certain character in one of your strings, and an unexpected encoding will most likely be at the heart of that error.

In Python, strings are recognized as a collection of characters surrounded by a set of either single quotation marks (`'...'`) or double quotation marks (`"..."`). So long as you open and close your string with a **matching** set of single or double quotation marks, you are free to use either. The single caveat to that is that if you are writing an expression with a single quotation mark in it (such as "Don't do that"), you will **have to** use a matching set of **double** quotation marks. Let's experiment with some strings in the IPython console...

```python
In [1]: 'This is a string.'
Out[1]: 'This is a string.'

In [2]: "This is another string, but this time with double quotation marks."
Out[2]: 'This is another string, but this time with double quotation marks.'

In [3]: 'They told me not to do this, but I didn't listen.'

SyntaxError: invalid syntax
```

Just like we expected, we can use both single and double quotation marks. What happened in the 3rd case there? Well, we opened the string with a single quotation mark, and Python started looking for the next single quotation mark to close the string. When it found that quotation mark in the word `didn't`, it assumed the string was closed after `didn`. As a result, this left `t listen.'` just hanging out, and Python didn't know how to interpret that, resulting in our error. The solution to this, as mentioned above, is to use double quotation marks in any case where your text will have single quotation marks in it. For example...

```python
In [1]: "Now that I've got double quotes, I can use all the contractions!"
Out[1]: "Now that I've got double quotes, I can use all the contractions!"

In [2]: "Can't, won't, didn't, don't... all the contractions!"
Out[2]: "Can't, won't, didn't, don't... all the contractions!"
```
As a final note before we dive into string operations, we can store strings in variables in the exact same way that we can store an `int`, `float`, or `complex`.

```python
In [1]: my_str_variable = 'This is a string variable.'

In [2]: my_str_variable
Out[2]: 'This is a string variable.'
```

#### String Operations

Surprisingly, a couple of our standard mathematical operations will work on strings, namely `+` and `*`. We can use the `+` operator to add two strings together (this is known as string **concatenation**), and we can use the `*` operator to repeat a string a given number of times. Let's take a look...

```python
In [1]: 'My first string' + 'My second string'
Out[1]: 'My first stringMy second string'

In [2]: 'Repeating string' * 3
Out[2]: 'Repeating stringRepeating stringRepeating string'
```

Note that Python didn't put spaces between the strings with either the `+` operator or the `*` operator. Why not? Because it wasn't told to! In this case, and in programming in general, we have to be extremely explicit about what we want the computer to do. To fix this, we can add a space in the middle of the first case, and then add a space to the end of our string in the second case.

```python
In [1]: 'My first string' + ' ' + 'My second string'
Out[1]: 'My first string My second string'

In [2]: 'Repeating string ' * 3
Out[2]: 'Repeating string Repeating string Repeating string '
```

That looks much better! But, what about that pesky little space at the end of our second string: `'Repeating string Repeating string Repeating string '`. Is there a way to remove this? It turns out there is! One of the methods (a name for a function that is attached to a particular object) that we can call on strings is the `strip()` method. Methods are something that we will cover in much more depth later, but for now just note that we call them on our objects through **dot notation**. We simply place a `.` at the end of our object (`str`, `int`, `float`, any variable, etc.), and then call the method like we would call a function. Here's how the use of this **dot notation** looks in practice.  

```python
In [1]: 'Repeating string Repeating string Repeating string '.strip()
Out[2]: 'Repeating string Repeating string Repeating string'

In [1]: ' Repeating string Repeating string Repeating string '.strip()
Out[2]: 'Repeating string Repeating string Repeating string'
```

So, what did the `strip()` method do? In the first example, it removed the trailing space from the string. In the second example, it removed both the leading and trailing spaces. This is exactly what the `strip()` method does - by default (without any arguments) it removes leading and trailing whitespace (*note, the method can actually remove any leading or trailing characters if you pass them to `strip()`, but whitespace is the default character that it removes*).

Are there other things that we can do with strings? There are tons! Let's store our string in a variable below, so we can get some exposure working with strings in variables.

```python
In [1]: my_str_variable = 'this IS my STRING to PLAY around WITH.'

In [2]: my_str_variable.capitalize()
Out[2]: 'This is my string to play around with.'

In [3]: my_str_variable.upper()
Out[3]: 'THIS IS MY STRING TO PLAY AROUND WITH.'

In [4]: my_str_variable.lower()
Out[4]: 'this is my string to play around with.'

In [5]: my_str_variable.replace('STR', 'fl')
Out[5]: 'this IS my flING to PLAY around WITH.'

In [6]: my_str_variable.split()
Out[6]: ['this', 'IS', 'my', 'STRING', 'to', 'PLAY', 'around', 'WITH.']
```

These are some of the most commonly used string methods. You can see above what they do by default: `capitalize()` capitalizes the first letter of the string and lowercases the rest; `upper()` converts all the letters in the string to uppercase, and `lower()` to lowercase; `replace()` replaces a given substring in your string with another given substring; finally, `split()` splits the string by an inputted string (whitespace by default, just as with `strip()`). There are many more string methods available, and you can check them out in the [docs](https://docs.python.org/3/library/stdtypes.html#string-methods).

Alternatively, you can find out what methods are available to call on strings from the IPython terminal itself (this is one of the really awesome features of IPython)! Using tab completion, if you have a string stored in a variable, you can type the variable name followed by a period, and then use tab complete to see all the methods available for strings!

```python
In [1]: my_str.  # Hit tab now!

my_str.capitalize  my_str.isalnum     my_str.lstrip      my_str.splitlines
my_str.center      my_str.isalpha     my_str.partition   my_str.startswith
my_str.count       my_str.isdigit     my_str.replace     my_str.strip
my_str.decode      my_str.islower     my_str.rfind       my_str.swapcase
my_str.encode      my_str.isspace     my_str.rindex      my_str.title
my_str.endswith    my_str.istitle     my_str.rjust       my_str.translate
my_str.expandtabs  my_str.isupper     my_str.rpartition  my_str.upper
my_str.find        my_str.join        my_str.rsplit      my_str.zfill
my_str.format      my_str.ljust       my_str.rstrip      
my_str.index       my_str.lower       my_str.split
```

**Note**: This works for all of our variable types! Not only that, but we can also tab complete the names of the variables that IPython currently knows about (those in the **namespace**).

#### Working with individual characters in strings

We know how to work with an entire string via some of the methods that we've discussed, but what if we wanted to work with the individual characters? There are a couple of ways to do this, but the first we'll focus on is through indexing. We know that to Python, a string is just a collection of characters. It turns out that we can access the individual characters simply by asking Python for a given numbered element in our collection (i.e. the string).  We do this by placing the element number that we want in square brackets, `[]`,  right after our string (or variable, if it's stored in one). This element number is referred to as the **index** of the character (or element, if it's not a string - more on this soon).

```python
In [1]: my_str_variable = 'Test String'

In [2]: my_str_variable[1]
Out[2]: 'e'

In [3]: my_str_variable[5]
Out[3]: 'S'

In [4]: my_str_variable[-1]
Out[4]: 'g'

In [5]: my_str_variable[-3]
Out[5]: 'i'
```

Using indices like this, we can access any element of a string. But why is the element at index 1 `e`, and not `T`? After all, `T` is the first element in the string. Also, what are those negative numbers doing? In the case of the former, it turns out that Python (and many programming languages) starts indexing at 0, which means that the first element in our string (and any collection that supports indexing) is accessed via indexing at 0. We refer to languages that work this way as **zero indexed**. As for the negative numbers, this is a way to access elements starting from the end of the string, rather than the beginning. Indexing from the end starts from -1 and continues downwards from there. So, we would use -2 to access the `n` in the string.

Note that we can also access any given number of the characters (any **substring**) by combining multiple index numbers separated by a colon `:`. For example:

```python
In [1]: my_str_variable = 'Test String'

In [2]: my_str_variable[1:3]
Out[2]: 'es'

In [3]: my_str_variable[5:9]
Out[3]: 'Stri'

In [4]: my_str_variable[-6:-1]
Out[4]: 'Strin'

In [5]: my_str_variable[1:]
Out[5]: 'est String'

In [6]: my_str_variable[:-1]
Out[6]: 'Test Strin'
```

This indexing turns out to be pretty useful. You might notice, though, that when indexing from `[1:3]`, only the letters at index 1 and 2 are returned; when indexing from `[5:9]`, we get the letters at indices 5, 6, 7, and 8. This is because the indices that you pass in are inclusive on the left side, and exclusive on the right side. This means that when you index, you will grab letters from the starting index that you give up to but not including letters at the ending index that you give.

What about those last two examples, where there isn't an ending index or a starting one? If you don't give an ending index, then Python assumes that your ending index is the last index in the string. Similarly, if you don't give a starting index, Python assumes that your starting index is the first index in the string. Remember, this is the zeroth index in Python (don't worry if this feels confusing, you'll get used to it quickly).

Is there a way to grab elements at regular intervals in a string? For example, what if we wanted to grab every second letter? Python allows us to do this by passing in an optional third number while indexing. This optional third number, also separated by a colon (`:`), tells Python the step size by which to move through the string when indexing. So, if we wanted to grab every second letter from the beginning to end, we could index with `[::2]`. If we wanted to grab every 3rd letter from the letter at index 2 to the letter at index 10, we could use the indexing `[2:10:3]`.

```python
In [1] my_str_variable = 'Test String'

In [2]: my_str_variable[::2]
Out[2]: 'Ts tig'

In [3]: my_str_variable[2:10:3]
Out[3]: 'sSi'
```

Got it, enough indexing already! Is there a way to cycle (or step through) each one of the letters one by one, and do something with the conditional logic we learned, rather than just grabbing a certain letter or group of letters? Of course! (Why would I ask a question for which the answer was no? That would be lame.)

#### Iteration and Strings

We can cycle through all of the letters in our string (a process called **iteration**) in one of a couple of different ways. Let's first look at cycling through with a `while` loop, since we worked with those last week.

```python
my_str, idx = 'hello', 0
while idx < 5:
    print(my_str[idx])
    idx += 1
```

This while loop will **iterate** over the letters of our string `hello`, printing each one until `idx` reaches the value 6. Since we knew the length of our string (i.e it's 5 letters long), we knew that we could use the condition `while idx < 5:` for our loop checking, and ensure that all the letters would be printed. What if we didn't know the length ahead of time, though? There is actually a function that we can use to figure this out (we'll talk much more about functions and how they work later). It's `len()`, and we simply call `len()` with our string passed as an argument, and it returns the length of our string.

```python
In [1]: my_str = 'hello'

In [2]: len(my_str)
Out[2]: 5
```

Now, we can write our `while` loop to be a little bit more general:

```python
my_str, idx = 'hello', 0
while idx < len(my_str):
    print(my_str[idx])
    idx += 1
```

Great! But we did mention that there are other ways to iterate over the letters in our string, and in general we try to stay away from `while` loops in Python.

The other way that we can iterate over the letters in our string is to use a `for` loop. `for` loops are built off of the same idea of `while` loops (doing something over and over again), but instead of continuing until some condition is no longer met, `for` loops operate directly on iterables. This leaves the concern about when to stop for Python to figure out. With a `for` loop, we don't have to care how many iterations/cycles the loop will go through. Let's look at the syntax of a `for` loop.   

```python
my_str = 'hello'
for idx in range(len(my_str)):
    print(my_str[idx])
```

**Note**: the `range()` function (which we will cover in more depth when we get to functions) as used above simply gives us a list of numbers from 0 up to but not including the inputted number. In the case above, since `len(my_str)` is 5, `range(len(my_str))` returns a list of integers from 0 to 4.

This `for` loop does the exact same thing as the `while` loop we wrote above, but with slightly different syntax. How does it work? At each iteration of the loop, `idx` is assigned one of the values in `range(len(my_str))`, and then the code within the indented block is run with that value of `idx`. How does Python know what the values of `idx` will be? Python simply goes through the values of whatever is after the `in` statement **in order**, and assigns those values to `idx`, one at a time through each iteration of the loop. Since `range(len(my_str))` returns to us a list of integers from 0 to 4, those values get assigned to `idx` as we run through the `for` loop. Let's look at one of our favorite kinds of tables to view this:

| After loop # | idx | What's Printed |
| ------------ |:---:|:--------------:|
|      1       |  0  |       'h'      |
|      2       |  1  |       'e'      |
|      3       |  2  |       'l'      |
|      4       |  3  |       'l'      |  
|      5       |  4  |       'o'      |

Note that with our `for` loop, the `idx` variable is automatically changed, rather than us having to manually update it (like we did in the `while` loop). This is one of the incredibly nice aspects of `for` loops! But wait, it gets even better!

It turns out that the above implementation of our `for` loop is actually considered to be non-Pythonic. This is because the way that `for` loops are constructed allows us to achieve the same output as above by writing the following:

```python
my_str = 'hello'
for char in my_str:
    print(char)
```

What's going on here!? Well, instead of iterating over all of the integers in a `range(len(my_str))` call like we did in our first `for` loop, we've gotten Python to simply iterate over all of the individual characters in our string, `my_str`. In each iteration of this `for` loop, `char` stores a different letter of `my_str`, and then the call `print(char)` prints that character. In the end, we get the same result as either of our `while` loops above, and the less Pythonic `for` loop that we wrote above. This way is considered to be the Pythonic way to iterate over a string (or other iterable, which we'll cover next class), and so it's an important concept to grasp.

Why is it more Pythonic? That's a good question. When we say that something is more "Pythonic", this means that we are using the language in such a way that makes your code both more readable and simultaneously uses Python's power to make your solutions more optimal. Let's look at how this applies to the final implementation of our `for` loop.

We can see that it is more readable since we don't have to index into our string anymore. This means that there is less to follow along with and keep track of; rather than keeping track of both the current index we are on and what letter that index corresponds to in our string, all we have to keep track of is the current letter we're on. We can also note that our code just looks cleaner and more simple, too. In terms of making our code more optimal, since we no longer have to index into the string to grab characters, we have fewer steps in each iteration of the loop. This means less work for Python to do.

#### A Quick Aside on String Formatting

There's one more thing that we should talk about before moving on from our discussion of strings - string formatting. String formatting is going to allow us to format strings in certain ways. Probably most usefully, it's going to allow us to insert variable contents into strings dynamically. We'll get an idea of how and when this is most useful as we work through this course. For now, let's just look at the syntax of it all.  

```python
In [1]: my_name = 'Sean'

In [2]: print('Hello %s' % my_name)
Hello Sean

In [3]: print('Hello {}'.format(my_name))
Hello Sean
```

How is this working? Well, in each case, it's filling in a given part of our string with the value of our variable. In the first case, we use a `%` sign to denote where the replacement should happen, followed by a letter to denote what type of variable will be passed in there (`s` is used for string, `d` is for a decimal, etc.). You can find what each letter denotes [here](https://docs.python.org/2/library/stdtypes.html#string-formatting). In the second case, we use brackets `{}` to denote where the replacement should take place. We can also place numbers, or even variable names themselves inside these brackets and referece them in the `format()` method...

```python
In [1]: print('Hello {0}'.format(my_name))
Hello Sean

In [2]: print('Hello {name}'.format(name=my_name))
Hello Sean
```

This is something that we don't use much past pretty simple cases, but there are many more things you can do with it - you can read about them [here](https://docs.python.org/3/library/string.html#format-specification-mini-language). In general, though, string formatting is much more readable and dynamic as compared to a bunch of concatenation.

### Lists

We've been talking about this idea of iterables for a while now and have seen our first example of it already when looking at strings. What other data structures does Python have for us to iterate through?

#### Intro to Lists

Lists are a more complex type of data structure. From a high level, lists are collections of ordered items. These items can be of any type, and a list can contain items of different types (or all the same type). You can construct a list in one of two ways. The first is simply by passing an arbitrary number of items into square brackets, `[]`, separated by commas. The second is by passing an iterable into the `list()` constructor (we'll discuss exactly what an iterable and constructor are later). For example...

```python
In [1]: my_first_lst = [1, 'hello', 3, 'goodbye']

In [2]: my_first_lst
Out[2]: [1, 'hello', 3, 'goodbye']

In [3]: my_second_lst = list('hello')

In [4]: my_second_lst
Out[4]: ['h', 'e', 'l', 'l', 'o']
```

Note that when we pass an iterable to the `list()` constructor, it breaks up each individual element in the iterable into a separate element in the list. Also, note again that we are able to place multiple different types of data structures into our lists. If we wanted to, we could even create a list of lists (and later we'll see we can make lists of any of the other data structures we learn).  

```python
In [1]: my_lst_of_lsts = [[1, 2, 3], ['str1', 'str2', 'str3'], [1, 'mixed', 3]]

In [2]: my_lst_of_lsts
Out[2]: [[1, 2, 3], ['str1', 'str2', 'str3'], [1, 'mixed', 3]]
```

#### List Operations

Just as we have operations (methods) that we can use on strings, we also have some for lists! Here are some of the most common operations that we have available for lists...

```python
In [1]: my_lst = [1, 2, 3, 4]

In [2]: my_lst.append(5)

In [3]: my_lst
Out[3]: [1, 2, 3, 4, 5]

In [4]: my_lst.pop()
Out[4]: 5 # my_lst now holds [1, 2, 3, 4]

In [5]: my_lst.remove(4)

In [6]: my_lst
Out[6]: [1, 2, 3]

In [7]: my_lst.reverse()

In [8]: my_lst
Out[8]: [3, 2, 1]

In [9]: my_lst.sort()

In [10]: my_lst
Out[10]: [1, 2, 3]
```

For most of these, you might be able to guess what they do: `append()` adds an element to the end of the list; `pop()` removes the last element from the list and returns it; `remove()` will remove a given element from the list; `reverse()` will reverse the elements of the list, in place; and `sort()` will sort the elements of the list, in place. For a more detailed discussion and/or to see all of the methods available for lists, see the [docs](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

Just as we can use tab complete in IPython to see all the available methods for strings, we can also do this with lists!

```python
In [1]: my_lst. # Hit tab now!

my_lst.append   my_lst.index    my_lst.remove   
my_lst.count    my_lst.insert   my_lst.reverse  
my_lst.extend   my_lst.pop      my_lst.sort
```

#### Working with Individual Elements in Lists

Working with individual elements in a list works the same way as working with characters in strings.

```python
In [1]: my_lst = [1, 2, 'hello', 'goodbye']

In [2]: my_lst[1]
Out[2]: 2

In [3]: my_lst[2:3]
Out[3]: ['hello']

In [4]: my_lst[:]
Out[4]: [1, 2, 'hello', 'goodbye']

In [5]: my_lst[-1]
Out[5]: 'goodbye'
```

**Note**: Remember that the ending index is non-inclusive.

Just as with strings, we can also add a 3rd number to our list indexing to step through the list and only grab elements at regular intervals.

```python
In [1]: my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

In [2]: my_lst[::3]
Out[2]: [1, 4, 7, 10]

In [3]: my_lst[4::2]
Out[3]: [5, 7, 9]

In [4]: my_lst[:4:3]
Out[4]: [1, 4]
```

#### Lists and Iteration

We can also iterate through lists in the same way that we can iterate through strings. I'll only show the final, efficient way that we use to iterate through lists below.

```python
In [1]: my_lst = [1, 2, 3, 4, 5]

In [2]: for num in my_lst:
   ...:     print(num)

1
2
3
4
5
```

Just as in the case of iterating through our strings, our `for` loop iterates over all of the values in our iterable (this time a `list`), and then places those values into the variable name we give (`num`) at each iteration of the loop.

What if I absolutely need the indices, though? Is there a way that I can still iterate through using a for loop without `range()` and `len()`, the way you're telling me is Pythonic, and still get the indices?? Yes!

There is a function, `enumerate()`, that will allow us to iterate through a list or string (grabbing each of the individual elements in the list or characters in the string) while at the same time keeping track of the index. The trick is that instead of using just one variable (such as `num` above) to store the elements of the list as you loop through them, we use two variables. The first of these variables stores the current index, and the second stores the corresponding element in the list. Let's see how it works...

```python
In [1]: my_lst = [1, 2, 3, 4, 5]

In [2]: for idx, num in enumerate(my_lst):
   ...:     print(idx, num)
   ...:
0 1
1 2
2 3
3 4
4 5
```

The trick here is that when we call `enumerate()` on our list, `enumerate()` gives us back two values at each iteration through the loop. The first value is the current index (which we chose to store as `idx` above), and the second value is the current element of the list (which we chose to store as `num`). Note how `idx` tracks one behind `num`... this is because `idx` starts at 0 and `num` starts at 1.

### The Magic of Iterables

Strings and lists are two kinds of iterables that we have looked at today. There are many other kinds of iterables that we'll work with in Python, and you can even define your own iterable if you'd like. The important thing that we want to note for now, though, is that the `for` loops that we have looked at today will work for any iterable. You can simply write `for <variable name> in <iterable>:`, and at each iteration through the loop you will be able to access another element from that iterable via `variable name`. Also, as mentioned above, the `list()` constructor accepts any iterable as an argument, and then creates a `list`, where each element in the iterable is a single element in the `list`.
