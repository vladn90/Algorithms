""" Problem statement:
https://leetcode.com/problems/linked-list-cycle-ii/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        """ Returns node where the cycle begins in the linked list, or None
        if there's no cycle.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        slow = fast = head
        # move 2 pointers, slow and fast at different speed
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # meeting point
                break
        if not fast or not fast.next:  # no cycle in the list
            return None

        # move 2 pointers at the same speed, one pointer starts from the head of
        # the list, other pointer starts from the previous meeting point
        while slow != head:
            slow = slow.next
            head = head.next
        return head  # return node where they met again, start of the cycle

    def detectCycle(self, head):
        """ More concise code version.
        Returns node where the cycle begins in the linked list, or None
        if there's no cycle.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:  # meeting point
                while slow != head:
                    slow = slow.next
                    head = head.next
                return head
        return None
