# import os
#
# print("Hello World from...")
# os.system("Python --version")

x = int(input("Enter the integer :  "))

match(x):
    case 0:
        print("X is zero")
    case 4 if x% 2 == 0:
        print("x % 2 == 0 and case is 4")
    case _ if x < 10:   #for default case _ is used
        print("x is < 10")

    case _:
        print(x)