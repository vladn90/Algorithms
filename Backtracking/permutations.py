""" Problem statement:
https://leetcode.com/problems/permutations/description/
https://www.interviewbit.com/problems/permutations/
"""
import random
from math import factorial
from itertools import permutations


class Solution:
    def permute(self, nums):
        """ Backtracking recursive algorithm.
        Time complexity: O(n * n!). Space complexity: O(n), n is len(nums).
        """
        def find_permutations(start, array, n, result):
            if start == n - 1:
                result.append(array[:])  # add current permutation
                return
            for i in range(start, n):
                array[i], array[start] = array[start], array[i]  # fix element i
                find_permutations(start + 1, array, n, result)
                array[start], array[i] = array[i], array[start]  # backtrack

        result = []
        find_permutations(0, nums, len(nums), result)
        return result


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

    def permute(self, nums):
        """ Generate next permutation until all permutations are generated.
        Time complexity: O(n * n!). Space complexity: O(n), n is len(nums).
        """
        n = factorial(len(nums)) - 1
        result = [nums[:]]
        for i in range(n):
            self.next_permutation(nums)
            result.append(nums[:])
        return result


def stress_test(func):
    """ Stress tests custom function against built-in itertools.permutations.
    """
    for i in range(2, 10):
        nums = list(range(1, i + 1))
        p1 = sorted(permutations(nums))
        p2 = sorted(map(tuple, func(nums)))
        assert p1 == p2
    print("All good.")


if __name__ == "__main__":
    sol = Solution()
    func = sol.permute

    nums = [1, 2, 3]
    result = func(nums)
    for arr in result:
        print(arr)

    stress_test(func)
