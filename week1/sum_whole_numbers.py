my_num = int(input("Enter a number to find the sum up to: "))
sum_result = 0
current = 1

while current <= my_num:
    sum_result += current
    current +=1
print(sum_result)
