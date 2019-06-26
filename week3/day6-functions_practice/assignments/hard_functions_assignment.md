# Hard Functions Exercise 2

# Instructions

Tonight you're going to be writing a program that does something cool! You're going to write a script that allows two people to play tic-tac-toe! This is a much more involved problem than any you've seen in this class so far. In general, you should be thinking about how to break up your solution into smaller parts as you write it. In addition, you should be giving all your functions good names as you write them.

The assignment will give suggestions on how to write this program. Remember, though, that there's always more than one solution to any programming problem. So, if you want to do something that's not suggested by the assignment, by all means give it a try! If you want to talk with someone about what you're thinking, grab an instructor or one of your peers. Frequently, talking about the problem will help you get a better handle on it and how to solve it.

Within each of these steps, and frequently between them, you will likely need to do some debugging. One way to do this is by trying to play your game as you implement different parts of it. If something isn't working, you'll get error messages as to why. In addition, Python will tell you where it ran into the error and give you the **stack trace** leading up to that line getting executed. Try reading these error messages and learning how to read stack traces - it is a necessary skill for a programmer to have, and one that can only be developed via practice. Later in the course, you will learn about other methods of debugging. However, learning these basic skills when your programs are smaller is a great way to make sure you have a good debugging foundation.

There are far too many programmers who can't debug on this fundamental level: reading an error message and thinking about/reading your code -> figuring out how that error could be produced -> fixing it -> starting over. You're not going to be one of those programmers. Debugging like this is also a great way to get very familiar with any language.

# Assignment Suggestions

### Part 1: Getting Started

One of the first things I always do when writing a script is start a main block. Inside of the main block, you'll be calling the function that is going to run your game. This puts you in the mindset of programming top down. It also makes it easy to test your code.

What are you going to call the function that runs your program? It should be a name that describes what it does. Other than that, you have free reign.

### Part 2: Set Up the Game

A simple way to store a tic-tac-toe board is with a list of three lists, each three elements long. You'll want to initialize the board to something in the beginning - I suggest that you have the coordinates of the board squares to begin with. This will make it easier for users to specify where they want to play.

It also makes sense to print this initial board. Since you'll probably want to print the board after any play is made, it would make sense to make a function that prints the board to the screen in a friendly way. Here's what I'm imagining the solution board to look like initially:

```
[(0, 0), (1, 0), (2, 0)]
[(0, 1), (1, 1), (2, 1)]
[(0, 2), (1, 2), (2, 2)]
```

It stores the location coordinates as tuples so that the users will know what squares they can play in and how to reference them.

### Part 3: Commence the Game

Now, you're going to want to repeatedly ask each player where they want to play. What do we do when we have to do the same thing over and over? We use a loop! So, what's going into this loop? You're going to want to allow a turn to be played based off the state of the board. One difficult part of this is making a single function that will allow either player to play.

One way of handling this is by passing the turn number that the game is on to the function, along with the state of the board. The first line of the function then determines which player's turn it is with some intelligent math: `player = turn % 2 + 1`. You're welcome to figure out what this line is doing and use it in your solution, or you can think of another way! It's your journey.

### Part 4: Accept a Play

Now that we've started the game and determined a way to figure out who's turn it is, you're script is going to have to allow a player to specify where they want to play. One way to do this is by accepting coordinates of the square, similar to how we stored the coordinates when we initialized the board. So, a player only has to look at the coordinate they want to play in, and enter the numbers associated with that square, separated by a comma. Here's an example of how this might look:

```
[(0, 0), (1, 0), (2, 0)]
[(0, 1), (1, 1), (2, 1)]
[(0, 2), (1, 2), (2, 2)]
Player 1 ( X ), where will you play? 0, 0
[' X ', (1, 0), (2, 0)]
[(0, 1), (1, 1), (2, 1)]
[(0, 2), (1, 2), (2, 2)]
```

### Part 5: Check for A Winner

At the end of each turn, your script will have to determine if the most recent play resulted in a win. If it did, the player that just played will be declared the winner, the game will be over, and the script will terminate. If a winner is not found, play will continue. Keep in mind that there are 8 different ways for a player to get three in a row. The function you write to solve this part of the problem will have to implement a lot of logic, and will most likely be the crux of building this game. **Hint**: One way to potentially make this part easier is by using the built-in `all()` function.

Once this functionality is implemented and working, the end of the game might look something like this:

```
[' X ', ' X ', (2, 0)]
[(0, 1), ' O ', ' O ']
[(0, 2), (1, 2), (2, 2)]
Player 1 ( X ), where will you play? 2, 0
[' X ', ' X ', ' X ']
[(0, 1), ' O ', ' O ']
[(0, 2), (1, 2), (2, 2)]
Player 1 Wins!!
```

### Part 6: Tie Game

There is a distinct chance that a tie will occur in the game. If this happens, your script should be aware. If all of the squares have been filled in, and there is no winner, a tie should be declared. Take a look at what the solution looks like when the game ends and a tie happens:

```
[' X ', ' O ', ' X ']
[' X ', ' O ', ' O ']
[' O ', ' X ', (2, 2)]
Player 1 ( X ), where will you play? 2, 2
[' X ', ' O ', ' X ']
[' X ', ' O ', ' O ']
[' O ', ' X ', ' X ']
Game resulted in a tie...like usual.
```

### Part 7: Check for Good Input

No matter how you implemented your game, you never know how users of your script will interact with it. What happens if they enter a square that is off the grid, outside the range of the board? What about if they don't enter properly formatted input? What if they try to play in a square that has already been played in? Can you make your script robust to these possibilities? Try to continually break your solution. It's both fun and can reveal bugs that you hadn't thought of before. If you can't find a way to break it, call over an instructor and let them know. If they can't break it, you're basically done.

At this point, you could work on making what is printed to the screen prettier, or adding doc strings to your functions (always a good idea). You could also just relax and play a game of tic-tac-toe. You've earned it.
