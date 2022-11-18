
count = 0
largest_number_so_far = float("+inf")
smallest_number_so_far = float("-inf")
larger_number = float("+inf")
while count < 5:

    number = int(input("Enter a number: "))
    if  number > largest_number_so_far:
        largest_number_so_far = number
    if largest_number_so_far < smallest_number_so_far:
        smallest_number_so_far = number

    count = count + 1

print()
print("the largest number is ", largest_number_so_far)
print("the smallest number is ", smallest_number_so_far)