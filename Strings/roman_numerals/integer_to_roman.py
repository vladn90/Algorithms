""" Problem description can be found here:
https://leetcode.com/problems/integer-to-roman/description/
"""


class Solution:
    def int_to_roman(self, number):
        """ Converts a decimal integer to Roman numeral.

        input: integer
        output: string
        Time complexity: O(lg(number)). Space complexity: O(1).
        """
        if number < 1 or number > 3999:
            raise Exception("Input number should be in range[1:3999]")

        # integer to roman hash map
        int_roman = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
                     6: "VI", 7: "VII", 8: "VIII", 9: "IX",
                     10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L",
                     60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
                     100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D",
                     600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
                     1000: "M", 2000: "MM", 3000: "MMM"}

        result = []
        k = 1
        while number != 0:
            n = (number % 10) * k
            if n != 0:
                result.append(int_roman[n])
            number //= 10
            k *= 10

        result.reverse()
        return "".join(result)


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.int_to_roman(5) == "V"
    assert sol.int_to_roman(9) == "IX"
    assert sol.int_to_roman(20) == "XX"
    assert sol.int_to_roman(1776) == "MDCCLXXVI"
    assert sol.int_to_roman(1954) == "MCMLIV"
    assert sol.int_to_roman(1990) == "MCMXC"
    assert sol.int_to_roman(1991) == "MCMXCI"
    assert sol.int_to_roman(2014) == "MMXIV"
