def average(a, b):  #Required Arguments  (a and b both are required arguments)
    print("The average is ", (a+b)/2)

average(4, 5)

# There are four types of arguments that we can provide in a function
# 1. Default Arguments
# 2. keyword Arguments
# 3. Variable Arguments
# 4. Required Arguments

def average(a=9, b=1):   #Default Arguments
    print("The average is", (a+b)/2)

average()   #o/p - 5.0
average(3, 6)   #will consider the new values if given
average(4)            #will consider the default value of b
average(b=9)          #will consider the default value of a

# def name(fname, mname="John", lname="Whatson"):
#     print("Hello, ", fname, mname, lname)
#
# name("Amy")

def average(b=9, a=21):    #Keyword Arguments  key=value
    print("The average is ", (a+b)/2)

def average(a, b=9):       #Required Arguments  (a is the only required argument b can be given or not)
    print("The average is ", (a+b)/2)


def average(*numbers):      #Getting the list or array of numbers as the argument
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is: ", sum/len(numbers))
    return sum/len(numbers)

c = average(5, 6)
print(c)

def name(**name):
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "Jones")



