# for i in []:
#     print(i)
# else:
#     print("Sorry no i")

# for x in range(5):
#     print("Iteration no {} in for loop".format(x+1))
# else:
#     print("Else block in loop")
# print("Out of loop")

for i in []:
    print(i)
    if i == 0:
        break
else:
    print("Sorry no i")

for x in range(5):
    print("Iteration no {} in for loop".format(x+1))

else:
    print("Print else block in loop")

print("Out of loop")