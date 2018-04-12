""" Problem statement:
https://leetcode.com/problems/delete-node-in-a-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteNode(self, node):
        """ Removes node from the linked list.
        Modifies linked list in-place. Doesn't return anything.
        """
        if node.next:  # check if current node is a tail
            node.val = node.next.val
            node.next = node.next.next
