""" Problem statement:
https://leetcode.com/problems/maximum-product-subarray/description/
"""
import random


class Solution:
    def max_product_brute(self, array):
        """ Returns max product of subarray. Brute force algorithm.
        Time complexity: O(n ^ 3). Space complexity: O(1), n is len(array).
        """
        max_value = float("-inf")
        n = len(array)
        # find the product for each subarray[i, j] and choose max
        for i in range(n):  # start of the subarray
            for j in range(i, n):  # end of the subarray
                curr = 1  # product of current subarray
                for x in range(i, j + 1):
                    curr *= array[x]
                max_value = max(max_value, curr)
        return max_value

    def max_product(self, array):
        """ Returns max product of subarray. Dynamic programming algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        if not array:  # special case, empty array
            return 0

        n = len(array)
        # max and min product ending at index i
        max_curr, min_curr, max_prod = array[0], array[0], array[0]
        for i in range(1, n):
            max_curr, min_curr = \
                max(array[i], max_curr * array[i], min_curr * array[i]), \
                min(array[i], max_curr * array[i], min_curr * array[i])
            max_prod = max(max_prod, max_curr)  # update max product so far
        return max_prod

    def max_product_2(self, array):
        """ Optimized version of algorithm from above.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        if not array:  # special case, empty array
            return 0

        # max and min product ending at index i
        max_curr, min_curr, max_prod = array[0], array[0], array[0]
        for i in range(1, len(array)):
            if array[i] > 0:
                max_curr = max(max_curr * array[i], array[i])
                min_curr = min(min_curr * array[i], array[i])
            else:
                max_curr, min_curr = \
                    max(min_curr * array[i], array[i]), \
                    min(max_curr * array[i], array[i])
            max_prod = max(max_prod, max_curr)  # update max product so far
        return max_prod

    def stress_test(self, func1, func2, n):
        """ Stress tests two functions against each other using random array
        of size n.
        """
        while True:
            array = [random.randrange(-10, 10) for i in range(n)]
            func1_result, func2_result = func1(array), func2(array)
            if func1_result == func2_result:
                print("OK")
                print(func1_result)
                print()
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"func1 result: {func1_result}")
                print(f"func2 result: {func2_result}")
                break


if __name__ == "__main__":
    sol = Solution()
    func = sol.max_product_2

    assert func([1, 2, 3, 4, 5, 6]) == 720
    assert func([5, 3, -2, 5, 6, -3, 8]) == 21600
    assert func([5, 3, -2, 5, 6, 8]) == 240
    assert func([1, 2, 3, 4, 0, 4, 2]) == 24
    assert func([1, 2, 4, -5, 6, 8, 0, -2, 4]) == 48
    assert func([6, 7, 0, 1, -1, -3, -10, -7, -3, 3]) == 1890

    func1 = sol.max_product_brute
    func2 = sol.max_product
    sol.stress_test(func1, func2, 10)
