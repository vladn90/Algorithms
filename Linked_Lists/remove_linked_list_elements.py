""" Problem statement:
https://leetcode.com/problems/remove-linked-list-elements/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head, value):
        """ Removes all nodes from the list with val = value.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        prev = None
        curr = head
        while curr:
            if curr.val == value:
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next  # to-be-removed element is the first one
            else:
                prev = curr
            curr = curr.next
        return head
