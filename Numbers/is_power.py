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
    """ Returns True n is a power of x,
    False otherwise.

    input: int n >= 2
           int x >= 2
    """
    while n % x == 0:
        n //= x
    return n == 1


def is_power(n, x):
    """ Returns True n is a power of x,
    False otherwise. Improved algorithm.

    input: int n >= 0
           int x >= 0
    """
    # validating input
    if n < 0 or x < 0 or (n == 0 and x > 0):
        raise Exception("Wrong input. Use int n >= 1, int x >= 0.")

    # 0 ^ (any int n) = 0
    if n == 0 and x == 0:
        return True

    # 0 ^ 0 = 1
    if n == 1 and x == 0:
        return True

    # 1 ^ (any int) = 1
    if n >= 1 and x == 1:
        return True

    # for any int x > 0, x ^ 0 = 1
    if n == 1 and x > 0:
        return True

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


# testing improved algorithm
if __name__ == "__main__":
    while True:
        x = random.randrange(2, 10**6)
        k = random.randrange(2, 10**3)
        n = x ** k
        if not is_power(n, x):
            print("Error.")
            print(f"number n = {n}")
            print(f"power x = {x}")
            break
        else:
            print("OK")
            print(f"number n = {n}")
            print(f"power x = {x}")
