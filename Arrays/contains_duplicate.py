""" Problem statement:
https://leetcode.com/problems/contains-duplicate/description/
"""


class Solution:
    def contains_duplicate_1(self, array):
        """ Set(hash table) can contain only unique values.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        return len(array) != len(set(array))

    def contains_duplicate_2(self, array):
        """ Solution(more like explanation of above) using hash table.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        nums = set()
        for num in array:
            if num in nums:
                return True
            nums.add(num)
        return False


if __name__ == "__main__":
    sol = Solution()
    func = sol.contains_duplicate_2

    assert func([1, 2, 3, 4, 5]) == False
    assert func([1, 2, 3, 4, 5, 2]) == True
