""" Problem description can be found here:
https://www.interviewbit.com/problems/minimize-the-absolute-difference/
"""
import random


class Solution:
    def min_diff_1(self, arr1, arr2, arr3):
        """ Naive algorithm. Returns minimum possible value of
        |max(a, b, c) - min(a, b, c)| and a, b, c.
        Algorithm checks all possible values of a, b, c from three arrays and
        chooses the minimum.

        Time complexity: O(n1 * n2 * n3). Space complexity: O(1),
        where n1, n2, n3 are len(arr1), len(arr2), len(arr3).
        """
        result = float("inf")
        x, y, z = 0, 0, 0
        for a in arr1:
            for b in arr2:
                for c in arr3:
                    curr = abs(max(a, b, c) - min(a, b, c))
                    if curr < result:  # update minimum difference
                        x, y, z = a, b, c
                        result = curr
        return result, (x, y, z)

    def min_diff_2(self, arr1, arr2, arr3):
        """ Improved algorithm. Returns minimum possible value of
        |max(a, b, c) - min(a, b, c)| and a, b, c.
        Algorithm description:
        1) Choose element with minimum value among arrays.
        2) Increase index of that array by 1.
        3) Take other two elements from other arrays, calculate difference.
        4) Update the difference value if needed.
        5) Repeat until all elements are checked.

        Time complexity: O(n1 + n2 + n3). Space complexity: O(1),
        where n1, n2, n3 are len(arr1), len(arr2), len(arr3).
        """
        len1, len2, len3 = len(arr1), len(arr2), len(arr3)
        a, b, c = 0, 0, 0  # best combination of elements so far
        num1, num2, num3 = 0, 0, 0  # current elements
        min_diff = float("inf")  # minimum difference so far

        i1, i2, i3 = 0, 0, 0
        while i1 < len1 and i2 < len2 and i3 < len3:
            num1, num2, num3 = arr1[i1], arr2[i2], arr3[i3]
            if arr3[i3] >= arr1[i1] <= arr2[i2]:  # min in the 1st array
                i1 += 1
            elif arr1[i1] >= arr2[i2] <= arr3[i3]:  # min in the 2nd array
                i2 += 1
            else:  # min in the 3rd array
                i3 += 1

            curr_diff = abs(max(num1, num2, num3) - min(num1, num2, num3))
            if curr_diff < min_diff:  # update min difference
                min_diff = curr_diff
                a, b, c = num1, num2, num3

        return min_diff, (a, b, c)


if __name__ == "__main__":
    sol = Solution()
    arr1 = [1, 4, 5, 8, 10]
    arr2 = [6, 9, 15]
    arr3 = [2, 3, 6, 6]
    assert sol.min_diff_1(arr1, arr2, arr3) == (1, (5, 6, 6))
    assert sol.min_diff_2(arr1, arr2, arr3) == (1, (5, 6, 6))

    # stress testing naive algorithm against improved algorithm
    while True:
        arr1 = [random.randrange(1, 10) for i in range(10)]
        arr2 = [random.randrange(5, 15) for i in range(10)]
        arr3 = [random.randrange(15, 20) for i in range(10)]
        arr1.sort()
        arr2.sort()
        arr3.sort()
        naive_result = sol.min_diff_1(arr1, arr2, arr3)
        improved_result = sol.min_diff_2(arr1, arr2, arr3)
        if naive_result == improved_result:
            print("OK")
            print(naive_result)
        else:
            print("Results are different.")
            print(f"arr1 = {arr1}")
            print(f"arr2 = {arr2}")
            print(f"arr3 = {arr3}")
            print(f"naive result: {naive_result}")
            print(f"improved result: {improved_result}")
            break
