# Live Coding: Password Checker and Suggestor

Last class we discussed functions in depth.  Functions are essential tools for developing programs of any real complexity, as they allow us to build small components that can work together to accomplish higher level tasks.

Today we will demo how this works out in practice by building a moderately complex program from scratch.

## Specification

We want to build a password checker and suggester.

Suppose we have a situation where we need to supply a new password (a password is just a string), and the password must satisfy a few rules:

  - The password must contain a lower case character.
  - The password must contain and upper case character.
  - The password must contain a digit.
  - The password must contain one of the following symbols: "^!#$?-@".

Our application should be a command line tool which consumes a string and, if it is not a valid password, returns a suggested alternative password that is valid:

```
$ python check-password.py 'moshi'
How about this:  ^^0Shi
```

Here's another example:

```
$ python check-password.py 'swimswim'
How about this:  5W!mswim
```

If we already supplied a valid password, our application should return it unchanged:

```
$ python check-password.py 'Sk8b0ard!ing'
Password is OK!
```

Occasionally, it may be impossible to find a substitution that works.  Our app should inform us of this situation:

```
$ python check-password.py 'coffee'
Warning: Could not find a substitution that works!
```

## Tips

### Command Line Arguments

To read arguments from the command line in your program, you can use the `sys` module.

```
$ echo command-line-args.py
import sys
print(sys.argv)
$ python command-line-args.py 'hi' 'there' '100'
['command-line-args.py', 'hi', 'there', '100']
```

Notice that these always enter our program as *strings*.

### String Replacement

To replace within a sting, use the `replace` method

```
$ "Matt is cool!".replace('t', '7')
"Ma77 is cool!"
```

To replace only the first occurrence of a substring:

```
$ "Matt is cool!".replace('t', '7', 1)
"Ma7t is cool!"
```
