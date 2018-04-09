""" Problem statement:
https://leetcode.com/problems/reverse-linked-list-ii/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """ Reverses linked list from index m to n, 1-based indices.
        Returns head pointer.
        Time complexity: O(n). Space complexity: O(1),
        n is length of the linked list.
        """
        prev = None
        curr = head
        curr_index = 1  # since m, n are 1-based indices
        while curr_index < m:  # traverse the linked list and find node m
            prev, curr = curr, curr.next
            curr_index += 1
        last_node = curr  # this node is gonna be last in reversed part
        prev_node = prev  # 1st node before the reversed part

        # reverse linked list from m to n
        prev = None
        while curr_index <= n:
            curr_index += 1
            link = curr.next
            curr.next = prev
            prev, curr = curr, link
        last_node.next = curr  # change the pointer of last node of reversed part
        if prev_node == None:
            head = prev
        else:
            prev_node.next = prev
        return head
