""" Problem description can be found here:
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
"""


class Solution:
    def findKthLargest(self, nums, k):
        """ Returns kth largest element in array, i.e. if array was sorted,
        it would be k-th element.
        Time complexity: O(n * lg(n)). Space complexity: O(n), where
        n is len(nums).
        """
        nums.sort(reverse=True)
        return nums[k - 1]


if __name__ == "__main__":
    sol = Solution()
    array = [3, 2, 1, 2, 2, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 4, 0, 0, 0, 0]
    assert sol.findKthLargest(array, 3) == 6
