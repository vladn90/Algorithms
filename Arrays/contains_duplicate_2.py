""" Problem statement:
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an array of integers and an integer k, find out whether
there are two distinct indices i and j in the array such that nums[i] = nums[j]
and the absolute difference between i and j is at most k.
"""


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """ Time complexity: O(n). Space complexity: O(n), n is len(nums).
        """
        nums_dict = dict()  # integer: most recent index
        for i, n in enumerate(nums):
            if n in nums_dict and abs(nums_dict[n] - i) <= k:
                return True
            nums_dict[n] = i  # update index of integer n in dictionary
        return False


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 4, 1, 6, 8]
    k = 4
    print(sol.containsNearbyDuplicate(nums, k))
