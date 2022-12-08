import string

user_input = input("Enter the word to decide ")
key = int(input("What key you would like to use "))

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase
decoded_lower_letters = lower_letters[key:] + lower_letters[:key]
decoded_upper_letters = upper_letters[key:] + upper_letters[:key]



import string

letters = lower_letters + upper_letters + string.whitespace
decoded_letters = decoded_lower_letters + decoded_upper_letters + string.whitespace
encoded = user_input.translate(str.maketrans(letters,decoded_letters))
decoded = encoded.translate(str.maketrans(decoded_letters,letters))

print(encoded)
print(decoded)
