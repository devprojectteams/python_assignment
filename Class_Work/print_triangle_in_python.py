# to print a triangle:
# hello ="Hello there!!!"

for i in range(1, 22, 2):
    a = "*" * i
    asterisks = "*" * i
    h = "*" * i
    v = "*" * i
    print(a.ljust(21), asterisks.center(21), h.rjust(21), v.center(21))

for e in range(1, 22, 2):
    a = "->" * e
    asterisks = "*" * e
    h = "*" * e
    v = "*" * e
    print(a.ljust(21), asterisks.center(21), h.rjust(21), v.center(21))




#for i in range(1, 22, 2):
 #asterisks = "*" * i
 #print(asterisks.center(21))