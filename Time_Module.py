import time

# def usingWhile():
#     i = 0
#     while i<500:
#         i = i+1
#         print(i)

# def usingFor():
#     for i in range(500):
#         print(i)

# init = time.time()
# usingFor()
# t1 = time.time() - init
# init = time.time()
# usingWhile()
# print(time.time() - init)
# print(t1)

# --- sleep Method
# print(3)
# time.sleep(2)
# print("This printed after 2 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)

print(formatted_time)
