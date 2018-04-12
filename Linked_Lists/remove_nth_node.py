""" Problem statement:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """ Removes nth node from the end of the linked list.
        If n > len(linked list), removes 1st node.
        Time complexity: O(m). Space complexity: O(1), m is len(linked list).
        """
        prev = None  # pointer to node before nth_node
        curr = head
        nth_node = head  # to-be-deleted node
        while curr:
            if n == 0:  # move nth_node pointer to the next node
                prev = nth_node
                nth_node = nth_node.next
            else:
                n -= 1
            curr = curr.next
        if prev == None:  # nth_node is the 1st in the list
            head = head.next
        else:
            prev.next = nth_node.next
        return head


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        """ Removes nth node from the end of the linked list.
        If n > len(linked list), removes 1st node.
        Time complexity: O(m). Space complexity: O(1), m is len(linked list).
        """
        prev = None  # pointer to node before nth_node
        curr = head
        nth_node = head  # to-be-deleted node
        while curr:
            if n == 0:  # move nth_node pointer to the next node
                prev = nth_node
                nth_node = nth_node.next
            else:
                n -= 1
            curr = curr.next
        if prev == None:  # nth_node is the 1st in the list
            head = head.next
        else:
            prev.next = nth_node.next
        return head
