""" Problem statement:
https://leetcode.com/problems/gray-code/description/
https://www.interviewbit.com/problems/gray-code/
"""


class Solution:
    def grayCode(self, n):
        """ Direct implementation of the algorithm described at wikipedia.
        """
        if n == 0:
            return [0]
        result = [""]
        for i in range(n):
            result = ["0" + num for num in result] + ["1" + num for num in reversed(result)]
        return [int(num, 2) for num in result]

    def grayCode(self, n):
        """ Improved implementation using bitwise operations.
        """
        result = [0]
        for i in range(n):
            result += [result[j] | 1 << i for j in range(len(result) - 1, -1, -1)]
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.grayCode

    n = 3
    result = func(n)
    for num in result:
        print(bin(num)[2:].zfill(n), num)
