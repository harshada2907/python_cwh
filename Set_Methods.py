# s1= {1, 2, 5, 6}
# s2 = {3, 6, 7}
#
# print(s1.union(s2))
# print(s1, s2)
# s1.update(s2)
# print(s1, s2)
#
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
#
# cities.intersection_update(cities2)
# print(cities)



# cities3 = cities.union(cities2)
# print(cities3)
#
# cities3 = cities.intersection(cities2)
# print(cities3)
#
# cities.intersection_update(cities2)
# print(cities)
#
# cities.union_update(cities2)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# cities3 = cities.symmetric_difference(cities2)
# print(cities3)

# cities ={"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities2 = {"Seoul", "Kabul", "Delhi"}
#
# cities3 = cities.difference(cities2)
# print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.isdisjoint(cities2))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}

print(cities.issuperset(cities2))

cities3 = {"Seoul", "Madrid", "Kabul"}
print(cities.issuperset(cities3))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))

# cities.add("Helsinki")
# print(cities)
#
# cities.remove("Tokyo")
# print(cities)

# cities.remove("Seoul")
# print(cities)

# cities.discard("Seoul")
# print(cities)
#
# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# items = cities.pop()
# print(items)
#
# del(cities)
# print(cities)

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.clear()
# print(cities)

info = {"Carla", 19, False, 5.9}


if "Carla" in info:
    print("Carla is present")
else:
    print("Carla is absent")