""" Problem decription can be found here:
https://leetcode.com/problems/zigzag-conversion/description/
"""


class Solution:
    def zigzag_convert(self, string, rows):
        """ Returns zigzagged string.
        Time complexity: O(n). Space complexity: O(n), where n is len(string).
        """
        # special case, empty string
        if not string:
            return ""
        # special case, one character in each row = original string
        if rows >= len(string) or rows == 1:
            return string

        result = [[] for i in range(rows)]
        down = True  # direction of filling in rows in result array
        i = 0  # start with the 1st row
        for char in string:
            if i == rows:  # last row, change direction to up
                down = False
                i -= 2
            elif i == -1:  # first row, change direction to down
                down = True
                i += 2
            # add character to the current row
            result[i].append(char)
            # increase or decrease row, depeneding on direction
            if down:
                i += 1
            else:
                i -= 1
        result = "".join(map("".join, result))
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.zigzag_convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert sol.zigzag_convert("ABCD", 2) == "ACBD"
    assert sol.zigzag_convert("ABCD", 4) == "ABCD"
    assert sol.zigzag_convert("ABCD", 1) == "ABCD"
    assert sol.zigzag_convert("", 99) == ""
