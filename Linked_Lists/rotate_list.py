""" Problem statement:
https://leetcode.com/problems/rotate-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head, k):
        """ Rotates linked list by k places to the right.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        if k == 0 or not head:  # no need to rotate the list
            return head

        # find the length of the list and save the link to last node
        last = None  # link to the last node in the list
        curr = head
        length = 0
        while curr:
            length += 1
            last = curr
            curr = curr.next

        k %= length  # so we don't go over end of the list
        if k == 0:  # no need to rotate the list
            return head

        # find (k + 1)th node from the end
        curr = head
        i = 0
        while length - i > (k + 1):
            i += 1
            curr = curr.next
        last.next = head  # attach left half to the last node of right half
        head = curr.next  # save link to the new head
        curr.next = None  # set tail of a new list to None
        return head
