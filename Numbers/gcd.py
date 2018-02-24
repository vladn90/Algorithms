""" Euclidean algorithm to find greatest common divisor (GCD) for two numbers.
https://en.wikipedia.org/wiki/Greatest_common_divisor#Using_Euclid's_algorithm

Algorithm description(pseudocode):
1) Find remainder of a // b, i.e. a % b
2) If remainder = 0, return int b.
3) Else repeat from step 2 for a = b, b = remainder.
"""


import math
import random


def gcd_1(a, b):
    """ Recursive implementation.
    """
    rem = a % b
    if rem == 0:
        return b
    return gcd_1(b, rem)


def gcd_2(a, b):
    """ Iterative implementation.
    """
    rem = a % b
    while rem != 0:
        a, b = b, rem
        rem = a % b
    return b


# stress testing Python implementations against math.gcd()
if __name__ == "__main__":
    while True:
        a = random.randrange(10**3, 10**18)
        b = random.randrange(10**3, 10**18)
        res_1 = gcd_1(a, b)
        res_2 = gcd_2(a, b)
        res_3 = math.gcd(a, b)
        if res_1 == res_2 == res_3:
            print("OK")
            print(res_1)
        else:
            print("Different values.")
            print(f"a = {a}")
            print(f"b = {b}")
            print(f"res_1: {res_1}")
            print(f"res_2: {res_2}")
            print(f"res_3: {res_3}")
            break
