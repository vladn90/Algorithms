""" Problem description can be found here:
https://leetcode.com/problems/maximum-gap/description/
"""
import math


class Solution:
    def maximumGap(self, nums):
        """ Returns the maximum gap between elements if array nums was sorted.
        Algorithm based on bucket sorting.
        Time complexity: O(n). Space complexity: O(b), where
        n is the length of array nums, b is the size of each bucket.
        """
        n = len(nums)
        # special case, empty array
        if n < 2:
            return 0

        # find the maximum and minimum element in the array
        max_num, min_num = max(nums), min(nums)
        # special case, only 1 unique number
        if max_num == min_num:
            return 0

        # calculate bucket size and number of buckets
        b = math.ceil((max_num - min_num) / (n - 1))
        k = (max_num - min_num) // b + 1

        buckets = [[None, None] for i in range(k)]  # initialize array of buckets
        # put min and max number in each bucket
        for num in nums:
            i = math.floor((num - min_num) / b)  # bucket index for current num
            if not buckets[i][0]:  # bucket doesn't have a minimum element yet
                buckets[i][0] = num
            else:
                buckets[i][0] = min(buckets[i][0], num)
            if not buckets[i][1]:  # bucket doesn't have a maximum element yet
                buckets[i][1] = num
            else:
                buckets[i][1] = max(buckets[i][1], num)

        # compare last(max) number of previous bucket with the first(min)
        # number of the current bucket
        last = buckets[0][-1]
        i = 1  # start from the 2nd bucket
        max_gap = 0
        while i < k:
            # find 1st non-empty bucket
            while not buckets[i][0] and i < k:
                i += 1
            if i == k:
                break
            # found the bucket, calculate the gap, update the max gap
            first = buckets[i][0]
            max_gap = max(max_gap, first - last)
            # set current bucket's max element as a new last and move on
            last = buckets[i][-1]
            i += 1

        return max_gap


if __name__ == "__main__":
    sol = Solution()

    # simple tests
    assert sol.maximumGap([9, 19, 13, 12, 33, 41, 22]) == 11
    assert sol.maximumGap([1, 2, 3]) == 1
    assert sol.maximumGap([9, 9, 9, 8, 7, 7, 8]) == 1
    assert sol.maximumGap([1, 1, 1, 1]) == 0
    assert sol.maximumGap([1, 10000000]) == 9999999
