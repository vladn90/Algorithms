""" Problem description can be found here:
https://leetcode.com/problems/valid-triangle-number/description/
"""
import random


class Solution:
    def is_triangle(self, a, b, c):
        """ Returns True if triangle can be built with sides a, b, c,
        False otherwise.
        """
        return a + b > c and a + c > b and b + c > a

    def count_triangles_brute(self, array):
        """ Returns number of triangles possible to build using integers from
        array. Brute force algorithm.
        Time complexity: O(n ^ 3). Space complexity: O(1),
        where n is len(array).
        """
        n = len(array)
        triangles = 0  # number of possible triangles
        for x in range(n - 2):
            for y in range(x + 1, n - 1):
                for z in range(y + 1, n):
                    if self.is_triangle(array[x], array[y], array[z]):
                        # print(array[x], array[y], array[z])
                        triangles += 1
        return triangles

    def count_triangles_1(self, array):
        """ Returns number of triangles possible to build using integers from
        array. Improved algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(n),
        where n is len(array).
        """
        n = len(array)
        array.sort()

        triangles = 0  # number of possible triangles
        for i in range(n - 2):  # choose 1st side
            if array[i] == 0:
                continue

            k = i + 2  # choose first possible 3rd side
            for j in range(i + 1, n):  # choose 2nd side
                curr_two = array[i] + array[j]
                while k < n and curr_two > array[k]:
                    k += 1
                # z -= 1
                triangles += (k - j - 1)
        return triangles if triangles > 0 else 0

    def binary_search(self, array, n, i, j, k):
        """ Helper function for count_triangles_2. Returns max value of k in
        array starting from index k, such as array[i] + array[j] > array[k].
        Time complexity: O(lg(n)). Space complexity: O(1), where
        n is length of the array[k:end].
        """
        start, end = k, n - 1
        while start <= end:
            mid = (start + end) // 2
            if array[i] + array[j] > array[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return start

    def count_triangles_2(self, array):
        """ Returns number of triangles possible to build using integers from
        array. Improved algorithm.
        Time complexity: O(n ^ 2). Space complexity: O(n),
        where n is len(array).
        """
        n = len(array)
        array.sort()

        triangles = 0  # number of possible triangles
        for i in range(n - 2):  # choose 1st side
            if array[i] == 0:
                continue

            k = i + 2  # choose first possible 3rd side
            for j in range(i + 1, n):  # choose 2nd side
                k = self.binary_search(array, n, i, j, k)
                triangles += (k - j - 1)
        return triangles if triangles > 0 else 0


if __name__ == "__main__":
    sol = Solution()

    # simple check
    solutions = [sol.count_triangles_brute,
                 sol.count_triangles_1,
                 sol.count_triangles_2]
    for s in solutions:
        assert s([2, 2, 3, 4]) == 3
        assert s([2, 2, 3, 3, 4, 5, 6]) == 21
        assert s([0, 1, 0, 1]) == 0
        assert s([0, 0, 0, 1, 1, 1]) == 1

    # stress testing solution x against brute force solution
    solution_x = sol.count_triangles_1
    solution_brute = sol.count_triangles_brute
    while True:
        array = [random.randrange(1, 20) for i in range(100)]
        x_result = solution_x(array)
        brute_result = solution_brute(array)
        if x_result == brute_result:
            print("OK")
            print(x_result)
        else:
            print("Different results.")
            print(f"array = {array}")
            print(f"brute force result: {brute_result}")
            print(f"improved solution result: {x_result}")
            break
