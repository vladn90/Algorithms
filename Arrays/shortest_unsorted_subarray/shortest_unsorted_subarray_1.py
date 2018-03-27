""" Problem description can be found here:
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        """ Simple algorithm. Algorithm description:
        Create a sorted copy of the array and find 1st different element
        from the right and from the left. Return the distance between them.

        Time complexity: O(n * lg(n)). Space complexity: O(n).
        """
        n = len(nums)
        nums_sort = sorted(nums)
        # compare sorted array nums with original nums and find first different
        # elements from the left and from the right
        x = 0
        for i in range(n):
            if nums[i] != nums_sort[i]:
                x = i
                break
        else:  # no break occured, i.e. original array is sorted
            return 0

        y = n - 1
        for i in range(n - 1, -1, -1):
            if nums[i] != nums_sort[i]:
                y = i
                break
        return y - x + 1


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
