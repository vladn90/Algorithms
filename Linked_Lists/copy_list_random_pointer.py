""" Problem statement:
https://leetcode.com/problems/copy-list-with-random-pointer/description/
"""


# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


class Solution:
    def copyRandomList(self, head):
        """ Creates a deep copy of a linked list with random pointer.
        Returns a head of a new list. More concise and efficient algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list),
        space used for deep copy of the list isn't included in complexity analysis.
        """
        # copy nodes in dictionary
        nodes = dict()
        curr = head
        while curr:
            nodes[curr] = RandomListNode(curr.label)
            curr = curr.next  # go to the next node

        # simplifies code below, handles cases when next or random link is None
        nodes[None] = None

        # copy next and random links
        curr = head
        while curr:
            nodes[curr].next = nodes[curr.next]  # copy next link
            nodes[curr].random = nodes[curr.random]  # copy random link
            curr = curr.next  # go to the next node
        return nodes[head]  # return new head

    def copyRandomList(self, head):
        """ Creates a deep copy of a linked list with random pointer.
        Returns a head of a new list. Another algorithm.
        Time complexity: O(n). Space complexity: O(1), n is len(linked list),
        space used for deep copy of the list isn't included in complexity analysis.
        """
        # create a copy of each node and attach it to the original node
        curr = head
        while curr:
            node = RandomListNode(curr.label)
            node.next = curr.next
            curr.next = node
            curr = curr.next.next  # go to the next unique node

        # copy random links for each copied node
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # detach copied nodes into separate list
        dummy = tail = RandomListNode(0)
        curr = head
        while curr:
            tail.next = curr.next  # attach copied node to the new list
            tail = tail.next  # move tail pointer to attached node
            curr.next = curr.next.next  # restore original next pointer
            curr = curr.next  # go to the next unique node
        return dummy.next
