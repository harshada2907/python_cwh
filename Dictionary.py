# dic = {"Harry":"Human Being", "Spoon":"Object"}
# print(dic["Harry"])

# dic = {
#     344: "Harry",
#     56: "Shubham",
#     678: "Harshada",
#     567: "Neha"
# }
# print(dic[567])

info = {"name":"Karan", "age":19, "eligible": True }
# print(info)

# print(info["name"])
# print(info.get("eligible"))

# print(info.keys())
# print(info.values())
print(info.items())

# for key in info.keys():
#     print(key)
#
# for key in info.keys():
#     print(info[key])
#
# for key in info.keys():
#     print(f"The value corresponding to {key} is {info[key]}")

for key, value in info.items():
    print(f"The value corresponding to {key} is {info[key]}")