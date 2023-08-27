names = "Harshada, Shrishti"
print(names[0:8])
print(names[0: 7])
print(names[19: 0])

fruit = "Mango"
mangoLen = len(fruit)

print(mangoLen)
print(fruit[0:4])
print(fruit[:4])
print(fruit[:])
print(fruit[0:])
print(fruit[:5])

# python interprets it as fruit[0:len(fruit)-3]
print(fruit[0:-3])

# (fruit[-1:len(fruit)-3])
print(fruit[-1:-3])  #4:2 not sensible
print(fruit[-3:-1])  #2:4  makes sense   (including 2 but not including 4) its 2,3


# Quick Quiz:
nm = "Harry"
print(nm[-4:-2])   #from (5-4 = 1) to (5-2 = 3) but 1 included and 3 not included.

