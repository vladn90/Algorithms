""" Problem statement:
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, head1, head2):
        """ Merges two sorted linked lists.
        Time complexity: O(max(n, m)). Space complexity: O(1),
        n, m are lengths of the linked lists.
        """
        dummy = ListNode(None)
        curr = dummy
        while head1 and head2:  # choose node with min value from two lists
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:  # list1 is longer, add whatever is left from it
            curr.next = head1
        elif head2:
            curr.next = head2
        return dummy.next
