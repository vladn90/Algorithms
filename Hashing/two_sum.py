""" Problem statement:
https://www.interviewbit.com/problems/2-sum/
"""


class Solution:
    def two_sum(self, array, target):
        """ Hash map based algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        prev = dict()  # previous number: its index(0-based)
        for i, a in enumerate(array):
            b = target - a  # a + b = target
            if b in prev:
                return [prev[b] + 1, i + 1]  # return 1-based indices
            if a not in prev:  # store a number with the smallest index
                prev[a] = i  # hash current number
        return []


if __name__ == "__main__":
    sol = Solution()

    array = [2, 7, 11, 15]
    target = 9
    assert sol.two_sum(array, target) == [1, 2]

    array = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1,
             9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8]
    target = -3
    assert sol.two_sum(array, target) == [4, 8]
