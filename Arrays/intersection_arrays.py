""" Problem description can be found here:
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""


class Solution:
    def intersect_1(self, nums1, nums2):
        """ Returns an array of elements appearing both in nums1 and nums2.
        Naive algorithm.
        Time complexity: O(n * m). Space complexity: O(min(m, n)), where
        n, m are len(nums1), len(nums2).
        """
        if not nums1 or not nums2:
            return []

        len1, len2 = len(nums1), len(nums2)
        result = []
        seen = set()  # indices of elements that've already been added to result
        for i in range(len1):
            for j in range(len2):
                if j not in seen and nums1[i] == nums2[j]:
                    seen.add(j)
                    result.append(nums1[i])
                    break
        return result

    def intersect_2(self, nums1, nums2):
        """ Returns an array of elements appearing both in nums1 and nums2.
        Improved algorithm.
        Time complexity: O(n * lg(n) + m * lg(m)). Space complexity: O(n + m),
        where n, m are len(nums1), len(nums2).
        """
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()
        len1, len2 = len(nums1), len(nums2)
        result = []
        i, j = 0, 0
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

    def intersect_3(self, nums1, nums2):
        """ Returns an array of elements appearing both in nums1 and nums2.
        Improved algorithm.
        Time complexity: O(n + m). Space complexity: O(n),
        where n, m are len(nums1), len(nums2).
        """
        if not nums1 or not nums2:
            return []

        dict_nums1 = {}
        for n in nums1:
            dict_nums1[n] = dict_nums1.get(n, 0) + 1

        result = []
        for n in nums2:
            if n in dict_nums1 and dict_nums1[n] > 0:
                result.append(n)
                dict_nums1[n] -= 1
        return result


if __name__ == "__main__":
    sol = Solution()

    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(sol.intersect_3(nums1, nums2))
