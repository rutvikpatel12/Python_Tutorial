# num=int(input("Entet number: "))

# if(num < 0):
#     print("Number is Negative")
# elif(num == 0):
#     print("Number is Zero")
# else:
#     print("Number is Positive")
# print("Completed")

# Nested If-Else
# num=int(input("Enter Number: "))
# if(num<0):
#     print("Number is negative")
# elif(num>0):
#     if(num<=10):
#         print("Number is between 1-10")
#     elif(num > 10 and num <= 20):
#         print("Number is between 11-20")
#     else:
#         print("Number is greater than 20")
# else:
#     print("Number is zero")


import time
timeset = time.strftime("%H")
# Conevrt String to int
times=int(timeset)

if(times <= 12):
    print("Good Morning Sir")
elif(times > 12 and times <= 16):
    print("Good Afternoon Sir")
elif(times > 16 and times <= 21):
    print("Good Evening Sir")
elif(times > 21 and times <= 24):
    print("Good Night Sir")
else:
    print("Please find Clock Time")