""" Problem statement:
https://leetcode.com/problems/sort-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class SolutionRecursive:
    def merge(self, head1, head2):
        """ Merges two sorted linked lists into one sorted linked list.
        Time complexity: O(max(n, m)). Space complexity: O(1),
        n, m are lengths of the linked lists.
        """
        dummy = ListNode(None)
        curr = dummy  # pointer to the current node of merged list
        curr1, curr2 = head1, head2
        while curr1 and curr2:  # choose node with min value from both lists
            if curr1.val < curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next  # move current pointer of merged list
        if curr1:  # list1 is longer
            curr.next = curr1
        elif curr2:  # list2 is longer
            curr.next = curr2
        return dummy.next  # head node of the new merged list

    def sortList(self, head):
        """ Recursive Merge Sort algorithm for linked list.
        Returns head pointer of the new sorted list.
        Time complexity: O(n * lg(n)). Space complexity: O(lg(n)),
        n is len(linked list).
        """
        # base case, 1 node or an empty list
        if head is None or head.next is None:
            return head

        # find the middle of the list using slow, fast pointers technique
        prev, slow, fast = None, head, head
        while fast != None and fast.next != None:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None  # divide list into two lists
        # now head is start of the left list and slow is start of the right list
        # recursively sort left and right lists
        left = self.sortList(head)
        right = self.sortList(slow)
        return self.merge(left, right)  # merge two lists


class SolutionIterative:
    def merge(self, left, right, tail):
        """ Merges two sorted linked lists. Returns the link to the last node
        of sorted merged list.

        input: left >> start of the left linked list
               right >> start of the right linked list
               tail >> last node of already original sorted linked list

        Time complexity: O(n + m). Space complexity: O(1),
        n, m are lengths of the input linked lists.
        """
        while left and right:  # choose node with min value from both lists
            if left.val <= right.val:  # <= gives us stable sort
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if left:  # left linked list is longer
            tail.next = left  # attach whatever is left of it
        elif right:  # right list is longer
            tail.next = right
        while tail.next:  # go the last node of merged list
            tail = tail.next
        return tail

    def split(self, head, size):
        """ Splits linked list starting from node head, such that left half
        of the list has exactly "size" nodes. Returns the head of the right list.

        Time complexity: O(n). Space complexity: O(1), n is len(linked list).
        """
        i = 1
        while head and i < size:  # find the last node of the left list
            head = head.next
            i += 1
        if head is None:
            return None
        right = head.next  # now right points to the 1st node of right list
        head.next = None  # disconnect left list from the right
        return right

    def sortList(self, head):
        """ Iteratively sorts the linked list using Merge Sort.
        Returns the head node to the new sorted list.
        Time complexity: O(n * lg(n)). Space complexity: O(1), n is len(linked list).
        """
        # special case, list is empty or has only 1 node
        if head is None or head.next is None:
            return head

        # find the length of the list
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        # sort part of iterative Merge Sort algorithm
        dummy = ListNode(None)  # dummy node to attach sorted linked list to
        dummy.next = head
        size = 1  # start with merging linked lists of size 1
        while size < length:
            curr = dummy.next  # curr points to the 1st node of the next list to be sorted
            tail = dummy  # tail points to last node of already sorted list
            while curr:  # while we still have list to sort
                left = curr  # start node of the left list
                right = self.split(left, size)  # start node of the right list
                curr = self.split(right, size)  # update curr
                tail = self.merge(left, right, tail)  # merge left and right lists, update tail
            size *= 2
        return dummy.next
