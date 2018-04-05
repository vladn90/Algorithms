""" Problem description can be found here:
https://www.interviewbit.com/problems/different-bits-sum-pairwise/
and similar problem (with counting only unique pairs) here:
https://leetcode.com/problems/total-hamming-distance/description/

Find the total Hamming distance between all pairs of the given numbers.
"""


class Solution:
    def diff_bits_sum_brute(self, array):
        """ Brute force algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(array).
        """
        m = 1000000007
        total = 0
        n = len(array)
        for i in range(n):
            for j in range(n):
                if i != j:  # since XOR of two equal numbers is 0
                    # calculate current hamming distance and add it to the total
                    curr = bin(array[i] ^ array[j])[2:].count("1")
                    total = (total + (curr % m)) % m
        return total

    def diff_bits_sum(self, array):
        """ Bit manipulation improved algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        m = 1000000007
        total = 0
        n = len(array)
        for i in range(32):
            mask = 1 << i  # mask for ith bit
            set_bits = 0  # count of set bits
            for num in array:
                if num & mask != 0:
                    set_bits += 1
            total = (total + ((set_bits * (n - set_bits) * 2) % m)) % m
        return total


if __name__ == "__main__":
    sol = Solution()

    array = [1, 3, 5]
    assert sol.diff_bits_sum_brute(array) == 8
    assert sol.diff_bits_sum(array) == 8
