import random


def binary(n):
    """ Converts integer n from decimal to binary.
    input: integer
    output: integer
    Time complexity: O(lg(n)). Space complexity: O(lg(n)).
    """
    # handles negative numbers
    negative = False
    if n < 0:
        negative = True
        n = abs(n)

    # divide n by 2 while n != 0, append remainder of division to array
    number = []
    while n != 0:
        number.append(n % 2)
        n //= 2

    # return binary number as integer
    bin_number = 0
    mult = 10 ** (len(number) - 1)
    n_len = len(number)
    for i in range(n_len - 1, -1, -1):
        bin_number += (number[i] * mult)
        mult //= 10
    return bin_number if not negative else -bin_number


if __name__ == "__main__":
    # stress testing binary function against built-in bin function
    while True:
        n = random.randrange(10**6, 10**12)
        print(f"current number: {n}")
        assert binary(n) == int(bin(n)[2:])
