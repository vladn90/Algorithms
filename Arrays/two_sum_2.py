""" Problem description can be found here:
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
"""


class Solution:
    def two_sum_1(self, numbers, target):
        """ Returns 1-based indices i and j of two elements from array nums,
        such as nums[i] + nums[j] == target.
        Two pointers algorithm.
        Time complexity: O(n). Space complexity: O(1), where n is len(numbers).
        """
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            curr = numbers[i] + numbers[j]
            if curr < target:
                i += 1
            elif curr > target:
                j -= 1
            else:
                return i + 1, j + 1

    def two_sum_2(self, numbers, target):
        """ Returns 1-based indices i and j of two elements from array nums,
        such as nums[i] + nums[j] == target.
        Hashing based algorithm.
        Time complexity: O(n). Space complexity: O(n), where n is len(numbers).
        """
        hash_map = dict()  # integer: index
        for i, num1 in enumerate(numbers):
            num2 = target - num1  # calculate second number
            if num2 in hash_map:  # check if we've seen this number before
                return hash_map[num2] + 1, i + 1
            hash_map[num1] = i  # save current integer and its index


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.two_sum_1([0, 0, 3, 4], 0) == (1, 2)
    assert sol.two_sum_1([2, 3, 4], 6) == (1, 3)
    assert sol.two_sum_2([0, 0, 3, 4], 0) == (1, 2)
    assert sol.two_sum_2([2, 3, 4], 6) == (1, 3)
