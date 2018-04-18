""" Problem statement:
https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
"""
import random


class Solution:
    def find_largest_brute(self, array):
        """ Brute force algorithm. Checks all subarrays.
        Time complexity: O(n ^ 3). Space complexity: O(n), n is len(array).
        """
        x, y = 0, -1  # start, end of largest subarray with zero sum
        n = len(array)
        for i in range(n):
            for j in range(i, n):
                curr_sum = sum(array[i:j + 1])
                if curr_sum == 0 and (j - i + 1) > (y - x + 1):
                    x, y = i, j
        return array[x:y + 1]

    def find_largest(self, array):
        """ Algorithm based on hashing already calculated sum.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        prev_sum = {0: -1}  # cumulative sum: index where it ends
        x, y = 0, -1  # start, end of largest subarray with zero sum
        curr = 0  # current cumulative sum
        for i, num in enumerate(array):
            curr += num
            if curr in prev_sum:  # found a zero sum subarray
                # compare current subarray length with max subarray length
                # length of subarray[i,j] = start_index - end_index + 1
                if i - prev_sum[curr] > y - x + 1:
                    x, y = prev_sum[curr] + 1, i  # update start, end of largest zero sum subarray
            else:  # add current cumulative sum to the dictionary
                prev_sum[curr] = i
        return array[x:y + 1]

    def stress_test(self, func1, func2, n):
        """ Stress tests two functions against each other using random array
        of size n as input.
        """
        while True:
            array = [random.randrange(-100, 100) for i in range(n)]
            res1 = func1(array)
            res2 = func2(array)
            if res1 == res2:
                print("OK")
                print(res1[:10])
            else:
                print("Results are different.")
                print(f"array = {array}")
                print(f"result 1 = {res1}")
                print(f"result 2 = {res2}")
                break


if __name__ == "__main__":
    sol = Solution()

    array = [1, 2, -2, 4, -4]
    assert sol.find_largest_brute(array) == [2, -2, 4, -4]
    assert sol.find_largest(array) == [2, -2, 4, -4]

    # stress testing brute force and hashing based algorithms
    sol.stress_test(sol.find_largest_brute, sol.find_largest, 10**2)
