# An example of Counter controlled Loop; print ("The final value is", x)

count = 0
largest_number_so_far = float("-inf")
smallest_number_so_far = float("+inf")

while count < 5:
    num = int(input("Give me a number: "))
    if num > largest_number_so_far:
        largest_number_so_far = num
    if num < smallest_number_so_far:
        smallest_number_so_far = num

    count += 1
print("The largest number is ", largest_number_so_far, "\nThe smallest number is ", smallest_number_so_far)

