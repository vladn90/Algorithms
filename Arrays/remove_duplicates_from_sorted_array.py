""" Problem description can be found here:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/solution/

Algorithm description can be found here:
https://leetcode.com/articles/remove-duplicates-sorted-array/
"""


class Solution:
    def removeDuplicates(self, array):
        """ Removes duplicates from array and returns length of modified array.
        Modifies original array in-place. Two pointers algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        # special case, empty array
        if n == 0:
            return 0

        i = 0  # position of current unique element
        j = 1  # position of current element's duplicate
        while j < n:
            if array[j] == array[i]:
                j += 1
            else:
                array[i + 1] = array[j]
                i += 1
                j += 1
        return i + 1  # length of array without duplicates


if __name__ == "__main__":
    sol = Solution()
    array = [1, 1, 1, 2, 2, 4, 5, 6, 6]
    print(sol.removeDuplicates(array))
