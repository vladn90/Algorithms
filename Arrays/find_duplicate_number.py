""" Problem description can be found here:
https://leetcode.com/problems/find-the-duplicate-number/description/
"""


class Solution:
    def find_duplicate_sort(self, nums):
        """ Return duplicate number from array nums.
        Sort the array, compare adjacent elements.
        Time complexity: O(n * lg(n)). Space complexity: O(n).
        """
        nums.sort()
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]

    def find_duplicate_hash(self, nums):
        """ Return duplicate number from array nums.
        Use hash table to keep track of repeating elements.
        Time complexity: O(n). Space complexity: O(n).
        """
        table = set()
        for num in nums:
            if num in table:
                return num
            table.add(num)

    def find_duplicate_cycle(self, nums):
        """ Return duplicate number from array nums.
        Use Floyd's cycle detection algorithm.
        Time complexity: O(n). Space complexity: O(1).
        """
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        p1, p2 = slow, nums[0]
        while p1 != p2:
            p1, p2 = nums[p1], nums[p2]

        return p1


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.find_duplicate_hash([1, 3, 4, 2, 2, 5]) == 2
    assert sol.find_duplicate_hash([1, 1, 2, 3, 4]) == 1
    assert sol.find_duplicate_hash([1, 2, 2, 2, 2, 3]) == 2
