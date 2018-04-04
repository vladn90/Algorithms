""" Problem description can be found here:
https://www.interviewbit.com/problems/array-3-pointers/
"""


class Solution:
    def array_3p_brute(self, arr1, arr2, arr3):
        """ Brute force algorithm.
        Time complexity: O(len1 * len2 * len3). Space complexity: O(1),
        where len1, len2, len3 are len(arr1), len(arr2), len(arr3).
        """
        min_val = float("inf")
        for i in range(len(arr1)):
            for j in range(len(arr2)):
                for k in range(len(arr3)):
                    curr = max(abs(arr1[i] - arr2[j]),
                               abs(arr1[i] - arr3[k]),
                               abs(arr2[j] - arr3[k]))
                    # if curr < min_val:
                    #     print(i, j, k)
                    #     print(arr1[i], arr2[j], arr3[k])
                    #     print()
                    min_val = min(min_val, curr)
        return min_val

    def array_3p(self, arr1, arr2, arr3):
        """ Improved algorithm using 3 pointers technique.
        Time complexity: O(len1 + len2 + len3). Space complexity: O(1),
        where len1, len2, len3 are len(arr1), len(arr2), len(arr3).
        """
        min_val = float("inf")
        i, j, k = 0, 0, 0
        len1, len2, len3 = len(arr1), len(arr2), len(arr3)
        while i < len1 and j < len2 and k < len3:
            curr = max(abs(arr1[i] - arr2[j]),
                       abs(arr1[i] - arr3[k]),
                       abs(arr2[j] - arr3[k]))
            # if curr < min_val:
            #     print(i, j, k)
            #     print(arr1[i], arr2[j], arr3[k])
            #     print()
            min_val = min(min_val, curr)
            if arr2[j] >= arr1[i] <= arr3[k]:
                i += 1
            elif arr1[i] >= arr2[j] <= arr3[k]:
                j += 1
            else:
                k += 1
        return min_val


if __name__ == "__main__":
    sol = Solution()
    func = sol.array_3p

    arr1 = [1, 4, 10]
    arr2 = [2, 15, 20]
    arr3 = [10, 12]
    assert func(arr1, arr2, arr3) == 5

    arr1 = [20, 24, 100]
    arr2 = [2, 19, 22, 79, 800]
    arr3 = [10, 12, 23, 24, 119]
    assert func(arr1, arr2, arr3) == 2
