""" Comparison of different algorithms to calculate n-th Fibonacci number.
In this implemention Fibonacci sequence is gonna start with 0, i.e.
0, 1, 1, 2, 3, 5...
"""
from timeit import timeit
from functools import lru_cache


def fib_1(n):
    """ Recursive algorithm. Very slow. Runs in exponential time.
    """
    # base case 0th Fibonacci number = 0
    if n == 0:
        return 0
    # base case 1st Fibonacci number = 1
    elif n == 1:
        return 1
    return fib_1(n - 1) + fib_1(n - 2)


fib_cache = {0: 0, 1: 1}  # Fib index: Fib number


def fib_2(n):
    """ Improved algorithm using memoization, runs in linear time.
    """
    if n in fib_cache:
        return fib_cache[n]
    fib_cache[n] = fib_2(n - 1) + fib_2(n - 2)
    return fib_cache[n]


@lru_cache()
def fib_3(n):
    """ Same logic as above but using cache function as a decorator.
    """
    # base case 0th Fibonacci number = 0
    if n == 0:
        return 0
    # base case 1st Fibonacci number = 1
    elif n == 1:
        return 1
    return fib_3(n - 1) + fib_3(n - 2)


def fib_4(n):
    """ Dynamic programming solution. Runs in O(n) time and uses O(1) space.
    """
    if n < 2:
        return n
    prev, curr = 0, 1
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == "__main__":
    # stress testing solutions against each other up to 20th Fibonacci number
    for n in range(0, 21):
        f1 = fib_1(n)
        f2 = fib_2(n)
        f3 = fib_3(n)
        f4 = fib_4(n)
        assert f1 == f2 == f3 == f4

    # time comparison for n-th Fibonacci number
    n = 30
    t1 = timeit("fib_1(n)", number=1, globals=globals())
    t3 = timeit("fib_2(n)", number=1, globals=globals())
    t4 = timeit("fib_4(n)", number=1, globals=globals())
    print(f"Recursive implemention: {t1}")
    print(f"Recursive implemention with memoization: {t3}")
    print(f"Dynamic programming solution: {t4}")
