# Python program to find factors of a number using while loop

print ("Enter the positive integer number: ", end="")
random_number, i = int (input ()), 1

print ("The factors of the ", random_number, "are: ", end="")
while i <= random_number:
    if random_number % i == 0:
        print (i, end=" ")
    i += 1
print (end="\n")




# Python program to find factors of a number using for loop
# # Python program to find factors of a number using for loop
#
# print ("Enter the positive integer number: ", end="")
# random_number = int (input ())
#
# print ("The factors of the ", random_number, "are: ", end="")
# for i in range (1, random_number + 1):
#     if random_number % i == 0:
#         print (i, end=" ")
# print (end="\n")