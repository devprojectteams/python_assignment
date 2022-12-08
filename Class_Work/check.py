count = 0
number = int(input("enter a number "))
largest_number_so_far = number
smallest_number_so_far = number

while count < 5:

    number = int(input("Enter a number: "))
    if number > largest_number_so_far:
        largest_number_so_far = number
    if number < smallest_number_so_far:
        smallest_number_so_far = number

    count = count + 1

print()
print("the largest number is ", largest_number_so_far)
print("the smallest number is ", smallest_number_so_far)