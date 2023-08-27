l = [1, 2, 3, 4, 6]
# print(l)

l.append(2)
print(l)

#l.sort
l = [3, 2, 34, 5, 45, 6]
# l.sort()
# print(l)
#
# l.sort(reverse = True)
# print(l)

l.reverse()
# print(l)

# print(l.index(2))

# print(l.count(2))

m = l   #m is a reference of l l changes along with m
# m[0] = 0
# print(l)
# print(m)
m = l.copy()
m[0] = 0
print(l)
print(m)

l.insert(1, 9899)
print(l)

m = [900, 1000, 1100]
l.extend(m)
print(l)

k = l+m
print(k)
