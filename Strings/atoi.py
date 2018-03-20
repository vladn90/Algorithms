""" Problem description can be found here:
https://leetcode.com/problems/string-to-integer-atoi/description/
"""


class Solution:
    def myAtoi(self, string):
        """ Converts string to an integer.
        input: string
        output: integer
        Time complexity: O(n). Space complexity: O(1), where n is len(string).
        """
        sign = 1
        result = 0
        found = False
        n = len(string)
        for char in string:
            # skip leading spaces
            if not found and char == " ":
                continue
            # negative sign before the integer
            elif not found and char == "-":
                found = True
                sign = -1
            # positive sign before the integer
            elif not found and char == "+":
                found = True
            # character is an integer
            elif char.isdigit():
                found = True
                result = result * 10 + int(char)
                # check if result fits in 32-bit integer
                if result > 2147483647 and sign == 1:
                    return 2147483647
                if result > 2147483648 and sign == -1:
                    return -2147483648
            else:
                break
        return sign * result


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.myAtoi("     ") == 0
    assert sol.myAtoi("") == 0
    assert sol.myAtoi("   +11233  ") == 11233
    assert sol.myAtoi("1234567") == 1234567
    assert sol.myAtoi("       1234567  ") == 1234567
    assert sol.myAtoi("       -1234567  ") == -1234567
    assert sol.myAtoi("   -    1234567  ") == 0
    assert sol.myAtoi("       1234567-  ") == 1234567
    assert sol.myAtoi("   abc1234567  ") == 0
    assert sol.myAtoi("   1234567abc  ") == 1234567
    for i in range(-10**3, 10**3):
        assert sol.myAtoi(str(i)) == i
