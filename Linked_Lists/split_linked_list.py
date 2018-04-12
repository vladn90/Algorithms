""" Problem statement:
https://leetcode.com/problems/split-linked-list-in-parts/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def splitListToParts(self, root, k):
        """ Returns an array of linked lists, i.e. [root1, root2...].
        Time complexity: O(n). Space complexity: O(1), n is len(linked list),
        size of the output array isn't included in space complexity.
        """
        # find length of the linked list using slow and fast pointer algorithm
        slow = fast = root
        length = 1  # index of slow pointer node, 1-based
        while True:
            if not fast:
                length = (length - 1) * 2  # even length list
                break
            elif not fast.next:
                length = length * 2 - 1  # odd length list
                break
            length += 1
            slow = slow.next
            fast = fast.next.next
        n = length // k  # number of nodes in each linked list in array
        r = length % k  # number of remaining nodes to split among linked lists

        # split linked list into smaller lists and put them into array
        result = [ListNode("") for i in range(k)]  # initialize an array of dummy nodes
        i = 0  # index of current linked list in array
        curr = root
        while curr:
            dummy = result[i]  # current dummy node
            for j in range(n):
                dummy.next = curr
                dummy = dummy.next
                curr = curr.next
            if r:  # while we still have remaining nodes
                r -= 1
                dummy.next = curr
                curr = curr.next
                dummy = dummy.next
            dummy.next = None  # detach current linked list from original list
            result[i] = result[i].next  # move pointer to the 1st node
            i += 1
        return result
