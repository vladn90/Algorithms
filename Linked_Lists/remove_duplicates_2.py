""" Problem statement:
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """ Removes all nodes that have duplicate values, leaving only nodes
        with unique values.
        Time complexity: O(n). Space complexity: O(1),
        n is length of the linked list.
        """
        prev = None
        curr = head
        while curr:
            found = False  # did we find node with duplicate value?
            # compare current node's value with next node's value
            while curr and curr.next and curr.val == curr.next.val:
                found = True
                curr = curr.next
            # after exiting the while loop curr is gonna point to the last
            # duplicate node, if there's one
            if found:
                curr = curr.next  # move curr pointer to the next unique node
                if prev != None:
                    prev.next = curr  # skip all duplicates
                else:  # prev == None, 1st duplicate node is the 1st node in the list
                    head = curr
            else:  # no duplicates were found
                prev, curr = curr, curr.next
        return head
