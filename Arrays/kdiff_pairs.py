""" Problem description can be found here:
https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
"""


class Solution:
    def find_pairs_brute(self, nums, k):
        """ Returns number of unique k-diff pairs(i, j) such as |i - j| = k.
        Naive algorithm. Checks all possible pairs of i, j, adds it to the set
        of unique pairs, where each pair is a tuple(min int, max int).

        Time complexity: O(n ^ 2). Space complexity: O(n), where n is len(nums).
        """
        n = len(nums)
        pairs = set()  # set of unique pairs(min integer, max integer)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    pair = (nums[i], nums[j])
                else:
                    pair = (nums[j], nums[i])
                if abs(nums[j] - nums[i]) == k and pair not in pairs:
                    pairs.add(pair)
        return len(pairs)

    def binary_search(self, nums, start, end, b):
        """ Returns True if there's number b in array nums[i:],
        False otherwise.
        """
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == b:
                return True
            elif nums[mid] < b:
                start = mid + 1
            else:
                end = mid - 1
        return False

    def find_pairs_sort(self, nums, k):
        """ Returns number of unique k-diff pairs(i, j) such as |i - j| = k.
        Algorithm description:
        1) Sort the array.
        2) For current smaller number a, find bigger number b = a + k, since
        b - a = k, using binary search.
        3) Add it to the set of unique pairs.

        Time complexity: O(n * lg(n)). Space complexity: O(n), n is len(nums).
        """
        nums.sort()
        pairs = set()
        n = len(nums)
        for i in range(n - 1):
            # b - a = k, a = nums[i], we need to find b = k + a
            b, a = nums[i] + k, nums[i]
            if self.binary_search(nums, i + 1, n - 1, b) and (a, b) not in pairs:
                pairs.add((a, b))
        return len(pairs)

    def find_pairs_hash(self, nums, k):
        """ Returns number of unique k-diff pairs(i, j) such as |i - j| = k.
        Algorithm based on hashing.

        Time complexity: O(n). Space complexity: O(n), n is len(nums).
        """
        num_count = dict()
        for n in nums:
            num_count[n] = num_count.get(n, 0) + 1

        total = 0
        for n in num_count:
            if k == 0 and num_count[n] > 1:
                total += 1
            elif k > 0 and (n + k) in num_count:
                total += 1
        return total


if __name__ == "__main__":
    sol = Solution()

    # tests
    function = sol.find_pairs_sort
    assert function([3, 1, 4, 1, 5], 2) == 2
    assert function([1, 3, 1, 5, 4], 0) == 1
    assert function([1, 1, 1, 1, 1], 0) == 1
