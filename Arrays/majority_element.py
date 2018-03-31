""" Problem description can be found here:
https://leetcode.com/problems/majority-element/description/
"""
from collections import Counter


class Solution:
    def majority_element_1(self, nums):
        """ Time complexity: O(n). Space complexity: O(n), n is len(nums).
        Hash map based algorithm. Regular version.
        """
        x = len(nums) // 2 + 1  # majority count
        num_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1
            if num_count[n] == x:
                return n

    def majority_element_2(self, nums):
        """ Time complexity: O(n). Space complexity: O(n), n is len(nums).
        Hash map based algorithm. Pythonic faster version.
        """
        num_count = Counter(nums)
        return max(num_count, key=lambda n: num_count[n])
        # or
        # x = len(nums) // 2 + 1  # majority count
        # num_count = Counter(nums)
        # return [n for n in num_count if num_count[n] >= x][0]

    def majority_element_3(self, nums):
        """ Time complexity: O(n). Space complexity: O(n), n is len(nums).
        Hash map based algorithm. Pythonic fastest version.
        """
        x = len(nums) // 2 + 1  # majority count
        num_count = Counter(nums)
        for n in num_count:
            if num_count[n] >= x:
                return n

    def majority_element_4(self, nums):
        """ Time complexity: O(n). Space complexity: O(1), n is len(nums).
        Boyer–Moore majority vote algorithm.
        """
        curr = None  # current majority element
        curr_count = 0  # current count of majority - minority
        for n in nums:
            if curr_count == 0:  # choose new majority element
                curr = n
                curr_count = 1
            else:
                if n == curr:  # +1, n == current majority element
                    curr_count += 1
                else:  # -1, n != current majority element
                    curr_count -= 1
        return curr


if __name__ == "__main__":
    sol = Solution()
    func = sol.majority_element_4

    # simples tests
    assert func([1, 1, 2]) == 1
    assert func([1, 1, 1, 1, 1, 1, 2]) == 1
    assert func([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 7, 7, 7, 7]) == 7
    assert func([7, 7, 5, 7, 5, 1, 5, 7, 5, 5, 7, 7, 5, 5, 5, 5]) == 5
