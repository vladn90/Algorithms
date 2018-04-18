""" Problem statement:
https://www.interviewbit.com/problems/equal/
"""
import random


class Solution:
    def equal_brute(self, array):
        """ Brute force algorithm.
        Time complexity: O(n ^ 4). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        result = [n, n, n, n]
        for a in range(n - 1):
            for b in range(a + 1, n):
                for c in range(n - 1):
                    for d in range(c + 1, n):
                        # A1 < C1, B1 != C1, B1 != D1
                        if array[a] + array[b] == array[c] + array[d] and a < c and b != c and b != d:
                            result = min(result, [a, b, c, d])
        return result if result != [n, n, n, n] else []

    def equal_hash(self, array):
        """ Hashing based algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(n), n is len(array).
        """
        n = len(array)
        sums = dict()  # previous sum: start, end indices
        result = [n, n, n, n]
        for i in range(n - 1):
            for j in range(i + 1, n):
                curr_sum = array[i] + array[j]
                if curr_sum in sums:  # we've already seen this sum
                    A1, B1 = sums[curr_sum]
                    if A1 < i and B1 != i and B1 != j:  # A1 < C1, B1 != C1, B1 != D1
                        curr_result = [A1, B1, i, j]
                        result = min(result, curr_result)
                else:
                    sums[curr_sum] = (i, j)  # hash current sum
        return result if result != [n, n, n, n] else []

    def stress_test(self, func1, func2):
        while True:
            array = [random.randrange(1, 10) for i in range(20)]
            res1 = func1(array)
            res2 = func2(array)
            if res1 == res2:
                print("OK")
                print(res1)
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"result 1 = {res1}")
                print(f"result 2 = {res2}")
                break


if __name__ == "__main__":
    sol = Solution()

    assert sol.equal_brute([3, 4, 7, 1, 2, 9, 8]) == [0, 2, 3, 5]
    assert sol.equal_hash([3, 4, 7, 1, 2, 9, 8]) == [0, 2, 3, 5]
    assert sol.equal_brute([3, 1, 4, 1, 4, 2]) == [0, 5, 1, 2]
    assert sol.equal_hash([3, 1, 4, 1, 4, 2]) == [0, 5, 1, 2]
    assert sol.equal_brute([1, 1, 1, 1, 1]) == [0, 1, 2, 3]
    assert sol.equal_hash([1, 1, 1, 1, 1]) == [0, 1, 2, 3]
    assert sol.equal_brute([1, 2, 3]) == []
    assert sol.equal_hash([1, 2, 3]) == []

    sol.stress_test(sol.equal_brute, sol.equal_hash)
