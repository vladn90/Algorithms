""" Problem statement:
https://www.interviewbit.com/problems/distinct-numbers-in-window/
"""
import random


class Solution:
    def count_distinct_brute(self, array, k):
        """ Brute force algorithm. Time complexity: O(n * k).
        Space complexity: O(k), n is len(array).
        """
        n = len(array)
        if k > n:
            return []

        result = []
        for i in range(n - k + 1):
            window = set()
            for j in range(i, i + k):
                window.add(array[j])
            result.append(len(window))
        return result

    def count_distinct(self, array, k):
        """ Improved algorithm using dictionary. Time complexity: O(n).
        Space complexity: O(n), n is len(array).
        """
        n = len(array)
        if k > n:
            return []

        window = dict()  # count number occurences in the 1st window
        for i in range(k):
            window[array[i]] = window.get(array[i], 0) + 1

        curr_count = len(window)
        result = [curr_count]
        for i in range(k, n):  # count unique numbers in all other windows
            if array[i] not in window or window[array[i]] == 0:  # add new
                curr_count += 1
            window[array[i]] = window.get(array[i], 0) + 1
            window[array[i - k]] -= 1  # delete old
            if window[array[i - k]] == 0:
                curr_count -= 1
            result.append(curr_count)
        return result


def stress_test(func1, func2, n):
    """ Stress tests two functions against each other using array of random
    integers of size n.
    """
    while True:
        array = [random.randrange(1, 10**3) for i in range(n)]
        k = random.randrange(1, n + 1)
        res1 = func1(array, k)
        res2 = func2(array, k)
        if res1 == res2:
            print("OK")
            print(res1[:20])
        else:
            print("Different results.")
            print(f"array = {array}")
            print(f"k = {k}")
            print(f"result_1 = {res1}")
            print(f"result_2 = {res2}")
            break


if __name__ == "__main__":
    sol = Solution()
    func = sol.count_distinct

    array = [1, 2, 1, 3, 4, 3]
    k = 3
    assert func(array, k) == [2, 3, 3, 2]

    # stress_test(sol.count_distinct_brute, sol.count_distinct, 10**3)
