""" Problem statement:
https://leetcode.com/problems/linked-list-cycle/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head):
        """ Returns True if there's a cycle in linked list, False otherwise.
        Slow and fast pointer algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        slow = fast = head  # both pointers start at the 1st node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # nodes met, there's a cycle, "is" check is faster than "=="
                return True
        return False

    def hasCycle(self, head):
        """ Returns True if there's a cycle in linked list, False otherwise.
        Hash based algorithm.
        Time complexity: O(n). Space complexity: O(n), n is len(linked list).
        """
        seen = set()  # nodes that we have seen already
        curr = head
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False
