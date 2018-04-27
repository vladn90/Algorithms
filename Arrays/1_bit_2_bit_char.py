""" Problem statement:
https://leetcode.com/problems/1-bit-and-2-bit-characters/description/
"""


class Solution:
    def isOneBitCharacter(self, bits):
        """ Time complexity: O(n). Space complexity: O(1), n is len(bits).
        """
        last = False  # is last seen character 1-bit?
        i = 0
        while i < len(bits):
            if bits[i]:  # current char is 1, hence we can skip the next char
                last = False
                i += 2
            else:  # current char is 0
                last = True
                i += 1
        return last


if __name__ == "__main__":
    sol = Solution()
    func = sol.isOneBitCharacter

    assert func([1, 0, 0]) == True
    assert func([1, 1, 1, 0]) == False
