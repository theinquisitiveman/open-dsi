## Write a script that computes the greatest common divisor
## between two user inputted numbers. If you don't know what
## a greatest common divisor is, check out this link.
## Things to think about:

# How do you get two numbers from the user?
# Where should you start your search for the GCD?
# Where/how should you end your search?

x = int(input("Let's find the greatest common divisor between two numbers, type in a number: "))
y = int(input("Type in another number: "))
print("The divisors for this number are: ")

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
