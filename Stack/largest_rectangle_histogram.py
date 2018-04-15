""" Problem statement:
https://leetcode.com/problems/largest-rectangle-in-histogram/description/
"""
import random


class SolutionBrute:
    def largest_area(self, heights):
        """ Brute force algorithm. Checks all possible combinations of bars.
        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(heights).
        """
        n = len(heights)
        max_area = 0  # maximum area of rectangle so far
        for i in range(n):
            min_height = heights[i]  # bar with min height in current range[i,j]
            for j in range(i, n):
                if heights[j] < min_height:  # adjust bar with min height if needed
                    min_height = heights[j]
                # calculate current area = width * min_height
                curr_area = (j - i + 1) * min_height
                if curr_area > max_area:  # update max_area if needed
                    max_area = curr_area
        return max_area


class SolutionDC:
    """ Divide and conquer algorithm. Largest rectangle is gonna be either in
    left half, in right half or between left and right halves.
    Time complexity: O(n * lg(n)). Space complexity: O(lg(n)), n is len(heights).
    """

    def largest_area_between(self, heights, start, end, mid):
        max_area = 0
        i, j = mid + 1, mid
        min_height = float("inf")
        while i >= start + 1 and j <= end - 1:
            height_left = min(min_height, heights[i - 1])
            area_left = (j - (i - 1) + 1) * height_left
            height_right = min(min_height, heights[j + 1])
            area_right = (j + 1 - i + 1) * height_right
            if area_left > area_right:
                i -= 1
                min_height = height_left
                max_area = max(max_area, area_left)
            else:
                j += 1
                min_height = height_right
                max_area = max(max_area, area_right)
        while i >= start + 1:
            i -= 1
            min_height = min(min_height, heights[i])
            max_area = max(max_area, (j - i + 1) * min_height)
        while j <= end - 1:
            j += 1
            min_height = min(min_height, heights[j])
            max_area = max(max_area, (j - i + 1) * min_height)
        return max_area

    def largest_area_divide(self, heights, start, end):
        if start == end:  # base case, only one bar
            return heights[start]

        mid = (start + end) // 2
        max_left = self.largest_area_divide(heights, start, mid)
        max_right = self.largest_area_divide(heights, mid + 1, end)
        max_between = self.largest_area_between(heights, start, end, mid)
        return max(max_left, max_right, max_between)

    def largest_area(self, heights):
        if not heights:
            return 0
        return self.largest_area_divide(heights, 0, len(heights) - 1)


class SolutionDP:
    def largest_area(self, heights):
        """ Dynamic programming algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(heights).
        """
        n = len(heights)
        # calculate left array, where left[i] is an index of the first bar to
        # the left of heights[i] that is smaller than heights[i]
        left = [-1] * n  # left[i] = -1 if there's no such bar
        for i in range(1, n):
            # check if previous bar is lower
            if heights[i - 1] < heights[i]:
                left[i] = i - 1
                continue
            # look for the 1st smaller bar in left array
            for j in range(i - 1, -1, -1):
                if left[j] == -1 or heights[left[j]] < heights[i]:
                    left[i] = left[j]
                    break

        # calculate right array, where right[i] is an index of the first bar to
        # the right of heights[i] that is smaller than heights[i]
        right = [n] * n  # right[i] = n if there's no such bar
        for i in range(n - 2, -1, -1):
            # check if next bar is lower
            if heights[i + 1] < heights[i]:
                right[i] = i + 1
                continue
            # look for the 1st smaller bar in right array
            for j in range(i + 1, n):
                if right[j] == n or heights[right[j]] < heights[i]:
                    right[i] = right[j]
                    break

        # compute the total area of rectangle consisting only of bars heights[i]
        max_area = 0  # keep track of maximum area so far
        for i in range(n):
            width = right[i] - left[i] - 1  # width of the current rectangle
            area = width * heights[i]  # area of current rectangle
            if area > max_area:
                max_area = area
        return max_area


class SolutionStack:
    def largest_area(self, heights):
        """ Stack based algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(heights).
        """
        stack = [-1]  # stack with indices of previous bars
        max_area = 0
        for i, curr_height in enumerate(heights):
            # if stack[-1] == -1, i.e. stack is empty or current height >= last height
            if stack[-1] == -1 or curr_height >= heights[stack[-1]]:
                stack.append(i)  # push index of current bar to the stack
            # if stack isn't empty and current height < last height
            elif curr_height < heights[stack[-1]]:
                # while stack isn't empty and last height >= current height
                while stack[-1] != -1 and heights[stack[-1]] >= curr_height:
                    # area = width * height
                    curr_area = (i - stack[-2] - 1) * heights[stack.pop()]
                    max_area = max(max_area, curr_area)
                stack.append(i)
        # pop off the stack whatever is left there
        while stack[-1] != -1:  # while stack isn't empty
            curr_area = (len(heights) - stack[-2] - 1) * heights[stack.pop()]
            max_area = max(max_area, curr_area)
        return max_area

    def largest_area(self, heights):
        """ Optimized version of stack based algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(heights).
        """
        stack = [-1]
        max_area = 0
        stack_app = stack.append  # optimization
        for i, curr_height in enumerate(heights):
            if stack[-1] == -1 or curr_height >= heights[stack[-1]]:
                stack_app(i)
            elif curr_height < heights[stack[-1]]:
                while stack[-1] != -1 and heights[stack[-1]] >= curr_height:
                    curr_area = (i - stack[-2] - 1) * heights[stack.pop()]
                    if curr_area > max_area:
                        max_area = curr_area
                stack_app(i)
        while stack[-1] != -1:
            curr_area = (len(heights) - stack[-2] - 1) * heights[stack.pop()]
            if curr_area > max_area:
                max_area = curr_area
        return max_area


def stress_test(func1, func2, n):
    """ Stress testing func1 against func2 on a random input of size n.
    """
    while True:
        heights = [random.randrange(1, 10**6) for i in range(n)]
        res1 = func1(heights)
        res2 = func2(heights)
        if res1 == res2:
            print("OK")
            print(res1)
        else:
            print(f"heights = {heights}")
            print(f"result 1 = {res1}")
            print(f"result 2 = {res2}")
            break


if __name__ == "__main__":
    sol_brute = SolutionBrute()
    sol_stack = SolutionStack()
    func = sol_stack.largest_area

    assert func([2, 1, 5, 6, 2, 3]) == 10
    assert func([1, 2, 3, 4, 5]) == 9
    assert func([5, 4, 3, 2, 1]) == 9
    assert func([1, 2, 3, 1, 2, 3]) == 6
    assert func([4, 1, 3, 4, 4]) == 9
    assert func([6, 2, 5, 4, 5, 1, 6]) == 12
    assert func([3, 2, 2, 4, 4]) == 10
    assert func([]) == 0

    # stress testing brute force algorithm against fast stack-based algorithm
    func1 = sol_brute.largest_area
    func2 = sol_stack.largest_area
    stress_test(func1, func, 100)
