# Duplicate sets in list of sets
# Using Counter() + count() + frozenset() + loop
# from collections import Counter


test_list = [{2, 3, 9, 12, 16, 4, 2, 3}, {2, 3, 21, 4,19, 18, 12}]


print("The original list is : " + str(test_list))

counter = 0


def Counter():
    pass


freqs = Counter()

res = []
for key, val in freqs.items():


    if val > 1:
        res.append(key)

print("Duplicate sets list : " + str(res))
