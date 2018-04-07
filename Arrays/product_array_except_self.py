""" Problem statement:
https://leetcode.com/problems/product-of-array-except-self/description/
"""
import random


class Solution:
    def product_except_self_1(self, array):
        """ Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        n = len(array)
        # array of product to the left of i
        left = [1] * n
        for i in range(1, n):
            left[i] = left[i - 1] * array[i - 1]

        # array of product to the right of i
        right = [1] * n
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * array[i + 1]

        # calculate resulting array
        return [left[i] * right[i] for i in range(n)]

    def product_except_self_2(self, array):
        """ Time complexity: O(n). Space complexity: O(1), n is len(array).
        Output array isn't included in space complexity analysis.
        """
        n = len(array)
        # array of product to the left of i
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i - 1] * array[i - 1]

        # array of product to the right of i and final result
        prev = 1  # previous result of product to the right of i
        for i in range(n - 2, -1, -1):
            result[i] *= array[i + 1] * prev
            prev *= array[i + 1]  # update previous
        return result

    def product_except_self_3(self, array):
        """ Last optimization. All in one loop.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        Output array isn't included in space complexity analysis.
        """
        n = len(array)
        result = [1] * n
        # current product to the left if i and to the right of j
        left, right = 1, 1
        for i in range(n):
            result[i] *= left
            left *= array[i]  # update left
            j = n - 1 - i
            result[j] *= right
            right *= array[j]  # update right
        return result

    def stress_test(self, func1, func2, n):
        """ Stress testing two functions against each other using random
        input array of size n.
        """
        while True:
            array = [random.randrange(1, 10**2) for i in range(n)]
            res1, res2 = func1(array), func2(array)
            if res1 == res2:
                print("OK")
                print(res1[:2])
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"result 1: {res1}")
                print(f"result 2: {res2}")
                break


if __name__ == "__main__":
    sol = Solution()
    func1 = sol.product_except_self_2
    func2 = sol.product_except_self_3

    assert func1([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert func2([1, 2, 3, 4]) == [24, 12, 8, 6]

    sol.stress_test(func1, func2, 10**2)
