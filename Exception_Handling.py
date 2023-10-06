# a = input("Enter number: ")

# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print("Invalid Input!")


# try:
#     num=int(input("Enter an integer: "))
#     a=[6,3]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer")

# except IndexError:
#     print("Index Error")


# Finally Keyword
# try:
#     l=[1,5,6,2,4]
#     num=int(input("Enter index: "))
#     print(l[num])
# except:
#     print("Some error occurred")
# finally:
#     print("Call Finally Block")

def func1():
    try:
        l=[1,5,6,2,4]
        num=int(input("Enter index: "))
        print(l[num])
        return 1

    except:
        print("Some error occurred")
        return 0

    finally:
        print("Call Finally Block")
    # print("Call Finally Block")      # not print under function

x = func1()
print(x)