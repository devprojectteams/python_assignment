# An example of Counter controlled Loop; print ("The final value is", x)

count = 0

largest_number_so_far = float("-inf")
smallest_number_so_far = float("+inf")
second_larger_number = float("inf")


while count < 5:
    user_input = int(input("Enter a number: "))

    if user_input > largest_number_so_far:
        second_larger_number = largest_number_so_far
        largest_number_so_far = user_input

    if largest_number_so_far > user_input > second_larger_number:
        second_larger_number = user_input

    if user_input < smallest_number_so_far:
        smallest_number_so_far = user_input

    count += 1

    print("The largest number is ", largest_number_so_far, "\nThe second largest number is ", "", second_larger_number)
    print("The smallest number is ", smallest_number_so_far)
