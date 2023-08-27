a = "Harry  !!!!!!!!!!"
print(len(a))
print(a.upper())

print(a)


# Strings are immutable

#upper() and lower() methods to convert strings to lower and upper case
u = a.upper()
l = a.lower()

print(u)
print(l)

#rstrip() to strip the unwanted characters in the string
print(a.rstrip("!"))

#replace the old string with a new string that is parsed in the method
print(a.replace("Harry", "John"))

#split method splits the string in parts as per mentioned in the method
print(a.split(" "))

#capitalize method capitalize the first letter of the string
blogHeading = "introduction tO js"
print(blogHeading.capitalize())

#center() brings the string to the center as per the number given in the method by the user
str1 = "Welcome to the console!"
print(str1.center(50))
print(len(str1.center(50)))
print(len(str1))

#count() is used to count the number of occurences of the given string in the actual string
b = "Harry !!!!!!!!!! Harry"
print(b.count("Harry"))

#endswith() is used to check whether the string ends with the specified thing which is given by the user in the method
print(str1.endswith("!", 4, 9))

print(str1.endswith("!!!"))
print(str1.endswith("!"))

#find() is used to find the given string in the method in the actual string and returns the position of the string if
#its present in the actual string
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("Welcome"))

#isalnum() is used to check whether the string is having the alphabets and numbers in the string or not.
str1 = "WelcometotheConsole78"
print(str1.isalnum())

#isapla() just checks the alphabets in the string and returns true if only alphabest are present in the string
print(str1.isalpha())

a = "Harshada"
b = a.lower()

print(b)

#islower() checks if the string is in lowercase or not
print(a.islower())
print(b.islower())

# isprintable() checks if the string is printable or not and returns true if it is printable and false if it is not
str1 = "We wish you a many Christmas\n!"
print(str1.isprintable())

# isspace returns true only if the string contains the white spaces
str1 = "Welcome  to  the  Console"
str2 = "    "
print(str1.isspace())
print(str2.isspace())

# istitle() returns true only if the first letter of each word of the string is capitalize
str1 = "welcome to the console"
str2 = "Welcome To The Console"
print(str1.istitle())
print(str2.istitle())

# startswith() checks if the string starts with the given string by the user
str1 = "Python is an interpreted language"
print(str1.startswith("Python"))
print(str1.startswith("language"))

# swapcase() swaps the case(upper or lower) of the string to the opposite
str1 = "python is an interpreted language"
print(str1.swapcase())

# title() returns the string by making all the first letters of all the words in the string to caps
str1 = "He's name is Dan. He is an honest man."
print(str1.title())




