""" Problem description can be found here:
https://leetcode.com/problems/majority-element-ii/description/
"""
from collections import Counter


class Solution:
    def majority_element_1(self, nums):
        """ Hash map based algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(nums).
        """
        x = len(nums) // 3
        nums_count = Counter(nums)
        return [n for n in nums_count if nums_count[n] > x]

    def majority_element_2(self, nums):
        """ Time complexity: O(n). Space complexity: O(1), n is len(nums).
        Boyer–Moore majority vote algorithm.
        """
        num1, num2 = None, None
        num1_count, num2_count = 0, 0
        for number in nums:  # choose 2 majority elements
            if num1_count <= 0 and number != num2:  # choose 1st num
                num1 = number
                num1_count = 0
            if num2_count <= 0 and number != num1:  # choose 2nd num
                num2 = number
                num2_count = 0

            if number == num1:
                num1_count += 1
            elif number == num2:
                num2_count += 1
            else:
                num1_count -= 1
                num2_count -= 1

        num1_count, num2_count = 0, 0  # verify majority count for each num
        for number in nums:
            if number == num1:
                num1_count += 1
            elif number == num2:
                num2_count += 1

        x = len(nums) // 3
        if num1_count > x and num2_count > x:
            return sorted([num1, num2])
        elif num1_count > x:
            return [num1]
        elif num2_count > x:
            return [num2]
        else:
            return []


if __name__ == "__main__":
    sol = Solution()
    func = sol.majority_element_2

    # simple tests
    assert func([1]) == [1]
    assert func([2]) == [2]
    assert func([1, 2]) == [1, 2]
    assert func([1, 1, 2, 2, 3]) == [1, 2]
    assert func([1, 1, 2, 2, 2, 3, 3, 3]) == [2, 3]
    assert func([1, 1, 2, 2, 1, 2, 4, 5]) == [1, 2]
