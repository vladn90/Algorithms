""" Algorithm to determine if n is a power of x.
Simple algorithm description(pseudocode):
1) Keep dividing int n by int x while remainder is 0, i.e. n % x == 0.
2) Compare resulting int n and 1.
3) If n == 1, then n is a power of x.

Improved algorithm description(pseudocode):
1) Create a set of endings(last digits) for x to the power of k,
for k = 1, 2, 3, 4, etc.
    For example, for x = 2, endings set will look like this {2, 4, 8, 16},
    because 2^1 = 2, 2^2 = 4, 2^3 = 8, 2^4 = 16, 2^5 = 32, 2^6 = 64, etc.
    We can see that after a certain power k, endings start repeating themselves,
    thus we only need to find endings until we encounter a repetition.
2) Keep dividing n by x while remainder is 0 and while we can find
last digit of n in set of endings.
2) Compare resulting int n and 1.
3) If n == 1, then n is a power of x.
Improved algorithm also takes in account n = 1 and x = 1 or x = 0.
"""


import random


def is_power_simple(n, x):
    """ Returns True n is a power of x, False otherwise.

    input: int n >= 2, int x >= 2
    output: int
    """
    # validating input
    if n < 2 or x < 2:
        raise Exception("input should be: int n >= 2, int x >= 2")

    # checking if n is a power of x
    while n % x == 0:
        n //= x
    return n == 1


def is_power(n, x):
    """ Returns True n is a power of x, False otherwise. Improved algorithm.

    input: int n >= 2, int x >= 2
    output: int
    """
    # validating input
    if n < 2 or x < 2:
        raise Exception("input should be: int n >= 2, int x >= 2")

    # creating a set of last digits for power of x
    endings = set()
    curr = x % 10  # last digit of x to the current power, starting from power 1
    # break out of the loop when digits start repeating
    while curr not in endings:
        endings.add(curr)
        curr = (curr * x) % 10

    # checking if n is a power of x
    while n % x == 0 and n % 10 in endings:
        n //= x
    return n == 1


def is_power_simple_2(n, x):
    """ Returns power as int if n is a power of x, returns -1 otherwise.

    input: int n >= 2, int x >= 2
    output: int
    """
    # validating input
    if n < 2 or x < 2:
        raise Exception("input should be: int n >= 2, int x >= 2")

    # checking if n is a power of x
    p = 0  # power counter
    while n % x == 0:
        p += 1
        n //= x
    return p if n == 1 else -1


def is_power_2(n, x):
    """ Returns power as int if n is a power of x, returns -1 otherwise.

    input: int n >= 2, int x >= 2
    output: int
    """
    # validating input
    if n < 2 or x < 2:
        raise Exception("input should be: int n >= 2, int x >= 2")

    # creating a set of last digits for power of x
    endings = set()
    curr = x % 10  # last digit of x to the current power, starting from power 1
    # break out of the loop when digits start repeating
    while curr not in endings:
        endings.add(curr)
        curr = (curr * x) % 10

    # checking if n is a power of x
    p = 0  # power counter
    while n % x == 0 and n % 10 in endings:
        p += 1
        n //= x
    return p if n == 1 else -1


def test_value(is_power, t):
    """ Testing is_power functions that return value of power.
    """
    for i in range(t):
        x = random.randrange(2, 10**6)
        k = random.randrange(2, 10**3)
        n = x ** k
        if is_power(n, x) == k:
            print("OK")
            print(f"x = {x}")
            print(f"k = {k}")
            print(f"x ^ k = {n}")
            print()
        else:
            print("Values that crashed the calculation are below.")
            print(f"x = {x}")
            print(f"k = {k}")
            print(f"x ^ k = {n}")
            raise Exception("Result is wrong.")


def test_boolean(is_power, t):
    """ Testing is_power functions that return boolean.
    """
    for i in range(t):
        x = random.randrange(2, 10**6)
        k = random.randrange(2, 10**3)
        n = x ** k
        if is_power(n, x):
            print("OK")
            print(f"x = {x}")
            print(f"k = {k}")
            print(f"x ^ k = {n}")
            print()
        else:
            print("Values that crashed the calculation are below.")
            print(f"x = {x}")
            print(f"k = {k}")
            print(f"x ^ k = {n}")
            raise Exception("Result is wrong.")


# testing all algorithms
if __name__ == "__main__":
    t = 10**3  # number of tests for each function
    test_boolean(is_power_simple, t)
    test_boolean(is_power, t)
    test_value(is_power_simple_2, t)
    test_value(is_power_2, t)
