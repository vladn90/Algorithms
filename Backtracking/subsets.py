""" Problem statement:
https://leetcode.com/problems/subsets/description/
https://www.interviewbit.com/problems/subset/
"""


class SolutionLeetcode:
    def subsets_brute(self, nums):
        """ Returns an array of tuples, where each tuple is a subset of original
        array nums.
        """
        result = set()  # so we don't have duplicate subsets
        result.add(tuple())  # add empty subset to result

        def find_subsets(array):
            """ Adds all subsets of array to result.
            """
            if not array:  # base case
                return
            result.add(tuple(array))  # add the whole array as subset
            for i in range(len(array)):
                find_subsets(array[:i] + array[i + 1:])  # exclude i from each subset

        find_subsets(nums)
        return result

    def subsets_brute(self, nums):
        """ Returns an array of tuples, where each tuple is a subset of original
        array nums.
        """
        original = set(nums)
        result = set()  # so we don't have duplicate subsets
        result.add(tuple())  # add empty subset to result

        def find_subsets(original):
            """ Adds all subsets of array to result.
            """
            if not original:  # base case
                return
            result.add(tuple(original))
            for num in original:
                original.remove(num)
                find_subsets(original)  # exclude num from each subset
                original.add(num)  # backtracking

        find_subsets(original)
        return result

    def subsets_fast(self, nums):
        """ Bottom-up dynamic programming approach.
        Time complexity: O(n * 2 ^ n). Space complexity: O(2 ^ n), n is len(nums).
        """
        result = [[]]  # start with an empty set(array in our case)
        for num in nums:
            new = []  # new array of subsets
            for arr in result:
                new.append(arr + [num])
            result.extend(new)
        return result

    def subsets_fast(self, nums):
        """ Bottom-up dynamic programming approach. Shorter and faster version.
        Time complexity: O(n * 2 ^ n). Space complexity: O(2 ^ n), n is len(nums).
        """
        result = [[]]
        for num in nums:
            result += [arr + [num] for arr in result]
        return result


class SolutionInterviewBit:
    def subsets(self, nums):
        """ Bottom-up dynamic programming approach.
        Time complexity: O(n * 2 ^ n). Space complexity: O(2 ^ n), n is len(nums).
        """
        nums.sort()
        result = [[]]
        for num in nums:
            result += [arr + [num] for arr in result]
        return sorted(result)


if __name__ == "__main__":
    sol = SolutionInterviewBit()
    func = sol.subsets

    nums = [1, 2, 3]
    assert func(nums) == [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
