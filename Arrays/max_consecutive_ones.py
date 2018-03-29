""" Problem description can be found here:
https://www.interviewbit.com/problems/max-continuous-series-of-1s/
"""


class Solution:
    def max_ones_length(self, array, m):
        """ Returns count of maximum consecutive ones that can be achieved by
        flipping m zeroes.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        i, j = 0, 0  # sliding window indices
        curr_ones = 0
        max_ones = 0
        while j < n:
            if array[j]:  # current element is 1, increase 1s count
                curr_ones += 1
                j += 1
                max_ones = max(max_ones, curr_ones)  # update max 1s count
            elif not array[j] and m > 0:  # current element is 0, we can flip it
                curr_ones += 1
                m -= 1
                j += 1
                max_ones = max(max_ones, curr_ones)  # update max 1s count
            else:  # current element is zero and we are out of flips
                if not array[i]:  # start of current 1s sequence is 0
                    m += 1  # increase available flips
                i += 1  # move the left pointer
                curr_ones -= 1  # decrease current 1s count
        return max_ones

    def max_ones_seq(self, array, m):
        """ Returns indices of longest sequence of consecutive 1s that can be
        achieved by flipping m 0s.
        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        n = len(array)
        i, j = 0, 0  # start, end of current consecutive 1s sequence
        x, y = 0, 0  # start, end of longest consecutive 1s sequence
        while j < n:
            if array[j]:  # current element is 1
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                j += 1  # move the right pointer
            elif not array[j] and m > 0:  # current element is 0, we can flip it
                if j - i > y - x:  # update start, end of longest 1s sequence
                    x, y = i, j
                m -= 1  # deacrese number of allowed flips
                j += 1  # move the right pointer
            else:  # current element is zero and we are out of flips
                if not array[i]:  # start of current 1s sequence is 0
                    m += 1  # increase available flips
                i += 1  # move the left pointer
        return list(range(x, y + 1))


if __name__ == "__main__":
    sol = Solution()

    # tests
    array = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    m = 2
    assert sol.max_ones_seq(array, m) == [3, 4, 5, 6, 7, 8, 9, 10]

    array = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
    m = 1
    assert sol.max_ones_seq(array, m) == [6, 7, 8, 9, 10]

    array = [1, 1, 0, 1, 1, 0, 0, 1, 1, 1]
    m = 1
    assert sol.max_ones_seq(array, m) == [0, 1, 2, 3, 4]
