""" Problem statement:
https://leetcode.com/problems/contains-duplicate-iii/description/

Given an array of integers, find out whether there are two distinct indices
i and j in the array such that the absolute difference between
nums[i] and nums[j] is at most t and the absolute difference between
i and j is at most k.
"""


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """ Time complexity: O(n). Space complexity: O(k), n is len(nums).
        """
        # special case
        if k <= 0 or t < 0 or not nums:
            return False

        buckets = dict()
        for i in range(len(nums)):
            curr = nums[i] // (t + 1)  # index of current bucket
            # there's already a number in curr bucket
            if curr in buckets:
                return True
            # there's a number in bucket to the left and their abs <= t
            if curr - 1 in buckets and abs(buckets[curr - 1] - nums[i]) <= t:
                return True
            # there's a number in bucket to the right and their abs <= t
            if curr + 1 in buckets and abs(buckets[curr + 1] - nums[i]) <= t:
                return True
            # else clause, put the number in the new(current) bucket
            buckets[curr] = nums[i]
            # clean the bucket that doesn't fit in current k-size window
            if i >= k:
                del buckets[nums[i - k] // (t + 1)]
        return False


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsNearbyAlmostDuplicate([1, 5, 17, 6, 8], 5, 2) == True
    assert sol.containsNearbyAlmostDuplicate([-3, 3], 2, 4) == False
    assert sol.containsNearbyAlmostDuplicate([1, 3, 1], 1, 1) == False
