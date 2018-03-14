""" Different algorithms to check if n is a power of 4.
"""
import random


def is_power_four_1(n):
    """ Returns True if n is a power of 4, False otherwise.
    Algorithm decription:
    1) Divide n by 4 while remainder == 0.
    2) If last n == 1, then n is a power of 4.
    Time complexity: O(lg(n)). Space complexity: O(1).
    """
    if n < 1:
        return False

    while n % 4 == 0:
        n //= 4
    return n == 1


def is_power_four_2(n):
    """ Returns True if n is a power of 4, False otherwise.
    Algorithm description:
    1) Check if n is a power of 2 (see below).
    2) If True, then count number of zeroes in binary representation of n.
    Every power of 4 has even number of zeroes.

    How to check if n is a power of two?
    Every power of 2 has only 1 bit on - left-most bit, or
    most significant bit. We can perform logical & operation on n and n - 1,
    and if result is 0, then n is a power of 2.
    Time complexity: O(1). Space complexity: O(1).
    """
    if n < 1:
        return False

    # check if n is a power of 2
    if n & (n - 1) == 0:
        # count zeroes
        # alternatively we can do bin(n)[2:].count("0")
        # but it will take up more space
        zeroes = 0
        while n > 1:
            n >>= 1
        return zeroes % 2 == 0
    return False


def is_power_four_3(n):
    """ Returns True if n is a power of 4, False otherwise.
    Algorithm description:

    1) Check if n is a power of 2 (see algorithm above).
    2) Check if n - 1 is divisible by 3, i.e. n - 1 % 3 == 0.
    Time complexity: O(1). Space complexity: O(1).
    """
    if n < 1:
        return False
    return n & (n - 1) == 0 and (n - 1) % 3 == 0


if __name__ == "__main__":
    # check all powers of 4 from 0 to 32
    for y in range(32):
        n = 4 ** y
        assert is_power_four_1(n) == is_power_four_2(n) == is_power_four_3(n)

    # check random numbers, stress testing algorithms against each other
    while True:
        n = random.randrange(1, 10**18)
        if is_power_four_1(n) == is_power_four_2(n) == is_power_four_3(n):
            print("OK")
            print(n)
        else:
            print("Results are different.")
            print(f"n = {n}")
            break
