""" Problem statement:
https://www.interviewbit.com/problems/diffk-ii/
"""
from collections import Counter


class Solution:
    def diffPossible(self, array, k):
        """ Returns 1 if there're two unique indices i and j in array,
        such that array[i] - array[j] == k. Returns 0 otherwise.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        if len(array) < 2:
            return 0

        nums = Counter(array)
        for a in array:
            if a - k in nums and k != 0:
                return 1
            elif a - k in nums and nums[a - k] > 1:
                return 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    func = sol.diffPossible

    array = [1, 3, 2]
    k = 0
    assert func(array, k) == 0

    array = [77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37,
             39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77, 12, 93, 0]
    k = 53
    assert func(array, k) == 1

    array = [1, 5, 3]
    k = 2
    assert func(array, k) == 1
