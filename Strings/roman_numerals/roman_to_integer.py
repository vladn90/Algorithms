""" Problem description can be found here:
https://leetcode.com/problems/roman-to-integer/description/
"""


class Solution:
    def roman_to_int(self, string):
        """ Converts Roman numerals to decimal integer. Intuitive algorithm.
        Algorithm description:
        1) Scan the string from left to right.
        2) If the value of current Roman character is less than the value of
        next Roman character, it means that we need to take 2 characters
        to evaluate number.
        3) Otherwise, we take only 1 character and evaluate it's number using
        hash map.
        4) Add current value to the resulting number.

        input: string
        output: integer

        Time complexity: O(n). Space complexity: O(1), where n is len(string).
        """
        # roman to integer hash map
        roman_int = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
                     'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                     'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        result = 0
        i = 0
        n = len(string)
        while i < n:
            if i < (n - 1) and roman_int[string[i]] < roman_int[string[i + 1]]:
                result += roman_int[string[i:i + 2]]
                i += 2
            else:
                result += roman_int[string[i]]
                i += 1
        return result

    def roman_to_int(self, string):
        """ Converts Roman numerals to decimal integer. Optimized algorithm.
        Algorithm description:
        1) Scan the string from left to right, initialize i = 0.
        2) If the value of current Roman character is less than the value of
        next Roman character, substract current value from result,
        add the next value to result, i += 2.
        3) Otherwise, just add current value to result, i += 1.

        input: string
        output: integer

        Time complexity: O(n). Space complexity: O(1), where n is len(string).
        """
        # roman to integer hash map
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
        result = 0
        n = len(string)
        i = 0
        while i < n:
            if i < (n - 1) and roman_int[string[i]] < roman_int[string[i + 1]]:
                result -= roman_int[string[i]]
                result += roman_int[string[i + 1]]
                i += 2
            else:
                result += roman_int[string[i]]
                i += 1
        return result


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.roman_to_int("V") == 5
    assert sol.roman_to_int("IX") == 9
    assert sol.roman_to_int("XX") == 20
    assert sol.roman_to_int("MDCCLXXVI") == 1776
    assert sol.roman_to_int("MCMLIV") == 1954
    assert sol.roman_to_int("MCMXC") == 1990
    assert sol.roman_to_int("MCMXCI") == 1991
    assert sol.roman_to_int("MMXIV") == 2014
