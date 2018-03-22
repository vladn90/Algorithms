""" Problem description can be found here:
https://leetcode.com/problems/plus-one/description/
"""


class Solution:
    def plusOne(self, digits):
        """ Modifies digits list.
        Time complexity: O(n). Space complexity: O(1), where n is len(digits).
        """
        # add one starting from the rightmost digit
        i = len(digits) - 1
        carry = 1
        while i > -1:
            digits[i] += carry
            carry = digits[i] // 10  # update carry
            digits[i] %= 10  # leave 1 digit in current digit place
            i -= 1
        # add carry if there's any as the 1st digit
        if carry:
            digits.insert(0, carry)
        return digits


if __name__ == "__main__":
    sol = Solution()
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert sol.plusOne([0]) == [1]
    assert sol.plusOne([1, 1, 1]) == [1, 1, 2]
