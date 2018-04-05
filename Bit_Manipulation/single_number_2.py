""" Problem description can be found here:
https://leetcode.com/problems/single-number-ii/description/

Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.
"""


class Solution:
    def single_number(self, nums):
        """ Time complexity: O(n). Space complexity: O(1), n is len(nums).
        """
        once, twice = 0, 0
        for n in nums:
            twice = twice | (once & n)  # store bits of number that appeared twice
            once = once ^ n  # store bits of number that appeared once
            common = once & twice  # common bits between once and twice
            once = once & (~common)  # remove common bits from once
            twice = twice & (~common)  # remove common bits from twice
        return once


if __name__ == "__main__":
    sol = Solution()
    assert sol.single_number([1, 2, 4, 3, 3, 2, 2, 3, 1, 1]) == 4
