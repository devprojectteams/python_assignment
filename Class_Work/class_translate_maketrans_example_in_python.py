hello = "hello world"
bin_ = "101100011001011110"
print(bin_.replace("i", "x").replace("0", "1").replace("x", "0"))
print(bin_.translate(str.maketrans("01", "10")))
print((str.maketrans("01", "10")))

bin_ = "10110001***100!!!1011110#78"
print(bin_.translate(str.maketrans("01", "10", "8#!*")))
