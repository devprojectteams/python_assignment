#input first,Second and third number
num1=int(input("Enter First Number"))
num2=int(input("Enter Second Number"))
num3=int(input("Enter Third Number"))

if (num1 < num2 and num1 < num3):
    print("The Smallest number is", num1)

elif (num2 < num1 and num2 < num3):
    print("The Smallest number is", num2)
else:
    print("The Smallest number is", num3)



#Check if first number is greater than rest of the two numbers.
if (num1> num2 and num1> num3):
    print("The Largest number is", num1)
#Check if Second number is greater than rest of the two numbers.
elif (num2 > num1 and num2> num3):
    print ("The Largest number is", num2)
else:
    print ("The Largest number is", num3)

    if (num1 > num2 and num1 < num3):
        print("The Larger number is", num1)
    # Check if Second number is greater than rest of the two numbers.
    elif (num2 > num1 and num2 < num3):
        print("The Larger number is", num2)
    else:
        print("The Larger number is", num3)

