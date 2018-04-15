""" Problem statement:
https://leetcode.com/problems/sliding-window-maximum/description/
"""
import random
from collections import deque


class Solution:
    def max_window_brute(self, nums, k):
        """ Brute force algorithm.
        Time complexity: O(n * k). Space complexity: O(1), n is len(nums).
        """
        n = len(nums)
        max_window = []
        for i in range(0, n - k + 1):
            curr_max = float("-inf")
            for j in range(i, i + k):  # find max in current window
                curr_max = max(curr_max, nums[j])
            max_window.append(curr_max)
        return max_window

    def max_window_deque(self, nums, k):
        """ Algorithm based on using dequeue. Assumes k <= len(nums).
        Time complexity: O(n). Space complexity: O(k), n is len(nums).
        """
        if not nums:  # special case, empty array
            return []
        if k > len(nums):  # special case, k > len(nums)
            return [max(nums)]

        max_window = []  # resulting window
        deq = deque()  # contains indices of the elements of nums
        # add index of elements to the dequeue from the 1st window
        for i in range(k):
            # remove all elements that <= current added element
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()  # remove from the right
            deq.append(i)  # add from the right
        max_window.append(nums[deq[0]])  # add max element from the 1st window

        # loop over nums and check all other windows
        for i in range(k, len(nums)):
            # remove elements that fall out from the current window
            while deq and deq[0] <= i - k:
                deq.popleft()  # remove from the left
            # remove all elements that <= current added element
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            deq.append(i)
            max_window.append(nums[deq[0]])  # add current max to the result
        return max_window


def stress_test(func1, func2, n):
    """ Stress tests two functions against each other on a random input array.
    """
    while True:
        nums = [random.randrange(1, 10**6) for i in range(n)]
        k = random.randrange(1, n + 1)
        res1 = func1(nums, k)
        res2 = func2(nums, k)
        if res1 == res2:
            print("OK")
            print(res1[:10])
        else:
            print(f"nums = {nums}")
            print(f"k = {k}")
            print(f"result 1 = {res1}")
            print(f"result 2 = {res2}")
            break


if __name__ == "__main__":
    sol = Solution()
    func = sol.max_window_deque

    # small tests
    assert func([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert func([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4) == [10, 10, 10, 15, 15, 90, 90]

    # stress testing slow and fast algorithms
    func1 = sol.max_window_brute
    func2 = sol.max_window_deque
    stress_test(func1, func2, 10**2)
