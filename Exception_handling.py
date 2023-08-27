# a = input("Enter the number : ")
# print("Multiplication table of {} is :  ".format(a))


#
# print("Some important lines of code")
# print("End of program")

# try:
#     for i in range(1, 11):
#         print(f"{int(a)} X {i} = {int(a) * i}")
#
# except Exception as e:
#     print(e)

# else:
#     print("Some important lines of code")
#     print("End of program")

try:
    num = int(input("Enter the number : "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index error")
else:
    print("The number is ", num)

