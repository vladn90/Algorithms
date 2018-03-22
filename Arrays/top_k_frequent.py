""" Problem description can be found here:
https://leetcode.com/problems/top-k-frequent-elements/description/
"""


class Solution:
    def topKFrequent(self, nums, k):
        """ Returns an array of top k frequent elements.
        Time complexity: O(n + u * lg(u)). Space complexity: O(u), where
        n is the length of array nums, u is number of unique elements in nums.
        """
        freq = {}  # frequency hash map; number: frequency
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        # create an array of unique numbers sorted in decreasing order
        # by their frequency, based on freq hash map
        numbers = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        return numbers[:k]


if __name__ == "__main__":
    sol = Solution()
    assert sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
