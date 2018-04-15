""" Problem statement:
https://leetcode.com/problems/min-stack/description/
--------------------------------------------------------------------------------
Design a stack that supports push, pop, top, and retrieving the minimum element
in O(1) time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
--------------------------------------------------------------------------------
Implementation of min stack in Python is the following.
Implement a regular stack data structure using array. Then initialize another
array within that's gonna hold the indices of minimum elements. Treat this array
as stack. So the index of last minimum element is gonna be the last element in
this stack. This way can always keep track of the next minimum element when we
pop the current minimum element from the stack. Details below.
"""


class MinStack:
    def __init__(self):
        """ Array self.elements is gonna hold all the elements of the stack,
        array self.min_index is gonna hold indices of minimum elements.
        """
        self.elements = []  # current elements on the stack
        self.min_index = []  # indices of min elements

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.elements.append(x)
        if not self.min_index \
                or self.elements[-1] < self.elements[self.min_index[-1]]:
            self.min_index.append(len(self.elements) - 1)

    def pop(self):
        """
        :rtype: void
        """
        # special case, stack is empty
        if not self.elements:
            return  # do nothing
        # to-be-removed element is current min
        if self.min_index[-1] == len(self.elements) - 1:
            self.min_index.pop()  # update current min index
        self.elements.pop()  # remove element

    def top(self):
        """
        :rtype: int
        """
        if not self.elements:  # stack is empty
            return -1
        return self.elements[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.elements:  # stack is empty
            return -1
        return self.elements[self.min_index[-1]]  # return element at min index


if __name__ == "__main__":
    stack = MinStack()

    stack.push(1)
    stack.push(2)
    print(f"last element is {stack.top()}, min element is {stack.getMin()}")
    stack.push(-2)
    stack.push(3)
    stack.push(4)
    print(f"last element is {stack.top()}, min element is {stack.getMin()}")
    stack.pop()
    stack.pop()
    stack.pop()
    print(f"last element is {stack.top()}, min element is {stack.getMin()}")
