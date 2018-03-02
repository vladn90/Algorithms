import math
import random


def find_root_1(x, n, p=0.001):
    """ Returns n-th root of a number x with precision p using guess method.
    """
    step = p / 10
    guess = step
    while abs(guess ** n - x) > p:
        guess += step
    return round(guess, 3)


def find_root_2(x, n, p=0.001):
    """ Returns n-th root of a number x with precision p using binary search.
    """
    step = p / 10
    left, right = 0, x
    while True:
        guess = (left + right) / 2
        result = guess ** n
        if abs(result - x) <= p:
            break
        elif result > x + p:
            right = guess - step
        else:
            left = guess + step

    if round(guess) ** n == x:
        return round(guess)
    return round(guess, 3)


def find_root_3(x, n, p):
    """ Intuitive way.
    """
    result = round(x ** (1 / n), p)
    if (result * 10) % 10 == 0:
        return int(result)
    return result


if __name__ == "__main__":
    # stress testing find_root_2 against find_root_3
    # y ^ n = x
    while True:
        y = random.randrange(1, 10)\
            + random.choice([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
        n = random.randrange(1, 10)
        x = round(y ** n, 3)
        fr3 = find_root_3(x, n, 3)
        fr2 = find_root_2(x, n)
        if round(fr3, 1) == round(fr2, 1):
            print("OK")
            print(f"{fr3} ^ {n} is roughly equal {x}")
        else:
            print("Something went wrong.")
            print(f"fr2 result: {fr2}")
            print(f"fr3 result: {fr3}")
            print(f"{y} ^ {n} = {x}")
            break
