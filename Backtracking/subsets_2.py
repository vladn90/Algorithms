""" Problem statement:
https://leetcode.com/problems/subsets-ii/description/
https://www.interviewbit.com/problems/subsets-ii/
"""


class SolutionLeetcode:
    def subsetsWithDup(self, nums):
        """ Time complexity: O(n * 2 ^ n). Space complexity: O(2 ^ n), n is len(nums).
        """
        result = [[]]  # start with an empty subset
        for integer in nums:
            result += [sorted(arr + [integer]) for arr in result]
        return list(set(map(tuple, result)))


class SolutionInterviewBit:
    def subsetsWithDup(self, nums):
        """ Time complexity: O(n * 2 ^ n). Space complexity: O(2 ^ n), n is len(nums).
        """
        result = [[]]  # start with an empty subset
        for integer in nums:
            result += [sorted(arr + [integer]) for arr in result]
        return sorted(set(map(tuple, result)))


if __name__ == "__main__":
    sol = SolutionInterviewBit()
    func = sol.subsetsWithDup

    assert func([1, 2, 2]) == [(), (1,), (1, 2), (1, 2, 2), (2,), (2, 2)]

    assert func([4, 4, 4, 1, 4]) == [(), (1,), (1, 4), (1, 4, 4), (1, 4, 4, 4),
                                     (1, 4, 4, 4, 4), (4,), (4, 4), (4, 4, 4),
                                     (4, 4, 4, 4)]
