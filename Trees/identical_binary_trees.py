""" Problem statement:
https://www.interviewbit.com/problems/identical-binary-trees/
https://leetcode.com/problems/same-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionInterviewBit:
    def inorder(self, root, result):
        if not root:
            result.append(None)
            return
        self.inorder(root.left, result)
        self.inorder(root.right, result)
        result.append(root.val)

    def isSameTree(self, root1, root2):
        result1 = []
        result2 = []
        self.inorder(root1, result1)
        self.inorder(root2, result2)
        return 1 if result1 == result2 else 0


class SolutionLeetCode:
    def inorder(self, root, result):
        if not root:
            result.append(None)
            return
        self.inorder(root.left, result)
        self.inorder(root.right, result)
        result.append(root.val)

    def isSameTree(self, root1, root2):
        result1 = []
        result2 = []
        self.inorder(root1, result1)
        self.inorder(root2, result2)
        return result1 == result2
