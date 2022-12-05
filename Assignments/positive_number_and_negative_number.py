number = int(input("Input some integers to calculate their sum and average. Input 0 to exit."))

count = 0
total = 0.0
number = 1
negative_number = 0
positive_number = 0

while number != 0:
    number = int(input())
    total = total + number

if number > 0:
    print(positive_number)
# elif number == 0:
#     print("Zero")
elif number < 0:
    print(negative_number)
#
# elif count == 0:
#     print("Input some numbers")
#     count += 1

else:
    print(" Sum of the above numbers are: ",  total)
    print("Average of the above numbers are: ", total / (count - 1))
    print(f"the number of positive is { positive_number}")
    print(f"the number of negative is  {negative_number}")