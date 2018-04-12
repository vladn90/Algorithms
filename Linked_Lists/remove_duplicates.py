""" Problem statement:
https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """ Removes duplicates from sorted linked list.
        Returns pointer to the head node.
        Time complexity: O(n). Space complexity: O(1),
        n is length of the linked list.
        """
        unique_val = None  # current unique node value
        prev = None
        curr = head
        while curr:
            if curr.val == unique_val:  # duplicate is found
                prev.next = curr.next
                curr = curr.next  # change only curr pointer
            else:  # new unique value
                unique_val = curr.val
                prev = curr
                curr = curr.next
        return head
