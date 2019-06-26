# Beginning Functions Exercise 2

# Instructions

Tonight you are going to get some practice writing functions that work together. Much of what we do in programming requires us to break down problems into smaller pieces. Tonight's assignment is aimed at getting you practice doing just that - working on breaking problems down to solve them with functions.

To start off, we'll give you already completed functions, and ask you to break them into smaller ones. The next part of the assignment will outline problems, and describe functions that we want you to write to solve them. This outline of breaking down the problem into smaller problems will get you used to thinking about the top-down process. Finally, you will get a set of problems to solve on your own, using the top down approach. Let's get started!

# Assignment

### Part 1 - Breaking Code Apart

For this section, you will be given functions that have a good amount of code in them. You task is to break them apart into more than one function, such that the original function we give you calls another function (which you'll define). For example, say I have the function below:

```python
def my_function(n):
    if n > 10:
        for _ in range(n - 9):
            print('I love Python!!!')
    else:
        for _ in range(n):
            print('I love Python so much!!!')
```

One way that we can break up this function is to have a separate function that performs a loop over the print statements. After all, we do have two blocks of code in `my_function` that are both looping over print statements. In the name of the DRY methodology, we should think about building a function that could help us do this. This function could accept an integer and a string to print. Then, it would loop through a range using that integer, printing the string in each iteration (this is exactly what we're doing above). Check it out...

```python
def print_n_string(print_times, print_string):
    for _ in range(print_times):
        print(print_string)

def my_function(n):
    if n > 10:
        print_times = n - 9
        print_n_string(print_times, 'I love Python!!!')
    else:
        print_times = n
        print_n_string(print_times, 'I love Python so much!!!')
```

Notice how the this new implementation only includes a single `for` loop, whereas before we had two. This is great, especially since we want to employ DRY programming as much as possible. Also, we can easily see what we are changing in each case of the `if`-block. This makes the code a little more readable.

We want you to do the same for all of the functions given to you in this section. One thing to keep in mind is that it's usually very useful to understand what the code is doing before you break it apart. So, make sure to read the code. Even better, you could come up with a test for it, and then go through it line by line to make sure you are clear on exactly what each function is doing before you break it apart.  

1. Break apart the function:

 ```python
 def update_library(books, library):
     '''
     Input:  List - book names, Set - books already in library
     Output: List - books that weren't in the library
     '''
     new_books = []
     for book in books:
         if book not in library:
             print('The book, {} is new!'.format(book))
             new_books.append(book)
         library.add(book)
     print(library)    
     return new_books
 ```

2. Break apart the function:

 ```python
 def play_rock_paper_scissors(n_rounds):
     '''
     Input:  Int - number of rounds to play rock paper scissors for
     '''
     for _ in range(n_rounds):
         player_1 = input('Player 1 play (r/p/s): ')
         player_2 = input('Player 2 play (r/p/s): ')
         if player_1 == player_2:
             print("It's a tie!")
         elif player_1 == 'r' and player_2 == 's':
             print('Player 1 wins!')
         elif player_1 == 'r' and player_2 == 'p':
             print('Player 2 wins!')
         elif player_1 == 'p' and player_2 == 'r':
             print('Player 1 wins!')
         elif player_1 == 'p' and player_2 == 's':
             print('Player 2 wins!')
         elif player_1 == 's' and player_2 == 'r':
             print('Player 2 wins!')
         elif player_1 == 's' and player_2 == 'p':
             print('Player 1 wins!')
         else:
             print("Someone didn't play right!")
 ```

3. Break apart the function:

 ```python
 def repeat_list_of_file_line(file_name, line_num, num_copies):
     '''
     Input:  Str - path to file,
             Int - number of line to copy from file,
             Int - number of times to copy line into list
     Output: List - filled with num_copies of line_num in file_name
     '''
     line = None
     with open(file_name) as f:
         for i, file_line in enumerate(f, 1):
             if i == line_num:
                 line = file_line.strip()
     if not line:
         copies_of_line = 'There were not {} lines in the document'.format(line_num)
     else:
         copies_of_line = [line for _ in range(num_copies)]
     return copies_of_line
 ```
4. Break apart the function:

 ```python
 import this

 def decode_zen_of_python():
     zen_decoder = this.d
     coded_zen = this.s
     print(coded_zen)
     decoded_chars = []
     for char in coded_zen:
         if char.isalpha():
             decoded_chars.append(zen_decoder[char])
         else:
             decoded_chars.append(char)
     decoded_text = ''.join(decoded_chars)
     print('\n' + decoded_text)
 ```

### Part 2 - Beginning to Write Top-Down

1. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.

 ```python
 def get_month_season(month):
     '''
     Input:  Str - Abbreviation of month
     Output: Str - Season of inputted month
     '''
     pass

 def month_info(month, category):
     '''
     Input:  Str - Abbreviation of month, Str - information category to get for month
     Output: Str - category information for the specified month

     Categories supported: 'full name'   ex: month_info('jan', 'full_name') -----> 'January'
                           'num_month'   ex: month_info('may', 'num_month') ----->  5
                           'birth_stone' ex: month_info('jul', 'birth_stone') ---> 'Ruby'
                           'season'      ex: month_info('oct', 'season') --------> 'Fall'
     '''
     full_names = {'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
                   'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
                   'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'}

     month_nums = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
                   'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}

     birth_stones = {'jan': 'Garnet', 'feb': 'Amethyst', 'mar': 'Aquamarine', 'apr': 'Diamond',
                     'may': 'Emerald', 'jun': 'Pearl', 'jul': 'Ruby', 'aug': 'Peridot',
                     'sep': 'Sapphire', 'oct': 'Opal', 'nov': 'Topaz', 'dec': 'Turquoise'}

     # Depending on the category get information about month from correct source and return
     pass
 ```

 *Hint*: While you can simply index into the `full_names`, `month_nums`, or `birth_stones` dictionaries using the month as the key, figuring out the season by each month is a little harder. This is why we want you to put it into another function.

2. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.

 ```python
 def perfect_square(num):
     '''
     Input:  Int
     Output: Bool

     Return True if num is a perfect square, e.g. 9 = 3 x 3. Return False if num is not
     a perfect square, 8 isn't any integer multiplied by itself.
     '''
     pass

 def next_perfect_square(num):
     '''
     Input:  Int
     Output: Int

     Ex: next_perfect_square(10) --> -1
         next_perfect_square(9) ---> 16
         next_perfect_square(25) --> 36
         next_perfect_square(37) --> -1

     Returns the next perfect square (a number that is the square of an integer e.g. 81 = 9 x 9)
     greater than the inputted number. If the inputted number is not a perfect square, return -1.
     (i.e. the inputted number must also be a perfect square).
     '''
     pass
 ```

3. Fill in the following stub code so that the functions operate in the way prescribed by their doc strings.

 ```python
 import random

 def flip_coin():
     '''
     Input:  None
     Output: Str - 'H' for head or 'T' for tail

     Perform an "experiment" using random.random(), return 'H' if result is above .5, 'T' otherwise.
     '''
     pass

 def roll_die():
     '''
     Input:  None
     Output: Int - Between 1 and 6

     Using random.randint(), perform a die roll and return the number that "comes up".
     '''
     pass

 def flip_coin_roll_die(n_times):
     '''
     Input:  Int - number of times to flip a coin and roll a die
     Output: List - of tuples with the outcomes
        of the flips and rolls from each time
     '''
     pass
 ```

### Part 3 - Tying it All Together

For this part of the assignment, you are going to be coding up your own functions from scratch! Most of the time when programming, all we have is a problem. It is then our job to create functions to solve this problem. This may sound daunting, but don't worry, because you've been practicing a lot in the previous sections; you've been getting your mind used to thinking about splitting up problems into smaller parts.

1. Write a function that rolls two sets of dice to model players playing a game with dice. It will accept two arguments, the number of dice to roll for the first player, and the number of dice to roll for the second player. Then, the function will do the following:

 * Model rolling the appropriate number of dice for each player.
 * Sum the total values of the corresponding dice rolls.
 * Print which player rolled the higher total.
 * Return the total sum of each players rolls in a tuple.

 Here's how we would call it:

 ```python
 In [1]: player_rolls = model_dice_rolls(3, 2)
 Player 1 wins!
 In [2]: player_rolls
 Out[2]: (13, 7)
 ```

 Remember, you already have some code that solves part of this problem. Feel free to use whatever code you have already written - that's part of the reason we use functions. Hopefully you're beginning to see the advantages of using functions!

2. Write a function that will calculate the total amount of a dinner bill, given the total before tax, the tax rate, and the tip percentage. Your function will accept these three values as arguments. It will then do the following:

 * Apply the tax rate to the bill total.
 * Apply the tip percentage to the total amount.
 * Return the total amount of bill before and after tip.

 Here's an example of how we would call the function:

 ```python
 In [1]: bill_with_tax, bill_with_tax_and_tip = calc_total_bill(100, 0.10, 0.10)

 In [2]: bill_with_tax_and_tip
 Out[2]: 121.0
 ```
