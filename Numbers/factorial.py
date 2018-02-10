import sys
sys.setrecursionlimit(10**6)  # increasing recursion limit


def factorial_1(n):
    """ Returns a factorial of number n. Recursive solution.

    input: n as int
    output: int
    """
    # base case, factorial(1) = 1 and factorial(0) = 1
    if n <= 1:
        return 1
    return n * factorial_1(n - 1)


def factorial_2(n):
    """ Returns a factorial of number n. Iterative solution.

    input: n as int
    output: int
    """
    # factorial(1) = 1 and factorial(0) = 1
    if n <= 1:
        return 1
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


# stress testing solutions against each other
if __name__ == "__main__":
    limit = 10**3
    for n in range(1, limit + 1):
        f1 = factorial_1(n)
        f2 = factorial_2(n)
        if f1 != f2:
            print(f"Different values for n = {n}")
            break
    else:
        print("OK")
