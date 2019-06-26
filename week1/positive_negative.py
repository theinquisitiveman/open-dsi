user_input = int(input("Type in a number to see if it is positive, negative, or zero: "))
answer = 0

if user_input == 0:
    print ("This is zero")
elif user_input % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
