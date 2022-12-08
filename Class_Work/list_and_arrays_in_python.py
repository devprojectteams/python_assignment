from array import *
x = array('i',[5,6,5,7])
x.append(45)
print(len(x))


numbers = [0,1,2,3,4,5,6,7,8,9,10]
# numbers.reverse()
print(numbers[::-2])
print(numbers[-4:-11:-2])

string = "mississippi is the longest river"
# print(string[17:11:-1])
# print(string[0], string[17])
for char in string:
    print(char)

sentence = ['obi is a boy', 'Ada is a girl']
print(sentence[0])
print(sentence[1])
print(sentence[0][0:3])
print(sentence[1][9:13])
print(sentence[0][9:12])
sentence.append("screen")
sentence.insert(1,"screen")
print(sentence)






# import numpy as np
#
# x = np.array([2,4,6,8,10,12])
# print(x/2)
#
# new = []
# y = [2,4,6,8,19,12]
# for val in y:
#     new.append(val/2)
#     # print(y/2)
