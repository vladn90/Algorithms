""" Problem description can be found here:
https://leetcode.com/problems/add-binary/description/
"""


import random


class Solution:
    def add_binary_naive(self, num1, num2):
        """ Naive algorithm to find sum of 2 binary numbers.
        """
        return bin(int(num1, 2) + int(num2, 2))[2:]

    def add_binary(self, num1, num2):
        """ Returns a sum of 2 binary numbers.
        input: num1, num2 as strings
        output: string
        Time complexity: O(n + m). Space complexity: O(n + m), where
        n, m are len(num1), len(num2).
        """
        # special case, empty strings
        if not num1 and not num2:
            return "0"
        elif not num1:
            return num2
        elif not num2:
            return num1

        result = []
        n1, n2 = len(num1), len(num2)
        i, j = n1 - 1, n2 - 1
        carry = 0
        # add binary digits starting from the right(least significant bit)
        while i > -1 and j > -1:
            curr1, curr2 = int(num1[i]), int(num2[j])
            curr_sum = curr1 + curr2
            if curr_sum == 0:
                result.append(carry)
                carry = 0
            elif curr_sum == 1 and carry == 1:
                result.append(0)
            elif curr_sum == 1 and carry == 0:
                result.append(1)
            elif curr_sum == 2 and carry == 1:
                result.append(1)
            elif curr_sum == 2 and carry == 0:
                result.append(0)
                carry = 1
            i -= 1
            j -= 1

        # add carry and whatever is left of number 1 or number 2
        while i > -1:
            curr1 = int(num1[i])
            curr_sum = curr1 + carry
            if curr_sum == 2:
                result.append(0)
            else:
                result.append(curr_sum)
                carry = 0
            i -= 1
        while j > -1:
            curr2 = int(num2[j])
            curr_sum = curr2 + carry
            if curr_sum == 2:
                result.append(0)
            else:
                result.append(curr_sum)
                carry = 0
            j -= 1
        if carry:
            result.append(carry)

        result.reverse()
        return "".join(map(str, result))


if __name__ == "__main__":
    sol = Solution()

    # stress testing solution against naive algorithm
    while True:
        num1 = bin(random.randrange(10**3, 10**6))[2:]
        num2 = bin(random.randrange(10**3, 10**6))[2:]
        naive_result = sol.add_binary_naive(num1, num2)
        result = sol.add_binary(num1, num2)
        if naive_result == result:
            print("OK")
            print(f"{result}")
        else:
            print("Results are different.")
            print(f"number 1: {num1}")
            print(f"number 2: {num2}")
            break
