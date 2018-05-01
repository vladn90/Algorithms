""" Problem statement:
https://www.interviewbit.com/problems/n-max-pair-combinations/
"""
import heapq
import random


class Solution:
    def solve_brute(self, arr1, arr2):
        """ Brute force algorithm. Checks all possible sum combinations.
        Time complexity: O(n ^ 2).
        """
        n = len(arr1)
        total_arr = []
        for num1 in arr1:
            for num2 in arr2:
                total_arr.append(num1 + num2)
        total_arr.sort(reverse=True)
        return total_arr[:n]

    def solve(self, arr1, arr2):
        """ Improved algorithm using max heap. Time complexity: O(n * lg(n)).
        """
        n = len(arr1)
        if not n:  # edge case, empty arrays
            return []

        arr1.sort()
        arr2.sort()

        # initial max combination, 2 largets values from both arrays
        heap = [(-(arr1[n - 1] + arr2[n - 1]), n - 1, n - 1)]
        result = []
        indices = set((n - 1, n - 1))  # combinations' indices that we've already checked
        while len(result) < n:
            # current combination sum, index of element in arr1, in arr2
            curr, i, j = heapq.heappop(heap)
            result.append(-curr)  # negate value since we're using Python built-in min heap
            if (i, j - 1) not in indices:
                heapq.heappush(heap, (-(arr1[i] + arr2[j - 1]), i, j - 1))
                indices.add((i, j - 1))
            if (i - 1, j) not in indices:
                heapq.heappush(heap, (-(arr1[i - 1] + arr2[j]), i - 1, j))
                indices.add((i - 1, j))
        return result


def stress_test(func1, func2, n):
    """ Stress tests two functions against each other using two random arrays
    of size n.
    """
    while True:
        arr1 = [random.randrange(1, 10) for i in range(n)]
        arr2 = [random.randrange(1, 10) for i in range(n)]
        res1 = func1(arr1, arr2)
        res2 = func2(arr1, arr2)
        if res1 == res2:
            print("OK")
            print(res1[:10])
        else:
            print("Different results.")
            print(f"n = {n}")
            print(f"arr1 = {arr1}")
            print(f"arr2 = {arr2}")
            print(f"result 1 = {res1}")
            print(f"result 2 = {res2}")
            break


if __name__ == "__main__":
    sol = Solution()
    func = sol.solve

    arr1 = [1, 4, 2, 3]
    arr2 = [2, 5, 1, 6]
    assert func(arr1, arr2) == [10, 9, 9, 8]

    arr1 = [3, 1, 3, 1]
    arr2 = [1, 4, 1, 4]
    assert func(arr1, arr2) == [7, 7, 7, 7]

    arr1 = [2, 3, 3, 4, 4, 4, 4, 8, 9, 9]
    arr2 = [1, 2, 2, 5, 5, 7, 7, 7, 8, 9]
    assert func(arr1, arr2) == [18, 18, 17, 17, 17, 16, 16, 16, 16, 16]

    stress_test(sol.solve_brute, sol.solve, 10)
