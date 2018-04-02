""" Problem description can be found here:
https://leetcode.com/problems/search-insert-position/description/
"""
import bisect


class Solution:
    def searchInsert(self, nums, target):
        """ Returns position of a target if it's present in nums,
        otherwise returns an insert position.
        Faster solution.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(nums).
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return start

    def searchInsert_builtin(self, nums, target):
        """ Returns position of a target if it's present in nums,
        otherwise returns an insert position. Using standard library function.
        Slower solution.
        Time complexity: O(lg(n)). Space complexity: O(1), n is len(nums).
        """
        return bisect.bisect_left(nums, target)


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.searchInsert([1, 3, 5, 7, 9], 1) == 0
    assert sol.searchInsert([1, 3, 5, 7, 9], 9) == 4
    assert sol.searchInsert([1, 3, 5, 7, 9], 2) == 1
    assert sol.searchInsert([1, 3, 5, 7, 9], 10) == 5
    assert sol.searchInsert([1, 3, 5, 7, 9], 0) == 0
