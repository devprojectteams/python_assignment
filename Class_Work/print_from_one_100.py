number = 1
count = 0
# while number <= 100:
# print(number)
for i in range(1, 101):
    # print(i)

    if number % 15 == 0:
        print("FIZZBUZZ")
    elif number % 3 == 0:
        print("Fizz")

    elif number % 5 == 0:
        print("Buzz ")

    else:
        print(number)

    number += 1

    # # number += 1
