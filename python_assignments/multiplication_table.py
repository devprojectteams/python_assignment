# Multiplication table (from 1 to 10) in Python


user_input = int(input("Enter a number: "))

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 13):
   print(user_input, 'x', i, '=', user_input *i)

