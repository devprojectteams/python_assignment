# An example of Counter controlled Loop; print ("The final value is", x)

count = 0

largest_number_so_far = 0
smallest_number_so_far = 0
second_larger_number = 0
second_smaller_number = 0

while count < 5:
    user_input = int(input("Enter a number: "))

    if user_input > largest_number_so_far and second_smaller_number:
        second_larger_number = largest_number_so_far
        largest_number_so_far = user_input

    elif user_input < second_larger_number and second_smaller_number > smallest_number_so_far:
        second_larger_number = largest_number_so_far
        largest_number_so_far = user_input

    if user_input < smallest_number_so_far:
        user_input = smallest_number_so_far

    count += 1

print("The largest number is ", largest_number_so_far, "\nThe larger number is ", "", second_larger_number)
print("The smallest number is ", smallest_number_so_far)
