import time

# t = time.strftime("%H:%M:%S")
# print(timestamp)

timestamp = time.strftime("%H")
# print(timestamp)
#
# timestamp = time.strftime("%M")
# print(timestamp)
#
# timestamp = time.strftime("%S")
# print(timestamp)

hour = int(timestamp)
hour = int(input("Enter the hour : "))

if(hour > 0 and hour < 12):
    print("Good Morning Sir")

elif(hour > 12 and hour < 17):
    print("Good Afternoon")

else:
    print("Good Evening")