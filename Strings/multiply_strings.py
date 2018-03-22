""" Problem description can be found here:
https://leetcode.com/problems/multiply-strings/description/
"""
import random


class Solution:
    def multiply(self, num1, num2):
        """ Returns product of two numbers. Long multiplication algorithm.
        input: num1, num2 as strings
        output: string
        Time complexity: O(n * m). Space complexity: O(n + m),
        where n is len(num1), m is len(num2).
        """
        len1, len2 = len(num1), len(num2)

        # reverse the numbers and convert each digit to integer
        num1 = list(map(int, reversed(num1)))
        num2 = list(map(int, reversed(num2)))
        # digits of resulting number in reversed order
        result = [0 for i in range(len1 + len2)]

        for j in range(len2):
            for i in range(len1):
                result[i + j] += num1[i] * num2[j]
                result[i + j + 1] += result[i + j] // 10  # carry
                result[i + j] %= 10  # 1-digit

        # get rid of leading zeros, find index of first non-zero digit
        i = len(result) - 1
        while result[i] == 0 and i > 0:
            i -= 1
        # convert digits to strings, reverse and concatenate
        return "".join(map(str, result[:i + 1][::-1]))


if __name__ == "__main__":
    sol = Solution()
    # simple tests
    assert sol.multiply("0", "0") == "0"
    assert sol.multiply("0", "99") == "0"
    assert sol.multiply("99", "0") == "0"
    assert sol.multiply("1", "1") == "1"
    assert sol.multiply("9", "9") == "81"
    assert sol.multiply("123", "456") == "56088"

    # stress testing long multiplication algorithm against
    # built-in Python Karatsuba algorithm for big integers
    while True:
        num1 = "".join(map(chr, [random.randrange(49, 58) for i in range(10**2)]))
        num2 = "".join(map(chr, [random.randrange(49, 58) for i in range(10**2)]))
        python_result = str(int(num1) * int(num2))
        my_result = sol.multiply(num1, num2)

        if my_result == python_result:
            print("OK")
            print(my_result)
            print()
        else:
            print("Results are different.")
            print(f"number 1: {num1}")
            print(f"number 2: {num2}")
            print(f"my result: {my_result}")
            print(f"python result: {python_result}")
            break
