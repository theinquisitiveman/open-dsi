# Write a script that takes two user inputted
# numbers and prints "The first number is larger" or
# "The second number is larger" depending on which is larger.
# (Hint: you'll need to use input() twice.)

user_input_1 = int(input("Give me your first number: "))
user_input_2 = int(input("Give me your second number: "))

if user_input_1 > user_input_2:
    print("The first number is larger")
else:
    print("The second number is larger")
