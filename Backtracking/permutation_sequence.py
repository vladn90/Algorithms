""" Problem statement:
https://leetcode.com/problems/permutation-sequence/description/
https://www.interviewbit.com/problems/kth-permutation-sequence/
"""
import random
import math
from itertools import permutations


class Solution:
    def reverse_array(self, array, i, j):
        """ Reverses array in-place from index i to j.
        """
        while i < j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    def next_permutation(self, array):
        """ Generates next lexicographical permutation of an array.
        Modifies array in-place, doesn't return anything.
        """
        # find longest non-increasing suffix
        for i in range(len(array) - 1, 0, -1):
            if array[i] > array[i - 1]:
                break
        else:  # this the last permutation, so next permutation is the 1st one
            array.reverse()
            return
        # swap the element at index i - 1 with the 1st > element from the right
        for j in range(len(array) - 1, i - 1, -1):
            if array[j] > array[i - 1]:
                array[j], array[i - 1] = array[i - 1], array[j]
                break
        # minimize suffix by reversing it
        self.reverse_array(array, i, len(array) - 1)

    def get_permutation_naive(self, n, k):
        """ Naive algorithm. List all permutations and find the one.
        Time complexity: O(n!).
        """
        perms = permutations(range(1, n + 1))
        for i, p in enumerate(perms):
            if i + 1 == k:
                return "".join(map(str, p))

    def get_permutation_naive(self, n, k):
        """ Another naive algorithm.
        Generate next permutation until we reach k-th permutation.
        Time complexity: O(n!).
        """
        curr = list(range(1, n + 1))  # first permutation
        for i in range(k - 1):
            self.next_permutation(curr)
        return "".join(map(str, curr))

    def get_permutation(self, n, k):
        """ Fast algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(1).
        """
        k -= 1  # since python arrays are 0-based
        fact = [1] * (n + 1)  # precompute factorials
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        nums = list(range(1, n + 1))  # our number "string"
        result = []  # k-th permutation
        for i in range(1, n + 1):
            j = k // fact[n - i]  # index of i-th element in original nums
            result.append(nums[j])
            del nums[j]  # remove element at index j from nums
            k -= j * fact[n - i]
        return "".join(map(str, result))


def stress_test(func1, func2):
    """ Stress tests two functions against each other.
    """
    while True:
        n = random.randrange(1, 9)
        k = random.randrange(1, math.factorial(n) + 1)
        res1 = func1(n, k)
        res2 = func2(n, k)
        if res1 == res2:
            print("OK")
            print(res1)
        else:
            print("Results are different.")
            print(f"n = {n}, k = {k}")
            print(f"result 1 = {res1}")
            print(f"result 2 = {res2}")
            break


if __name__ == "__main__":
    sol = Solution()
    func = sol.get_permutation

    assert func(3, 3) == "213"
    assert func(4, 9) == "2314"

    # stress testing naive and improved algorithms against each other
    stress_test(sol.get_permutation_naive, sol.get_permutation)
