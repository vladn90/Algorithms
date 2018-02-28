""" Check if a number is a palindrome, i.e. 12321 is a palindrome number.
"""
import random
from time import time


def is_palnum(n):
    """ Returns True if number is a palindrome, False otherwise.
    Pythonic way.
    """
    return n == int(str(n)[::-1])


def is_palnum_fast(n):
    """ Returns True if number is a palindrome, False otherwise.
    Faster algorithm.
    1) Compare digits from the start of the number to the digits at the end
    of the number.
    2) Increment left index by 1, decrement right index by 1.
    3) Return False if digits are different.
    4) Stop at the middle. Return True.
    """
    num = str(n)
    # initialize left index i and right index j
    i, j = 0, len(num) - 1
    # stop the loop when we reach the middle of the number
    while i < j:
        if num[i] != num[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    t = 10**6  # number of tests

    # testing random numbers
    time1, time2 = 0, 0  # total time for each function
    for i in range(t):
        n = random.randrange(10**6, 10**12)
        start = time()
        result1 = is_palnum(n)
        time1 += time() - start
        start = time()
        result2 = is_palnum_fast(n)
        time2 += time() - start
        if result1 != result2:
            print("Error.")
            print(f"n = {n}")
            print(f"result 1: {result1}")
            print(f"result 2: {result2}")

    print(f"time 1: {time1}")
    print(f"time 2: {time2}")

    # testing palindrome numbers
    time1, time2 = 0, 0  # total time for each function
    for i in range(t):
        n = random.randrange(10**3, 10**6)
        n = int(str(n) + str(n)[::-1])
        start = time()
        result1 = is_palnum(n)
        time1 += time() - start
        start = time()
        result2 = is_palnum_fast(n)
        time2 += time() - start
        if result1 != result2:
            print("Error.")
            print(f"n = {n}")
            print(f"result 1: {result1}")
            print(f"result 2: {result2}")

    print(f"time 1: {time1}")
    print(f"time 2: {time2}")
