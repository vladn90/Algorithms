""" Problem statement:
https://leetcode.com/problems/insertion-sort-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def insert_node(self, head, node):
        """ Inserts node in a sorted linked list.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        prev, curr = None, head
        while curr.val < node.val:
            prev, curr = curr, curr.next
        if not prev:
            head = node
        else:
            prev.next = node
        node.next = curr
        return head

    def insertionSortList(self, head):
        """ Sorts input linked list using insertion sort.
        Time complexity: O(n ^ 2). Space complexity: O(1), n is len(linked list).
        """
        # special case, list is empty or has only 1 node
        if not head or not head.next:
            return head

        tail = head  # pointer to tail node of already sorted linked list
        curr = head.next
        while curr:
            if curr.val < tail.val:
                link = curr.next  # save link to the next node
                # insert curr node in sorted part of the list
                head = self.insert_node(head, curr)
                tail.next = link
                curr = link
            else:
                tail = tail.next
                curr = curr.next
        return head
