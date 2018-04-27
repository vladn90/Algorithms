""" Problem statement:
https://leetcode.com/problems/combination-sum/description/
https://www.interviewbit.com/problems/combination-sum/
"""


class SolutionLeetCode:
    def combinationSum(self, candidates, target):
        """ Recursive backtracking algorithm.
        """
        candidates.sort()

        def helper(candidates, target, start, arr, curr_sum, result):
            if curr_sum == target:
                result.append(arr[:])
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                curr_sum += candidates[i]
                helper(candidates, target, i, arr, curr_sum, result)
                curr_sum -= arr.pop()  # backtracking

        result = []
        helper(candidates, target, 0, [], 0, result)
        return result

    def combinationSum(self, candidates, target):
        """ Same as above but instead of keeping track of a new variable with
        current sum, we can just substract current value from target. If target
        equals exactly 0, then we found our combination. If it's less than 0,
        it means current sum is too big already.
        And we can optimize solution further by breaking out of the loop whenever
        previous sum was too big already.
        """
        candidates = sorted(set(candidates))

        def helper(candidates, target, start, arr, result):
            if not target:
                result.append(arr[:])
                return True  # see code below for explanation
            if target < 0:
                return True
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                res = helper(candidates, target - candidates[i], i, arr,  result)
                arr.pop()  # backtracking
                # line below means we've already had sum >= target, hence
                # there's no need to look further, so we either quit completely
                # or backtrack, i.e. go the previous function on the call stack
                if res:
                    break

        result = []
        helper(candidates, target, 0, [], result)
        return result


class SolutionInterviewbit:
    def combinationSum(self, candidates, target):
        candidates = sorted(set(candidates))

        def helper(candidates, target, start, arr, curr_sum, result):
            if curr_sum == target:
                result.add(tuple(arr))
                return
            if curr_sum > target:
                return
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                curr_sum += candidates[i]
                helper(candidates, target, i, arr, curr_sum, result)
                curr_sum -= arr.pop()  # backtracking

        result = set()
        helper(candidates, target, 0, [], 0, result)
        return sorted(result)


if __name__ == "__main__":
    sol = SolutionInterviewbit()
    func = sol.combinationSum

    candidates = [2, 3, 6, 7]
    target = 7
    assert func(candidates, target) == [(2, 2, 3), (7,)]

    candidates = [2, 3, 5]
    target = 8
    assert func(candidates, target) == [(2, 2, 2, 2), (2, 3, 3), (3, 5)]

    # good test case to check for duplicate sets in result
    candidates = [7, 8, 10, 6, 11, 1, 16, 8]
    target = 28
