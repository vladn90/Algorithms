""" Problem statement:
https://leetcode.com/problems/maximum-product-of-three-numbers/description/
"""
import random


class Solution:
    def max_product_sort(self, nums):
        """ Returns maximum possible product of three numbers from array nums.
        Sort the array and calculate max product as
        max(max(nums) * product(two min numbers), max(nums) * product(two max numbers)).

        Time complexity: O(n * lg(n)). Space complexity: O(n), n is len(nums).
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])

    def max_product_scan(self, nums):
        """ Returns maximum possible product of three numbers from array nums.
        Find three max numbers and two min numbers in one scan, then
        calculate max product as before.

        Time complexity: O(n). Space complexity: O(1), n is len(nums).
        """
        min1, min2 = float("inf"), float("inf")  # 2 min nums
        max1, max2, max3 = float("-inf"), float("-inf"), float("-inf")  # 3 max nums
        for number in nums:
            # update max nums
            if number > max1:
                max1, max2, max3 = number, max1, max2
            elif number > max2:
                max2, max3 = number, max2
            elif number > max3:
                max3 = number
            # update min nums
            if number < min1:
                min1, min2 = number, min1
            elif number < min2:
                min2 = number
        return max(max1 * min1 * min2, max1 * max2 * max3)

    def stress_test(self, func1, func2, n):
        """ Stress tests two functions against each other using random array
        of size n.
        """
        while True:
            array = [random.randrange(-10**3, 10**3) for i in range(n)]
            func1_result, func2_result = func1(array), func2(array)
            if func1_result == func2_result:
                print("OK")
                print(func1_result)
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"func1 result: {func1_result}")
                print(f"func2 result: {func2_result}")
                break


if __name__ == "__main__":
    sol = Solution()
    func1 = sol.max_product_sort
    func2 = sol.max_product_scan

    assert func1([1, 2, 3]) == 6
    assert func2([1, 2, 3]) == 6
    assert func1([1, 2, 3, 4]) == 24
    assert func2([1, 2, 3, 4]) == 24
    assert func1([-4, -3, -1, -2]) == -6
    assert func2([-4, -3, -1, -2]) == -6

    # stress testing two solutions against each other
    sol.stress_test(func1, func2, 10**3)
