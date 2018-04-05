""" Problem description can be found here:
https://leetcode.com/problems/reverse-bits/description/
"""


class Solution:
    def reverse_bits_1(self, n):
        """ Python solution using string manipulation.
        """
        return int(bin(n)[2:].zfill(32)[::-1], 2)

    def reverse_bits_2(self, n):
        """ Bit manipulation solution.
        """
        result = 0
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.reverse_bits_1(43261596) == 964176192
    assert sol.reverse_bits_2(43261596) == 964176192
