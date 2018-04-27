""" Problem statement:
https://leetcode.com/problems/palindrome-partitioning/description/
https://www.interviewbit.com/problems/palindrome-partitioning/

Algorithm description:
1) Check every substring starting from the 1st character if it's a palindrome.
2) If it is, then recursively check every other substring starting from the next index.
3) If it's not, keep checking until we find first palindrome.
4) There always gonna be at least partition since 1-letter string is a palindrome.
"""


class Solution:
    def is_palindrome(self, string, i, j):
        """ Returns True if string from index i to j is a palindrome,
        False otherwise.
        """
        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        return True

    def find_partition(self, string, start, curr_res, result):
        """ Helper function for function partition.
        """
        if start == len(string):
            result.append(curr_res[:])
            return
        for i in range(start, len(string)):
            if self.is_palindrome(string, start, i):
                curr_res.append(string[start:i + 1])
                self.find_partition(string, i + 1, curr_res, result)
                curr_res.pop()  # backtracking

    def partition(self, string):
        """ Returns an array of all possible partitions of string such that
        each partition is a palindrome.
        """
        result = []
        self.find_partition(string, 0, [], result)
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.partition

    string = "aabb"
    result = func(string)
    for arr in result:
        print(arr)
