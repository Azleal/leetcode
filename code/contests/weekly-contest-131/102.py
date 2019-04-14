# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:

        if root is None:
            return 0
        return max(self.findMaximum(root.val, root.val,root.left),self.findMaximum(root.val, root.val,root.right))

    def findMaximum(self, maxVal, minVal, root: TreeNode):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return max(abs(maxVal - root.val),abs(minVal - root.val))

        left_maximun=right_maximum=0
        if root.left:
            left_maximun = self.findMaximum(max(maxVal, root.val), min(minVal, root.val), root.left)
        if root.right:
            right_maximum = self.findMaximum(max(maxVal, root.val), min(minVal, root.val), root.right)


        return max(abs(maxVal - root.val), abs(minVal - root.val),left_maximun, right_maximum)


root = TreeNode(8)

root.left=TreeNode(3)
root.left.left=TreeNode(1)
root.left.right=TreeNode(6)
root.left.right.left=TreeNode(4)
root.left.right.right=TreeNode(7)

root.right=TreeNode(10)
root.right.right=TreeNode(14)
root.right.right.left=TreeNode(1)

r=Solution().maxAncestorDiff(TreeNode(8))
print(r)