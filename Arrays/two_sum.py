""" Problem description can be found here:
https://leetcode.com/problems/two-sum/description/
"""


class Solution:
    def two_sum_1(self, nums, target):
        """ Returns indices i and j of two elements from array nums, such as
        nums[i] + nums[j] == target.
        Simple algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(1),
        where n is len(nums).
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return i, j

    def two_sum_2(self, nums, target):
        """ Returns indices i and j of two elements from array nums, such as
        nums[i] + nums[j] == target.
        Simple algorithm. Short version.
        Time complexity: O(n ^ 2). Space complexity: O(1),
        where n is len(nums).
        """
        return [(i, j) for i in range(len(nums) - 1)
                for j in range(i + 1, len(nums))
                if nums[i] + nums[j] == target][0]

    def two_sum_3(self, nums, target):
        """ Returns indices i and j of two elements from array nums, such as
        nums[i] + nums[j] == target.
        Two pointers algorithm.
        Time complexity: O(n * lg(n)). Space complexity: O(n),
        where n is len(nums).
        """
        # sort the array while preserving original indices
        nums_sort = sorted(enumerate(nums), key=lambda x: x[1])
        i, j = 0, len(nums) - 1
        while i < j:
            curr = nums_sort[i][1] + nums_sort[j][1]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return nums_sort[i][0], nums_sort[j][0]

    def two_sum_4(self, nums, target):
        """ Returns indices i and j of two elements from array nums, such as
        nums[i] + nums[j] == target.
        Improved algorithm, based on hashing.
        Time complexity: O(n). Space complexity: O(n),
        where n is len(nums).
        """
        nums_dict = {}  # integer: index
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in nums_dict:
                return nums_dict[num2], i
            nums_dict[num] = i


if __name__ == "__main__":
    sol = Solution()

    # simple test
    nums = [2, 7, 11, 15]
    target = 9
    print(sol.two_sum_4(nums, target))
