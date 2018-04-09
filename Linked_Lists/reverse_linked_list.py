""" Problem statement:
https://leetcode.com/problems/reverse-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head):
        """ Reverses a singly linked list in-place.
        Time complexity: O(n). Space complexity: O(1),
        where n is length of the linked list.
        """
        prev = None  # pointer to the previous node
        while head:  # current node, start with a head node
            link = head.next  # save the link to the next node
            head.next = prev  # reverse the next link of current node
            prev = head  # adjust prev pointer
            head = link  # go the the next node
        return prev  # return the prev node, since curr node is gonna point to None
