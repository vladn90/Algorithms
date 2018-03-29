""" Problem description can be found here:
https://leetcode.com/problems/remove-element/description/
"""


class Solution:
    def removeElement(self, array, value):
        """ Removes element == value from array. Modifies array in-place.
        Return length of the array consisting of only valid elements.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        i = -1  # current valid element index
        j = 0  # current element index
        while j < n:
            # element = value, skip this element
            if array[j] == value:
                j += 1
            else:
                # put this element next to current valid element
                array[i + 1] = array[j]
                i += 1
                j += 1
        return i + 1


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.removeElement([], 9) == 0
    assert sol.removeElement([1], 1) == 0
    assert sol.removeElement([1, 1, 1], 9) == 3
    assert sol.removeElement([1, 1, 1], 1) == 0
    assert sol.removeElement([1, 1, 2, 2, 1, 2], 1) == 3
    assert sol.removeElement([1, 1, 2, 2, 1, 2], 2) == 3
    assert sol.removeElement([1, 1, 2, 3, 1], 1) == 2
    assert sol.removeElement([1, 1, 2, 3, 9], 9) == 4
