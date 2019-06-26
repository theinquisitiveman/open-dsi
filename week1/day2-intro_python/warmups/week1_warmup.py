import random

y = random.randint(1,100)
x = int(input("Please enter a number 1 and 100: "))
count = 1

while x != y:
    if x > y:
        print("You are too high.")
    elif x < y:
        print("You are too low.")
    x = int(input("Please enter another number: "))
    count += 1
print("You are correct! That only took " + str(count) + " guesses!")
