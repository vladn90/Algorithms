""" Problem description can be found here:
https://leetcode.com/problems/3sum/description/
"""
import random


class Solution:
    def three_sum(self, array):
        """ Returns array of tuples of unique integers a, b, c from array,
        such as a + b + c = 0. Algorithm description:
        1) Sort the array.
        2) Fix integer a at position i.
        3) Find two other integers b and c at positions i and i + 1, such as
        b + c = -a, i.e. a + b + c = 0.

        Time complexity: O(n ^ 2). Space complexity: O(n),
        where n is len(array).
        """
        array.sort()

        result = []
        n = len(array)
        for i in range(n - 2):  # choose integer a
            # skip duplicates of previous a
            if i > 0 and array[i] == array[i - 1]:
                continue

            sum_two = -array[i]
            x, y = i + 1, n - 1
            while x < y:  # choose integers b and c, two sum problem
                # skip duplicates of previous b and c
                if x > i + 1 and array[x] == array[x - 1]:
                    x += 1
                    continue
                elif y < n - 1 and array[y] == array[y + 1]:
                    y -= 1
                    continue

                curr_two = array[x] + array[y]
                if curr_two < sum_two:
                    x += 1
                elif curr_two > sum_two:
                    y -= 1
                else:  # current sum == sum_two
                    result.append((array[i], array[x], array[y]))
                    x += 1
                    y -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    array = [-1, 0, 1, 2, -1, -4, -1, 2]
    print(sol.three_sum(array))

    # self-checking the solution
    while True:
        array = [random.randrange(-10, 10) for i in range(10**2)]
        result = sol.three_sum(array)
        assert len(set(result)) == len(result)  # no duplicates
        for arr in result:
            assert sum(arr) == 0  # a + b + c == 0
        print(result)
