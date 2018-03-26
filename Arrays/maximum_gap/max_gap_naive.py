""" Problem description can be found here:
https://leetcode.com/problems/maximum-gap/description/
"""


class Solution:
    def maximumGap(self, nums):
        """ Returns the maximum gap between elements if array nums was sorted.
        Naive algorithm. Sort the array and find the maximum gap.
        Time complexity: O(n * lg(n)). Space complexity: O(n), where
        n is len(nums).
        """
        # special case, len(nums) < 2
        if len(nums) < 2:
            return 0

        nums = sorted(nums)
        max_gap = 0
        n = len(nums)
        for i in range(n - 1):
            max_gap = max(max_gap, abs(nums[i] - nums[i + 1]))
        return max_gap


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.maximumGap([9, 19, 13, 12, 33, 41, 22]) == 11
    assert sol.maximumGap([1, 2, 3]) == 1
    assert sol.maximumGap([9, 9, 9, 8, 7, 7, 8]) == 1
    assert sol.maximumGap([1, 1, 1, 1]) == 0
    assert sol.maximumGap([1, 10000000]) == 9999999
