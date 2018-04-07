""" Problem statement:
https://www.interviewbit.com/problems/square-root-of-integer/
"""
import math


class Solution:
    def sqrt(self, n):
        """ Returns sqrt of n.
        Time complexity: O(lg(n)). Space complexity: O(1).
        """
        if n == 1:
            return 1

        start, end = 2, n // 2  # choose a guess between 2 and n // 2
        while start <= end:
            mid = (start + end) // 2  # current guess
            result = mid ** 2
            if result == n:
                return mid
            elif result > n:
                end = mid - 1
            else:
                start = mid + 1
        return end  # returns floor(sqrt(n))


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.sqrt(1) == 1
    for n in range(2, 10**5):
        assert sol.sqrt(n) == int(math.sqrt(n))
