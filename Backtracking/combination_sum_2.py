""" Problem statement:
https://leetcode.com/problems/combination-sum-ii/description/
https://www.interviewbit.com/problems/combination-sum-ii/
"""


class SolutionLeetCode:
    def combinationSum2(self, candidates, target):
        """ Recursive backtracking algorithm.
        """
        def helper(candidates, target, arr, start, result):
            if not target:
                result.add(tuple(arr))
                return True
            if target < 0:
                return True
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                res = helper(candidates, target - candidates[i], arr, i + 1, result)
                arr.pop()  # backtracking
                if res:
                    break

        candidates.sort()
        result = set()  # so we avoid duplicate combinations
        helper(candidates, target, [], 0, result)
        return list(result)


class SolutionInterviewbit:
    # @param candidates : list of integers
    # @param target : integer
    # @return a list of list of integers
    def combinationSum(self, candidates, target):
        """ Recursive backtracking algorithm.
        """
        def helper(candidates, target, arr, start, result):
            if not target:
                result.add(tuple(arr))
                return True
            if target < 0:
                return True
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                res = helper(candidates, target - candidates[i], arr, i + 1, result)
                arr.pop()  # backtracking
                if res:
                    break

        candidates.sort()
        result = set()  # so we avoid duplicate combinations
        helper(candidates, target, [], 0, result)
        return list(result)


if __name__ == "__main__":
    sol = SolutionLeetCode()
    func = sol.combinationSum2

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = func(candidates, target)
    for arr in result:
        print(arr)

    candidates = [2, 5, 2, 1, 2]
    target = 5
    result = func(candidates, target)
    for arr in result:
        print(arr)
