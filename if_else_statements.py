# a = int(input("Enter your age : "))
#
# print("Your age is ", +a)
#
# print(a > 18)
# print(a < 18)
# print(a == 18)
# print(a != 18)
#
# if a > 18:
#     print("You can drive")
# else:
#     print("You cannot drive")

# applePrice = 210
# budget = int(input("Enter your budget: "))
#
# if applePrice <= budget:
#     print("Alexa, add 1kg apples to the cart")-
# else:
#     print("Alexa, do not add apples to the cart")

# num = int(input("Enter the integer : "))
# if num < 0:
#     print("Number is negative")
# elif num == 0:
#     print("Number is zero")
# else:
#     print("Number is positive")

num = int(input("Enter the number : "))

if num < 0:
    print("Number is negative")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")