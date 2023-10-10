import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

def main():
    time1 = time.perf_counter()
    # Normal code
    # func(5)
    # func(3)
    # func(2)

    # Same code using Threads
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    # Calculating Time
    time2 = time.perf_counter()
    print(time2 - time1)

def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # future = executor.submit(func, 3)
        # print(future.result())
        # future = executor.submit(func, 2)
        # print(future.result())
        # future = executor.submit(func, 5)
        # print(future.result())
        l = [3,5,7,2]
        results = executor.map(func, l)
        for result in results:
            print(result)

poolingDemo()