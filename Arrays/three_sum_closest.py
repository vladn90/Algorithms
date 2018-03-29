""" Problem description can be found here:
https://leetcode.com/problems/3sum-closest/description/

Algorithm description:
1) Sort the array.
2) Choose element i from array.
3) Calculate the sum of two integers(diff), i.e. target sum minus element i.
4) Find the sum of other two integers closest to diff.
4) Update the closest sum of three if needed.
"""


class Solution:
    def threeSumClosest(self, array, target):
        """ Returns sum of integers from array closest to target.
        Time complexity: O(n ^ 2). Space complexity: O(n),
        where n is len(array).
        """
        array.sort()

        n = len(array)
        best_sum = float("inf")  # closest sum of 3 integers so far
        for i in range(n - 2):  # choosing the 1st integer
            if i > 0 and array[i] == array[i - 1]:  # skip duplicates
                continue

            diff = target - array[i]  # best sum for 2 other integers
            x, y = i + 1, n - 1
            best_diff = float("inf")
            while x < y:
                curr_diff = array[x] + array[y]
                if curr_diff == diff:  # exact sum we're looking for
                    return target
                elif curr_diff < diff:  # increase current sum of 2 integers
                    x += 1
                else:  # curr_diff > diff, decrease current sum of 2 integers
                    y -= 1
                # update best difference so far
                if abs(curr_diff - diff) < abs(best_diff - diff):
                    best_diff = curr_diff

            # update best sum if needed
            curr_sum = array[i] + best_diff
            if abs(curr_sum - target) < abs(best_sum - target):
                best_sum = curr_sum
        return best_sum


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    array = [-1, 2, 1, -4]
    target = 1
    assert sol.threeSumClosest(array, target) == 2

    array = [0, 1, 2]
    target = 3
    assert sol.threeSumClosest(array, target) == 3

    array = [-5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9,
             5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3]
    target = -1
    assert sol.threeSumClosest(array, target) == -1

    array = [1, 1, 1, 0]
    target = 100
    assert sol.threeSumClosest(array, target) == 3
