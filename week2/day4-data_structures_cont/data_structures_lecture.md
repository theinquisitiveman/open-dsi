# Tuples, Dictionaries, and Sets

## Data Structures Continued

Up till now you have learned about some very useful data structures in Python: numeric types, strings, and lists. However, the fun doesn't stop there! Today we are going to talk about some other data structures that will allow us to solve very different problems from those that we have been solving so far.

### Mutability

One thing that will come up as an important distinction in the structures we learn about today is the concept of mutability. **Mutability** refers to the capability of an object to be changed after it has been instantiated. With lists, we can change the contents at any arbitrary index and even grow the list dynamically...

```python
# Declare a simple list
l = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8 , 9]

# Change the element at the 4th index, the fifth in the list, to 0
l[4] = 0  # [0, 1, 2, 3, 0, 5, 6, 7, 8 , 9]

# Add the number 1 to the end of the list
l.append(1)  # [0, 1, 2, 3, 0, 5, 6, 7, 8 , 9, 1]
```

Mutability is nice, but there are times when you won't want your data structure to be mutable. For example, if you're allowing a user of your program to have access to a data structure, one way to ensure that they won't mess with it (sometimes users do this out of malice, and we want to try and prevent it) is to make the structure **immutable**. There are many more reasons why immutability is a desired trait, and we will discuss plenty more of them throughout the rest of the course.

Let's quickly discuss the mutability of objects you already know about. The first types you learned about were various numerics (`int`, `float`, `complex`) - these are all immutable. What?! Immutable you say? But I can change a value in a variable after it's been declared. Consider the following simple code.

```python
# First mention of x
x = 1

# Change the value of x
x = 2
```

How can numerics be immutable while at the same time allowing us to change the value of a variable that holds a numeric? What's really going on under the hood when you assign a value to a variable is that Python puts that value or data structure in memory, and then simply associates the variable name with that value or data structure. Changing a variable, then, simply amounts to associating that name with a different thing in memory.

Using this same logic, it shouldn't be too hard to explain to yourself why strings are immutable as well. The contents of that string are put in memory, and the variable name you want to use is associated with that string. When you want to change the variable to a different string, Python simply associates that name with a different, also immutable string.

**Note**: The discussion of Python having names [here](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#python-has-names) is really good if you're looking for more clarification.

Lists, on the other hand, are mutable. What this really means is that you can change the structure of the list in addition to the names of the things that are in the list (notice the specific use of names there, we'll come back to that in the next section).

### Tuples

Tuples are simply the immutable brother of the `list`. Tuples are immutable ordered collections. This means that once a tuple is instantiated, all you can do is access its contents. You cannot make a tuple longer. You cannot reassign what is in a tuple (there are some subtleties to this which we will discuss presently). Similar to lists, tuples are declared by passing an iterable to the `tuple()` constructor, with the syntactic sugary parenthesis, or without parenthesis (this works because Python automatically interprets comma separated things that aren't specifically specified otherwise as tuples).

```python
my_first_tuple = tuple([1, 2])
my_other_tuple = (1, 2)
my_third_tuple = 1, 2
```

Alright, thats all well and good. But what are the direct implications of using a tuple versus a list. Well, suppose we are trying to grab the even numbers, stored in some collection, somewhere. If we were to do this with a list, that might look like the following...

```python
evens = []
for element in some_collection:
    if element % 2 == 0:
        evens.append(element)
```

We could try to do this with evens as a tuple instead of a list with `evens = ()`, but once we tried to run our code we would immediately get an error that says `AttributeError: 'tuple' object has no attribute 'append'`. The error message is pretty self explanatory. In plain English, it tells us that tuples have no ability to append. This is just as we expected given that they are immutable.

You might be asking yourself what a tuple can store? The answer is, just as with lists, anything! Just as with lists, the elements of tuples can be accessed via zero-based indexing, and looped through with a `for` loop. And just as with lists, the elements in a tuple can be either homogeneous or heterogeneous (know though, that there are structures in Python that enforce homogeneity). Let's stick with looking at tuples for now, and take a look at some of the things we can store.

```python
In [1]: t = (1, 3.5)

In [2]: type(t[0])
Out[2]: int

In [3]: type(t[1])
Out[3]: float

In [4]: t = (1, [1, 2])

In [5]: type(t[1])
Out[5]: list

In [6]: t = (1, (1, 2))

In [7]: type(t[1])
Out[7]: tuple
```

One tricky thing about tuples is that even though they are immutable, if they are storing any mutable data types, those structures **can** be changed!

```python
In [1]: t = (1, [1, 2])

In [2]: t[1].append(3)

In [3]: t
Out[3]: (1, [1, 2, 3])
```

**Note**: This is the first time that you've seen the `append()` method used directly on something that doesn't look like a list. This works because Python, upon accessing the contents of `t` at index 1, will find a list. It will then immediately call the `append()` method on that structure. This concept of being able to act on data structures that you don't necessarily know the contents of is very powerful, and we will use it time and again.

One last thing to note is that since tuples are immutable, they have very few methods associated with them - only `count()` and `index()`. For this reason we say that they are very lightweight; they don't take up much space in memory, but also don't have much built in functionality.

### Dictionaries

So far, the only collections that we have talked about are ordered.  These are great as containers if there is some intrinsic order to the data that we're storing. However, there are plenty of times when we don't care about order, either because it simply doesn't matter or because the data are associated with each other in a different way. For example, say we have a bunch of state names and we want to associate each state's name with its capital. How would we do this in a list? One way would be to have tuples that store pairs of states and their capitals.

```python
states_caps = [('Georgia', 'Atlanta'), ('Colorado', 'Denver'), ('Indiana', 'Indianapolis')]
```

There are limits to how intuitive this storage method is, though. Consider that if we wanted to find the capital of Indiana, we would have to search through the entire list, checking to see if Indiana is in the first position of each tuple. If/when we found it, we would then have to grab the second position of that tuple.

```python
search_state = 'Indiana'
capital = 'State not found'
for state_cap in states_caps:
    if state_cap[0] == search_state:
        capital = state_cap[1]
        break
print(capital)
```

While this isn't horrible, we can do better. Python to the rescue!!!

The dictionary data structure in Python allows us to store data in a way that is more intuitive for this problem. Dictionaries allow us to store a value associated with a keyword. In the example above, we wanted to store the capital as the value, where that capital value was associated with its state keyword. There are many ways to instantiate a dictionary. Let's look at the simplest way first.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: states_caps_dict
Out[2]: {'Colorado': 'Denver', 'Georgia': 'Atlanta', 'Indiana': 'Indianapolis'}
```

This looks very similar to the way that we made lists and tuples, except now we use curly braces, and there is this new use of colons (`:`). On the left side of each colon we have the keyword, and on the right the value associated with it. Each *key-value* pair, as we call them, is separated by a comma.

So how do we use these things once we have them? Let's take the example from above and say we're trying to find the capital of Indiana. With a list of tuples, we had to search through the list of tuples from the beginning to find the one with 'Indiana' in the first position, and then grab the second entry in that tuple. With dictionaries it's much easier!

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: states_caps_dict['Indiana']
Out[2]: 'Indianapolis'

In [3]: states_caps_dict['Washington']
___________________________________________________________________________
KeyError                                  Traceback (most recent call last)
<ipython-input-3-fac88f6748> in <module>()
    > 1 states_caps_dict['Washington']

KeyError: 'Washington'
```

All we had to do was index into the dictionary, like we did with lists, but this time with the key. The dictionary then returns the associated value. Notice that if we tried to find a key that wasn't already in the dictionary with `[]` indexing, we get a `KeyError` telling us that that key is not stored in the dictionary.

This shouldn't happen too frequently, because we often know the keys in our dictionaries. However, there are times when we don't know if a key is in the dictionary already. For these times, we luckily have the `get()` method. This method takes the key you're trying to find and a default return value to hand back if the key doesn't exist.

```python
In [4]: states_caps_dict.get('Washington', 'State not found')
Out[4]: 'State not found'
```

Above, we asked `states_caps_dict` for the value associated with the key `'Washington'`, and told it to return `'State not found'` if the keyword wasn't in the dictionary. And lo-and-behold, we get back `'State not found'`, which makes sense because we knew that `'Washington'` wasn't in the dictionary.

#### Mutability of Dictionaries

At this point, a question that could be on your mind is whether or not dictionaries are mutable? Well, first, great question. And, second, yes, yes they are! Before we talk about how to mutate them, let's describe dictionaries in the language that we used for lists and tuples. A dictionary is defined as an unordered collection of key-value pairs that requires unique keys.

With that in mind, let's recall how we mutated a **list**. To change an element at an existing index, we just indexed into the list and did assignment. To make them bigger, we used the `append()` method. This method of mutation made a lot of sense, considering that lists are ordered. In the unordered paradigm where dictionaries live, to change/add a key-value pair, all you have to do is index into it with the existing/new key and assign a value to it. Let's take a look.

```python
In [1]: my_dict = {'thing': 1, 'other': 2}

In [2]: my_dict['thing']
Out[2]: 1

In [3]: my_dict['thing'] = 3

In [4]: my_dict['thing']
Out[4]: 3

In [5]: my_dict['thingy'] = 4

In [6]: my_dict['thingy']
Out[6]: 4

In [7]: my_dict
Out[7]: {'other': 2, 'thing': 3, 'thingy': 4}
```

#### Caveat to Dictionary Keys, More on Mutability

We have learned that dictionaries make it easy to store key-value relationships in a single data structure that is designed for easy value retrieval. So, what are the restrictions on things you can put in a dictionary? As for the values, like in lists, there are none! But in terms of the keys those values are associated with, that's a different story.

Keys in dictionaries **must** be an immutable type, and if that type is a container, then the container cannot contain any mutable types. Why is this the case? The answer lies in the way that dictionaries store values and associate them with a key.

Python dictionaries are an implementation of what's known as a *hash map* or *hash table* ([here's](https://en.wikipedia.org/wiki/Hash_table) the wikipedia page for them if you want to learn more). This computer science idea is basically a function that relates any input, in our case the keys, to a location in memory. Thus, retrieval of a value from a dictionary is entirely dependent on the key. The consequence of this is that, if we were to use a mutable type as the key for a dictionary and later change what that key looked like by mutating it, the dictionary wouldn't be able to find the value it was supposed to associate with that key (since the key has now changed). Let's take a gander at what this type of incorrect usage would look like, but know, the code below will **not** run.

```python
# Original key
my_bad_key = ['key']

# Dictionary declared with a list as a key (won't work)
my_dict = {my_bad_key: 'This wont work'}

# Let's append to our mutable 'key'
my_bad_key.append('other_key')

# How is the dictionary supposed to know what we're looking for???
my_dict[my_bad_key]
```

This idea is so important that Python doesn't leave it up to you to remember to make keys immutable types. It just flat out won't let you do it.

```python
In [1]: my_bad_key = ['key']

In [2]: my_dict = {my_bad_key: 'This wont work'}
___________________________________________________________________________
TypeError                                 Traceback (most recent call last)
<ipython-input-2-a1fb4b3621ba> in <module>()
    > 1 my_dict = {my_bad_key: 'This wont work'}

TypeError: unhashable type: 'list'
```

The above code attempts to set a list as a key to a dictionary. Luckily, it throws an error as soon as we try, telling us that it can't hash a list (read: list's aren't immutable).

#### Getting More Out of Dictionaries

We now know how to make and alter dictionaries and how to use them to store arbitrary key-value pairs; let's talk about how to use them with loops.

As with lists and tuples, dictionaries are iterables in Python. This means that Python knows how to traverse everything that's stored in the collection. The way we did this with list was with a `for` loop. We will again use the `for` loop with dictionaries, but there are a few changes in how it's implemented, since dictionaries are unordered, key-value pairs whereas lists are ordered collections of values.

Let's revisit how we traverse a list with a `for` loop. Consider the following code that only prints the even numbers between 0 and 9.

```python
for element in range(10):
    if element % 2 == 0:
        print(element)
```

This specific syntax makes sense, since we want to check each value in the list, one at a time.  Each time we grab a number from the list, we give it the name `element`, check if it's even, and then print that value if it is. It's the one at a time part that I want to call you're attention to. Lists are an ordered collection of values; dictionaries, on the other hand, have keys and values that are tied together. However, if we were to traverse a dictionary with a for loop, we would expect to only get one of these out. Naturally, it's the keys.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for thing in states_caps_dict:
   ...:     print(thing)

Georgia
Indiana
Colorado
```

Notice when we access the keys, they are not printed in order. Remember that dictionaries are unordered. Here we see a direct ramification of that fact; we are not guaranteed any particular order when accessing a dictionary's keys. It's not necessarily a problem, just a random fact we keep in our pocket for a rainy day.

The natural question that follows is whether we can loop through all of the values? This can be done with the aptly named `values()` method on dictionaries.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for value in states_caps_dict.values():
   ...:     print(value)

Atlanta
Indianapolis
Denver
```

We can see that all of the capitals (the values in the dictionary) are printed, again in no particular order. One thing to know is that there is an analogue to `values()` for keys, `keys()`.

This is a very useful feature, but it gets even better! One of the most useful ways to loop through the contents of a dictionary is by getting each key-value pair together in turn within the loop. The `items()` method does exactly this. To use it we will employ a similar syntax to what we used with `enumerate()`.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for state, capital in states_caps_dict.items():
   ...:     print(state, capital)

Colorado Denver
Indiana Indianapolis
Georgia Atlanta
```

This is awesome! But as a learning tangent, let's see what's happening when we use this syntax. As above we are going to use the `items()` method, but this time not store the output in both a `state` *and* `capital` variable.

```python
In [1]: states_caps_dict = {'Georgia': 'Atlanta', 'Colorado': 'Denver', 'Indiana': 'Indianapolis'}

In [2]: for thing in states_caps_dict.items():
   ...:     print(thing)

('Georgia', 'Atlanta')
('Indiana', 'Indianapolis')
('Colorado', 'Denver')
```

Now that we're only using a single variable to grab the output of `items()`, we can clearly see that the method is outputting a tuple. So what was happening when we used `state` and `capital` to grab the output?? Very frequently we want to put the separate values from ordered collections into different variables. This happens so frequently, in fact, that Python has a built way to do it quickly (called **unpacking**).

So, when, Python sees the two variable names `state` and `capital` in the first implementation, it knows to take the values in the tuple returned from `items()` and put the first one in `state` and the second in `capital`. This is what was happening when you called `enumerate` - it returned a tuple with the index it was on, as well as the value itself. It is up to you whether or not to grab those values in a single variable as a tuple or have Python unpack it for you into two variables.

**Note**: Python will not allow you to "unpack" a collection containing a single item into multiple variables.

### Sets

There is one more data structure that we're going to take a look at today, the `set`. A set combines some of the awesome features of both the `list` and the `dictionary`. A set is defined as an unordered, mutable collection of unique items. What does this mean? It means that a set is a data structure where you can store items and not care about their order, knowing that there will always be at most one of them in the structure.

This description, while highly informal, is rather spot on. Sets in Python are actually analogous to sets that you would see in a mathematical setting. For this reason, much of the jargon and functionality that you will hear about when learning and talking about Python sets is similar to, if not exactly the same as, that which applies to mathematical sets ([here's](https://en.wikipedia.org/wiki/Set_(mathematics)) the wiki on sets if you want a quick overview of them).

Let's take a look at how we construct sets.

```python
In [1]: my_set = set([1, 2, 3])

In [2]: my_other_set = {1, 2, 3}

In [3]: my_set == my_other_set
Out[3]: True
```

Here we see the two ways we have to make sets, both with the constructor, which takes an iterable, and with the syntactic sugary curly braces (*Note, the curly braces are also used for dictionaries. In those we had a colon separating the keywords and values, which is how Python determines whether or not you're declaring a set or a dictionary. The only place where Python doesn't know is when declaring an empty structure. When this happens, Python can't figure out if you want a dictionary or a set. For this reason, the empty curly braces `{}` always mean an empty dictionary to remove ambiguity*). Sets with the same items in them will evaluate as equal.

If we take a look at the methods that are available on sets we see:
```
set.add                          set.intersection                 set.remove
set.clear                        set.intersection_update          set.symmetric_difference
set.copy                         set.isdisjoint                   set.symmetric_difference_update
set.difference                   set.issubset                     set.union
set.difference_update            set.issuperset                   set.update
set.discard                      set.pop  
```

As discussed earlier, many of these methods are similar to, if not the same as, those available to mathematical sets. Naturally, we see ways to compute set operations (`intersection()`, `union()`, etc.) and alter the set (`add()`, `update()`, `pop()` and `remove()`). Let's take a look at some of these methods in action.

```python
In [1]: my_set, my_other_set = {1, 2, 3}, {5, 6, 7}

In [2]: my_set.union(my_other_set)
Out[2]: {1, 2, 3, 5, 6, 7}

In [3]: my_set.add(4) # {1, 2, 3, 4}

In [4]: my_set.update(my_other_set) # {1, 2, 3, 4, 5, 6, 7}

In [5]: my_set.remove(5) # {1, 2, 3, 4, 6, 7}

In [6]: my_set.intersection(my_other_set)
Out[6]: {6, 7}
```

All of these methods should look fairly intuitive. The `update()` method is like an `add()` en masse. The `union()` method is like adding two sets together, but since there are only unique elements in a set, it removes duplicates. The `intersection()` method returns those elements that the sets have in common.

These are some of the most common set operations you will ever use. If you'd like to take a look at the documentation for all of them, check it out [here](https://docs.python.org/3/library/stdtypes.html#set).

#### Why Do We Need Sets?

Alright, that's cool, but when would I use a set? That's a great question! The most apparent answer is for times when you need to perform set operations, like checking what elements two lists have in common. Take the set of them both and find the intersection of those sets. The most obvious use case is to find the unique items in an iterable. There's also another amazing place where we'll want to use sets that might not be so apparent.

Remember, when discussing dictionaries above, we talked about how checking if an item is in a list requires us to check every item in the list? This can be computationally expensive and generally we want to avoid it. What do we do instead, then?

We use a set! The reason why lies in the fact that sets in Python are built very similarly to dictionaries. There's an underlying hash table that allows elements to be stored, and, more importantly, queried for membership within a set (*Note, this means that the elements of a set have to be immutable*). This operation happens much faster with sets than with lists ([here's](https://wiki.python.org/moin/TimeComplexity) some coverage on how quickly some Python methods run). Let's take a look at this in action, and simultaneously learn about how to time things in IPython.

```python
In [1]: my_list = list(range(10000))

In [2]: my_set = set(my_list)

In [3]: timeit 1000 in my_list
100000 loops, best of 3: 19.2 µs per loop

In [4]: timeit 1000 in my_set
10000000 loops, best of 3: 87.2 ns per loop
```

Here we used the magic `timeit` function that's built into IPython. To use it, call `timeit` and then a line of code. We can see that the list version of checking membership in a collection took ~200 times longer than the set version. This is two orders of magnitude! That number would only get bigger as the size of the collection that we're checking against grows.
