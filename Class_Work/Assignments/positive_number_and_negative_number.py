count = 0
total = 0.0
positive_count = 0
negative_count = 0
negative_number = 0
positive_number = 0
#average = 0
number = int(input("Input some integers to calculate their sum and average or Input 0 to exit: "))
while number != 0:

    if number > 0:
        positive_number = positive_number + number
        positive_count +=1

    if number < 0:
        negative_number += number
        negative_count += 1


    number = int(input("Input some integers to calculate their sum and average or Input 0 to exit: "))
    count = count +1
    total = negative_number + positive_number
    average = float(total / count)

print(f"the number of positive is {positive_count}")
print(f"the number of negative is  {negative_count}")
print(" Sum of the above numbers are: ", total)
print("Average of the above numbers are: ", average)