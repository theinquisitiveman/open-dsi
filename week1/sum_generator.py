#Write a script that computes the sum from 0 to a user inputted number.
# This time though, start at the user inputted number and work down.
# This answer will look very much like the example above,
# you'll just need to change a couple of things.

n = int(input("Give me a number: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))
