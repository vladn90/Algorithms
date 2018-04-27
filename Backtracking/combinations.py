""" Problem statement:
https://leetcode.com/problems/combinations/description/
https://www.interviewbit.com/problems/combinations/
"""
import random
from itertools import combinations


class Solution:
    def combine(self, n, k):
        """ Built-in solution.
        """
        return combinations(range(1, n + 1), k)

    def combine(self, n, k):
        """ Slow recursive backtracking algorithm.
        """
        result = []

        def find_all(i, n, k, arr):
            if k == 0:
                result.append(arr)
                return
            for j in range(i, n + 1):
                find_all(j + 1, n, k - 1, arr + [j])

        find_all(1, n, k, [])
        return result

    def combine(self, n, k):
        """ Fast iterative backtracking algorithm.
        """
        result = []
        stack = []
        x = 1
        while True:
            if len(stack) == k:  # subset of size k is ready
                result.append(stack[:])
            if len(stack) == k or x > n - k + len(stack) + 1:  # very important line
                if not stack:  # we exhausted all possibilities
                    return result
                x = stack.pop() + 1  # backtrack
            else:  # stack isn't full yet and x <= n
                stack.append(x)
                x += 1


def stress_test(func1, func2):
    while True:
        n = random.randrange(10, 20)
        k = random.randrange(3, 9)
        res1 = list(map(list, func1(n, k)))
        res2 = func2(n, k)
        assert res2 == sorted(res2)
        if res1 == res2:
            print("OK")
            print(n, k)
        else:
            print("Different results.")
            print(f"n = {n}, k = {k}")
            break


if __name__ == "__main__":
    sol = Solution()
    func = sol.combine

    n = 4
    k = 2
    result = func(n, k)
    for arr in result:
        print(arr)
