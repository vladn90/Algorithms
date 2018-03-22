""" Problem description can be found here:
https://leetcode.com/problems/third-maximum-number/description/
"""


class Solution:
    def thirdMax_1(self, nums):
        """ Returns 3rd maximum unique number in array nums.
        If there's no such, returns 1st / 2nd max unique number.
        Simple algorithm. Algorithm description:
        1) Create a set of max numbers.
        2) Loop over array 3 times.
        3) Choose next max number that doesn't equal numbers in the set.
        4) If we found 3 max numbers, choose min from the set,
           else choose max number from the set.

        Time complexity: O(n). Space complexity: O(1), where n is len(nums).
        """
        max_nums = set()  # set of 3 or less max numbers from nums
        for k in range(3):
            curr_max = float("-inf")  # current maximum number
            for n in nums:
                if n not in max_nums and n > curr_max:
                    curr_max = n
            if curr_max != float("-inf"):
                max_nums.add(curr_max)
        return min(max_nums) if len(max_nums) == 3 else max(max_nums)

    def thirdMax_2(self, nums):
        """ Returns 3rd maximum unique number in array nums.
        If there's no such, returns 1st / 2nd max unique number.
        Improved algorithm. Algorithm description:
        1) Iterate over array once and keep track of 1st, 2nd, 3rd max numbers.
        2) Return 3rd max number if there's one, else return 1st max number.

        Time complexity: O(n). Space complexity: O(1), where n is len(nums).
        """
        first = second = third = float("-inf")
        for n in nums:
            if n > first:
                first, second, third = n, first, second
            elif n != first and n > second:
                second, third = n, second
            elif n != first and n != second and n > third:
                third = n
        if third != float("-inf"):
            return third
        else:
            return first


if __name__ == "__main__":
    sol = Solution()
    assert sol.thirdMax_1([3, 2, 1]) == 1
    assert sol.thirdMax_2([3, 2, 1]) == 1
    assert sol.thirdMax_1([1, 2]) == 2
    assert sol.thirdMax_2([1, 2]) == 2
