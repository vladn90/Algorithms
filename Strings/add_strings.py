""" Problem description can be found here:
https://leetcode.com/problems/add-strings/description/
"""
import random


class Solution:
    def addStrings(self, num1, num2):
        """ Returns sum of two numbers. Pen-and-paper algorithm.
        input: num1, num2 as strings
        output: string
        Time complexity: O(n + m). Space complexity: O(n + m), where
        n is len(num1), m is len(num2).
        """
        result = []  # digits of resulting number in reverse order
        len1, len2 = len(num1), len(num2)

        # sum numbers starting from the rightmost digits
        i, j = len1 - 1, len2 - 1
        carry = 0
        while i > -1 and j > -1:
            curr = int(num1[i]) + int(num2[j]) + carry  # current digits sum
            result.append(curr % 10)  # add 1 digit to resulting number
            carry = curr // 10  # update carry
            i -= 1
            j -= 1

        # number 1 is longer than number 2
        while i > -1:
            curr = carry + int(num1[i])
            result.append(curr % 10)
            carry = curr // 10
            i -= 1
        # number 2 is longer than number 1
        while j > -1:
            curr = carry + int(num2[j])
            result.append(curr % 10)
            carry = curr // 10
            j -= 1
        # add last carry-digit if there's any
        if carry:
            result.append(carry)

        # reverse the digits, convert each digit to string and concatenate
        return "".join(map(str, result[::-1]))


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.addStrings("0", "0") == "0"
    assert sol.addStrings("9", "0") == "9"
    assert sol.addStrings("0", "9") == "9"
    assert sol.addStrings("999", "1") == "1000"
    assert sol.addStrings("1", "999") == "1000"
    assert sol.addStrings("999", "999") == "1998"

    # stress testing against Python built-in big int arithmetic
    while True:
        num1 = "".join(map(chr, [random.randrange(49, 58) for i in range(10**4)]))
        num2 = "".join(map(chr, [random.randrange(49, 58) for i in range(10**4)]))

        python_result = str(int(num1) + int(num2))
        my_result = sol.addStrings(num1, num2)
        if my_result == python_result:
            print("OK")
            print(my_result[:100])
            print()
        else:
            print("Results are different.")
            print(f"number 1: {num1}")
            print(f"number 2: {num2}")
            print(f"my result: {my_result}")
            print(f"python result: {python_result}")
            break
