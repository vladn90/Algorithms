""" Problem statement:
https://leetcode.com/problems/palindrome-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head):
        """ Returns True if singly linked list is a palindrome,
        False otherwise.
        Algorithm based on using stack. Traverse linked list, push node's value
        to the stack. Traverse again, pop node's value from the stack
        and compare to value of current node. If all values are equal,
        then list is a palindrome.

        Time complexity: O(n). Space complexity: O(n),
        where n is length of the linked list.
        """
        stack = []
        curr = head  # start traversing the list from the head node
        while curr:
            stack.append(curr.val)
            curr = curr.next
        # traverse one more time and compare the values
        # alternatively we can just check if stack(array) is a palindrome
        # return stack == stack[::-1]
        curr = head
        while curr:
            if curr.val != stack.pop():
                return False
            curr = curr.next
        return True

    def isPalindrome(self, head):
        """ Returns True if singly linked list is a palindrome,
        False otherwise.
        Algorithm is the following. Find the middle of the linked list,
        reverse right half of the list, traverse both halves and compare the
        nodes' values. Put the list back in order(optional).

        Time complexity: O(n). Space complexity: O(1),
        where n is length of the linked list.
        """
        # find the middle of the linked list, using slow and fast pointers
        # even = False  # is length of the linked list is even?
        slow, fast = head, head
        while True:
            if fast == None:  # fast pointer traversed all nodes
                # even = True  # this can only happen if list length is even
                curr = slow  # it's gonna be last node of reversed right half
                break
            elif fast.next == None:  # fast pointer is at the last node
                curr = slow.next  # it's gonna be last node of reversed right half
                break
            slow = slow.next  # goes to the next node
            fast = fast.next.next  # goes to the node after next node

        # reverse right half of the list
        prev = None
        while curr:
            link = curr.next
            curr.next = prev
            prev = curr
            curr = link
        # prev is gonna be start of the reversed right half of the list

        # traverse both halves and compare nodes' values
        is_pal = True
        curr_left, curr_right = head, prev
        while curr_left and curr_right:
            if curr_left.val != curr_right.val:
                is_pal = False
                break
            curr_left, curr_right = curr_left.next, curr_right.next

        # put the list back in order(optional)
        curr = prev  # prev still points to the head of reversed right half
        prev = None
        while curr:
            link = curr.next
            curr.next = prev
            prev = curr
            curr = link
        return is_pal
