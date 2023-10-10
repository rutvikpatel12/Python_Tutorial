from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")
print(fx(5))
print("done for 5")
print(fx(7))
print("done for 7")

print(fx(20))
print("done for 20")
print(fx(5))
print("done for 5")
print(fx(7))
print("done for 7")
print(fx(42))
print("done for 42")
