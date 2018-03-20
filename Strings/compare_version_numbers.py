""" Problem description can be found here:
https://leetcode.com/problems/compare-version-numbers/description/
"""


class Solution:
    def compareVersion(self, version1, version2):
        """ Returns 1 if version1 newer than version2,
                   -1 if version1 older than version2,
                    0 if versions are the same.
        Time complexity: O(n + m). Space complexity: O(1), where
        m, n are the lengths of the strings version1, version2.
        """
        i, j = 0, 0
        n, m = len(version1), len(version2)
        while i < n and j < m:
            # find number in version1
            num1 = 0
            while i < n and version1[i] != ".":
                num1 = num1 * 10 + int(version1[i])
                i += 1
            # find number in version2
            num2 = 0
            while j < m and version2[j] != ".":
                num2 = num2 * 10 + int(version2[j])
                j += 1
            # compare current version numbers
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1

            if i == n or j == m:  # version1 or version2 is finished
                break
            else:  # move on to the next number in version
                i += 1
                j += 1
        # versions are the same so far, so
        # check version numbers from longer version (if there's one)
        # if any of the versions has additional numbers, current i / j is
        # gonna be stopped at ".", so we increase it
        i += 1
        for x in range(i, n):
            if version1[x] == ".":
                continue
            if version1[x] > "0":  # version1 is higher
                return 1
        j += 1
        for x in range(j, m):
            if version2[x] == ".":
                continue
            if version2[x] > "0":  # version2 is higher
                return -1
        return 0  # same versions


if __name__ == "__main__":
    sol = Solution()

    # tests
    assert sol.compareVersion("1", "1") == 0
    assert sol.compareVersion("1", "1.0.0.0.0") == 0
    assert sol.compareVersion("1", "1.0.0.0.0") == 0
    assert sol.compareVersion("1", "1.0.0.0.1") == -1
    assert sol.compareVersion("1", "1.1") == -1
    assert sol.compareVersion("1.0.0.0.1", "1.0.0") == 1
    assert sol.compareVersion("3.6.2", "3.6.1") == 1
