# Magic Methods (and Interfaces)
  
## Warmup: Coffee Cup

We're going to be digging into objects and classes more today, so let's warm up with an exercise.

#### Exercise: Coffee Cup

Make a `CoffeeCup` class, which can be used to make `CoffeeCup` objects.  The cup should have two states, full or not full.  Create a method `drink` which empties a full cup, and `fill` which fills an empty cup.

#### Exercise: Coffee Cup Revisited

Ok, maybe that was unreasonable, no one drinks a full cup of coffee in one drink.  Modify your `CoffeeCup` class to keep track of *how full* the coffee cup is.  Create a `sip` method which takes a small drink, a `gulp` method which takes a large drink, and a `pour_out` method which empties the cup (along with the `fill` method from before).


## You Can Add Multiple Things

Consider an example that may or may not have been mysterious until now: in python, the `+` operation can mean multiple things:

```python
$ 2 + 5
7

$ 'Matt' + ' ' + 'Drury'
'Matt Drury'

$ ['apples', 'oranges'] + ['bananas', 'tomatoes']
['apples', 'oranges', 'bananas', 'tomatoes']
```

We used the same symbol `+` to operate on many different data types.  In each different situation, a different thing happened:

  - When we used `+` on numbers, we did standard arithmetic.
  - When we used `+` on strings, we concatenated.
  - When we used `+` on lists, we extended the lists.

#### Question: What Else?

What other types of things does it make sense to add?

#### Questions To Answer...

So, a couple questions arise:

  - How does python know what to do with each different use of the `+` symbol?
  - How can we create objects that know how to use the `+` symbol?

The answer to these questions are found in python's concept of **magic methods**.

##  Magic Methods

**Magic methods** are a special notation in python that can be used to add natural behaviour to classes.  For example, we can use magic methods to:

  - Allow our custom objects to be added.
  - Create natural string representations of our object, say, to print them.
  - Allow our objects to act like dictionaries.
  - Allow our custom object to be tested for equality.

A **magic** method is any method whose name starts and ends with a double underscore

  - `__add__` is used to allow for addition.
  - `__str__` and `__repr__` are used to add printing capabilities.
  - `__setitem__` and `__getitem__` are used for creating dictionary like behaviour.
  - `__eq__` is used to allow for equality testing.

There are many more.  [A complete list is here](https://www.python-course.eu/python3_magic_methods.php).

**Note:** you should not feel it necessary to memorize all of these!  You will learn them over time, and that is fine.

### Making a Dictionary like Object

Let's start where we left off last class.  We build a dictionary like object which was symmetric.

```python
$ sym_dict = SymmerticDict()
$ sym_dict.add_key_value('Matt', 'Data Scientist')
$ sym_dict.add_key_value('Jack', 'Physicist')
$ sym_dict.lookup('Matt')
'Data Scientist'
$ sym_dict.lookup('Jack')
'Physicist'
$ sym_dict.lookup('Data Scientist')
'Matt'
$ sym_dict.lookup('Physicist')
'Jack'
```

Our goal is to make this interaction more **natrual** and dictionary like:

```python
$ sym_dict = SymmerticDict()
$ sym_dict['Matt'] = 'Data Scientist'
$ sym_dict['Jack'] = 'Physicist'
$ sym_dict['Matt']
'Data Scientist'
$ sym_dict['Jack']
'Physicist'
$ sym_dict['Data Scientist']
'Matt'
$ sym_dict['Physicist']
'Jack'
```

This is nice.  Now a user of our class doesn't need to remember that we named our methods `add_key_value` and `lookup`, they can just use their existing knowledge about dictionaries to get their work done.  The fact that they are using our custom `SymmetricDict` object disappears from their mind.

### `__setitem__` and `__getitem__`

It is actually really easy to accomplish this, now that we have understood what we have to do.  Where we had this code in our class before:

```python
def add_key_value(self, key, value):
    self.dict[key] = value
    self.dict[value] = key
```

To add more natural dictionary like behaviour we only need to change the **name of the method**!

#### Exercise: `__setitem__`

Change the name of the method to `__setitem__`.  Check that it works.

#### Exercise: `__getitem__`

Change the name of the `lookup` method to `__getitem__` and make sure it works!

###  Pretty printing with `__repr__` and `__str__`

Now lets look at what happens when we print our object:

```python
$ print(sym_dict)
<symmetric_dict.SymmetricDict object at 0x1124c5278>
```
This is not so useful.  The only interesting information we get out of this is the name of the class associated with the object.  If we really want our users to feel that our `SymmetricDict` is just like a regular dictionary, it would be good to have print work that way too.

The `__str__` magic method controls how our object will be converted to a string, which is what happens when we print something.

```python
$ str(sym_dict)
'<symmetric_dict.SymmetricDict object at 0x1124c5278>'
```

#### Exercise: `__str__` 

Implement a `__str__` method for your `SymmetricDict` class, which returns a string representation of the internal dictionary.

```python
$ str(sys_dict)
"{'a': 2, 2: 'a'}"
```

After implementing this, you should be able to `print` your `SymmetricDictionary` and get a useful result.

```python
print(sym_dict)
{'a': 2, 2: 'a'}
```

## Putting it Together: A Linear Polynomial Class

A **linear polynomial** is an algebraic expression like `m x + b`.  So, the following are examples of linear polynomials

```
2x + 1
x  # <- since b can be zero
1  # <- since m can be zero
-x + 2
3z - 4
```
#### Exercise: `LinearPolynomial` class.

Create a `LinearPolynomial` class.  The following interaction will serve as an example of how it should work.  You will have to figure out what methods to implement, and how they should work.

```python
$ f = LinearPolynomial(m=2, b=1)
$ g = LinearPolynomial(m=-4, b=4)
$ print(f)
2x+1
$ print(g)
-4x+4
$ f.evaluate(0)
1
$ f.evaluate(2)
5
$ g.evaluate(0)
4
$ g.evaluate(1)
0
```

### Arithmetic With `__add__` and `__sub__`

As we mentioned at the beginning of the lesson, many objects in Python can be added with `+`.  Linear polynomials can be added and subtracted (as mathematical objects)

```
(2x + 1) + (-x + 2) = x + 3
(-x + 5) + (x - 7) = -2
(2x + 1) - (-x + 2) = 3x - 1
```

but our code does not yet support this

```python
$ f + g
TypeError: unsupported operand type(s) for +: 'LinearPolynomial' and 'LinearPolynomial'
```

We can add arithmetic behaviour to our classes by implementing the `__add__` and `__sub__` methods.

```
def __add__(self, other):
    ...
```

#### Question:
What **type of object** should `__add__` return?

#### Exercise: Implement `__add__`

Implement the `__add__` method on your `LinearPolynomial` class.

#### Exercise: Implement `__eq__`

What do you think the magic method `__eq__` should do?  What should it return?  Implement it.


### Final Exercise: Currency Converter

Write a currency converter class.  Here's an example of how it should work.

```python
$ from currencies import CurrencyConverter
$ v1 = CurrencyConverter(23.43, "EUR")
$ v2 = CurrencyConverter(19.97, "USD")
$ print(v1)
23.43 USD
$ print(v1.convert("USD"))
27.72 USD
$ print(v1 + v2)
40.62 EUR
$ print(v2 + v1)
57.19 USD
```

You should support at least five currencies.

You will need to look up conversion rates between currencies.  What data structures are useful for storing these conversion rates?
