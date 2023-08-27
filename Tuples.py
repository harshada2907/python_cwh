tup = (1, 5, 6)
# print(type(tup))
# print(tup)

tup = (1)
print(type(tup), tup)
# will give the class as int since one element is there in the list
# to make it tuple put a comma after the element

tup = (1, )

# tuples are immutable
# tup[0] = 90
# print(type(tup), tup)

tup = (1, 2, 76, 342, 32, "green", True)
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])

# print(len(tup))

# if 3421 in tup:
#     print("Yes 342 is present in this tuple")


tup2 = tup[1:4]
print(tup2)

