def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num-1)

print(fact(4))

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

# nt = int(input("Enter the number of terms you want : "))
# if nt <= 0:
#     print("Please enter a positive number ")
#
# else:
#     for i in range(nt):
#         print(fibo(i))

# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
#
#
# nterms = int(input("Enter the number of terms you want : "))
#
# if nterms <= 0:
#     print("Please enter the positive number")
#
# else:
#     for term in range(nterms):
#         print(fibo(term))

nterms = int(input("Enter the number of terms you want : "))

f1 = 0
f2 = 1
count = 0

if nterms <= 0:
    print("Please enter the positive number")

else:
    while count < nterms:
        print(f1)
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        count += 1
