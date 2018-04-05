""" Problem description can be found here:
https://leetcode.com/problems/single-number/description/

Given an array of integers, every element appears twice except for one.
Find that single one.
"""


class Solution:
    def single_number_bit(self, nums):
        """ Time complexity: O(n). Space complexity: O(1), n is len(nums).
        """
        curr = 0
        for n in nums:
            curr ^= n
        return curr


if __name__ == "__main__":
    sol = Solution()
    assert sol.single_number_bit([1, 2, 2, 3, 1]) == 3
