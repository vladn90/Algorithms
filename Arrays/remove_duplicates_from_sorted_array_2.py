""" Problem description can be found here:
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
"""


class Solution:
    def removeDuplicates(self, array):
        """ Modifies array in-place so that each element can have only one
        duplicate.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        # special case, empty array
        if not array:
            return 0

        n = len(array)
        i = 0  # index of the last unique element or its 1st duplicate
        j = 1  # index of current element
        d = 1  # number of duplicates of current element i
        while j < n:
            if array[j] == array[i]:
                if d == 1:
                    d += 1
                    array[i + 1] = array[i]
                    i += 1
                j += 1
            else:
                array[i + 1] = array[j]
                d = 1
                j += 1
                i += 1
        return i + 1


if __name__ == "__main__":
    sol = Solution()
    array = [1, 1, 1, 2, 2, 2, 3, 3]
    new_length = sol.removeDuplicates(array)
    print(f"new length = {new_length}")
    print(f"new array = {array}")
