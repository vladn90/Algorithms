""" Problem statement:
https://www.interviewbit.com/problems/painters-partition-problem/
"""


class Solution:
    def count_painters(self, array, max_length):
        """ Returns total number of painters, that we're gonna need if we use
        max_length as maximum boards' length that each painter is gonna paint.

        Time complexity: O(n). Space complexity: O(1), n is len(array).
        """
        total = 0  # count of total length for current painter
        painters = 1  # painters count
        for length in array:
            total += length
            if total > max_length:
                painters += 1
                total = length
        return painters

    def paint(self, k, t, array):
        """ Returns minimum time required to paint all the boards.
        Time complexity: O(n * lg(sum(array))). Space complexity: O(1),
        n is len(array).
        """
        low = max(array)
        high = sum(array)
        while low < high:
            mid = (low + high) // 2  # current max board's length per painter
            painters = self.count_painters(array, mid)
            if painters <= k:  # search in left half, including current mid
                high = mid
            else:  # search in right half, discard the mid
                low = mid + 1
        m = 10000003
        return ((low % m) * (t % m)) % m


if __name__ == "__main__":
    sol = Solution()
    array = [100, 200, 300, 400, 500, 600, 700, 800, 900]
    k = 3
    t = 1
    print(sol.partition(k, t, array))
