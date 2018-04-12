""" Problem statement:
https://leetcode.com/problems/partition-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head, x):
        """ Partitions linked list such that nodes with value < x come
        before nodes with value >= x.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        left_head = ListNode(None)  # head of the list with nodes values < x
        right_head = ListNode(None)  # head of the list with nodes values >= x
        left = left_head  # attach here nodes with values < x
        right = right_head  # attach here nodes with values >= x
        # traverse the list and attach current node to left or right nodes
        while head:
            if head.val < x:
                left.next = head
                left = left.next
            else:  # head.val >= x
                right.next = head
                right = right.next
            head = head.next
        right.next = None  # set tail of the right list to None
        left.next = right_head.next  # attach left list to the right
        return left_head.next  # head of a new partitioned list
