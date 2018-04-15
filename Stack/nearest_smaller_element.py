""" Problem statement:
https://www.interviewbit.com/problems/nearest-smaller-element/
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, array):
        """ Algorithm based on using stack.
        Time complexity: O(n). Space complexity: O(n), n is len(array).
        """
        stack = []
        result = []
        for num in array:
            # see of there's integer smaller than num in the stack
            while stack and stack[-1] >= num:
                stack.pop()
            if stack:  # found the smaller integer
                result.append(stack[-1])
            else:  # stack is empty, smaller integer wasn't found
                result.append(-1)
            stack.append(num)  # push current num to the stack
        return result

    def prevSmaller(self, array):
        """ Dynamic programming algorithm. The idea is to use output array to
        store previous smaller integers, hence stack isn't needed.
        Time complexity: O(n). Space complexity: O(1), n is len(array),
        space used for output array isn't included.
        """
        result = [-1]  # since there are no integers to the left of 1st integer
        for i in range(1, len(array)):
            # check if previous integer is smaller than current
            if array[i - 1] < array[i]:
                result.append(array[i - 1])
                continue
            # check if there's a smaller integer to the left in resulting array
            for j in range(len(result) - 1, -1, -1):
                if result[j] < array[i] or result[j] == -1:
                    result.append(result[j])
                    break
        return result


if __name__ == "__main__":
    sol = Solution()
    func = sol.prevSmaller

    # tests
    assert func([4, 5, 2, 10, 8]) == [-1, 4, -1, 2, 2]
    assert func([3, 2, 1]) == [-1, -1, -1]
    assert func([1, 2, 3, 4, 5, 6, 7, 8]) == [-1, 1, 2, 3, 4, 5, 6, 7]
    assert func([1, 2, 3, 1, 2, 3, 1, 2, 3]) == [-1, 1, 2, -1, 1, 2, -1, 1, 2]
    assert func([3, 2, 1, 3, 2, 1, 3, 2, 1]) == [-1, -1, -1, 1, 1, -1, 1, 1, -1]
    assert func([2, 2, 2]) == [-1, -1, -1]
