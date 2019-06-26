## Write a script that computes and prints all of the divisors
## of a user inputted number. If you don't know what a divisor
## is or need a review, check out this link. Things to think about:
## How do you determine if a single number is a divisor of another?
## How do you do this multiple times (Hint: it involves a while loop)?
## When do you stop the loop?

n = int(input("Let's find the divisor, type in a number: "))
print("The divisors for this number are: ")

#def divisor(n):
#    for x in range(1, n+1):
#        if n % x == 0:
#            print(x)

def divisor(n):
    d = 1
    while d <= n:
        if n % d == 0:
            print(d)
        d += 1

divisor(n)
