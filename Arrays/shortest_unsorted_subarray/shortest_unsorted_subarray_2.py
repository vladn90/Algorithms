""" Problem description can be found here:
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """ Improved algorithm.
        Time complexity: O(n). Space complexity: O(1).
        """
        n = len(nums)
        # special case
        if n < 2:
            return 0

        # find index of the min number of the unsorted subarray from the left
        left = n - 1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                left = i + 1
                break
        min_i = left
        for i in range(left + 1, n):
            if nums[i] < nums[min_i]:
                min_i = i

        # find index of max number of the unsorted subarray from the right
        right = 0
        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                right = i - 1
                break
        max_i = right
        for i in range(max_i - 1, -1, -1):
            if nums[i] > nums[max_i]:
                max_i = i

        # find the correct position of number at min index
        for i in range(min_i):
            if nums[i] > nums[min_i]:
                min_i = i
                break

        # find the correct position of number at max index
        for i in range(n - 1, max_i, -1):
            if nums[i] < nums[max_i]:
                max_i = i
                break

        # return length of unsorted subarray
        length = max_i - min_i + 1
        return length if length > 0 else 0


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.findUnsortedSubarray([]) == 0
    assert sol.findUnsortedSubarray([1]) == 0
    assert sol.findUnsortedSubarray([1, 2]) == 0
    assert sol.findUnsortedSubarray([2, 1]) == 2
    assert sol.findUnsortedSubarray([1, 1, 1, 1]) == 0
    assert sol.findUnsortedSubarray([1, 1, 1, 1, 0]) == 5
    assert sol.findUnsortedSubarray([9, 1, 1, 1, 1]) == 5
    assert sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
    assert sol.findUnsortedSubarray([4, 3, 2, 1]) == 4
    assert sol.findUnsortedSubarray([1, 2, 3, 4]) == 0
    assert sol.findUnsortedSubarray([-1, -2, -3, -4]) == 4
    assert sol.findUnsortedSubarray([-4, -3, -2, -1]) == 0
    assert sol.findUnsortedSubarray([1, 3, 3, 3, 2, 2, 2, 4, 4, 4]) == 6
    assert sol.findUnsortedSubarray([1, 2, 4, 5, 3]) == 3
    assert sol.findUnsortedSubarray([1, 2, 5, 3, 4]) == 3
    assert sol.findUnsortedSubarray([1, 2, 5, 1, 3, 4]) == 5
    assert sol.findUnsortedSubarray([1, 3, 5, 3, 4]) == 3
