""" Problem statement:
https://leetcode.com/problems/sort-colors/description/
"""
from collections import Counter


class Solution:
    def sortColors(self, nums):
        """ Doesn't return anything. Modifies array nums in-place.
        Algorithm is based on counting colors(0, 1, 2) in array nums.
        Time complexity: O(n). Space complexity: O(1), n is len(nums).
        """
        # count number of red, white and blue objects in nums
        colors = Counter(nums)
        # change values in array nums according to count of colors
        i = 0
        while i < colors[0]:  # set first colors[0] values to 0
            nums[i] = 0
            i += 1  # current color count and array index
        j = 0  # set next colors[1] values to 1
        while j < colors[1]:
            nums[i] = 1
            i += 1  # array index
            j += 1  # current color count
        k = 0  # set next colors[2] values to 2
        while k < colors[2]:
            nums[i] = 2
            i += 1
            k += 1

    def sortColors(self, nums):
        """ Doesn't return anything. Modifies array nums in-place.
        Algorithm is based on partitioning array into 3 parts.
        Time complexity: O(n). Space complexity: O(1), n is len(nums).
        """
        # initialize left, mid and right pointers
        left, mid, right = 0, 0, len(nums) - 1
        while left <= right and nums[left] == 0:  # find first value from the left != 0
            left += 1
            mid = left
        while right > -1 and nums[right] == 2:  # find first value from the right != 2
            right -= 1

        while mid <= right:
            if nums[mid] == 0:  # swap with current left
                nums[left], nums[mid] = nums[mid], nums[left]
                mid += 1
                left += 1
            elif nums[mid] == 2:  # swap with current right
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1
            else:  # nums[mid] == 1, no swaps needed, move mid to the next color
                mid += 1


if __name__ == "__main__":
    sol = Solution()
    colors = [0, 1, 1, 1, 2, 0, 2, 2, 2]
    print(f"before: {colors}")
    sol.sortColors(colors)
    print(f"after: {colors}")
