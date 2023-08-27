marks = [3, 5, 6]
print(marks)
print(type(marks))


# lists are ordered collection of data
# store multiple values i a single variable
# lists are mutable


# print(marks[0])
# print(marks[1])
# print(marks[2])
#
# for mark in marks:
#     print(mark, end=', ')
#
marks = [3, 5, 6, "Harshada", True, 4.5, 5, 6, 6, 3, 2, 0]
#
# for i in l:
#     print(i)

# print(marks[-3])   #len(marks)-3 = 5-3 = 2  (marks[2] = Harshada)

# if "Harshada" in marks:
#     print("Yes")
# else:
#     print("No")

# if "6" in marks:
#     print("Yes")
# else:
#     print("No")

# if "ary" in "Harry":
#     print("Yes")

# Same thing applies for string as well


#To print the entire list
for mark in marks:
    print(mark, end = ", ")

print(marks[:], end = ", ")

print(marks[1:8:2])
print(marks[1:8:3])

lst = [i for i in range(4)]
print(lst)

lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)



