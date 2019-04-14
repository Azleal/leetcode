# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    nodeX = nodeY = None

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.nodeX = {'val': 0, 'depth': None, 'parent': None}
        self.nodeY = {'val': 0, 'depth': None, 'parent': None}
        self.nodeX['val'] = x
        self.nodeY['val'] = y

        self.getNoneInfo(root, 0, None)

        return self.nodeX['depth'] == self.nodeY['depth'] and \
               self.nodeX['parent'] != self.nodeY['parent']

    def getNoneInfo(self, root: TreeNode, depth, parent):

        if self.nodeX['depth'] is not None and depth > self.nodeX['depth']:
            return
        if self.nodeY['depth'] is not None and depth > self.nodeY['depth']:
            return

        if root.val == self.nodeX['val']:
            self.nodeX['depth'] = depth
            self.nodeX['parent'] = parent
            return

        if root.val == self.nodeY['val']:
            self.nodeY['depth'] = depth
            self.nodeY['parent'] = parent
            return

        if root.left is not None:
            self.getNoneInfo(root.left, depth + 1, root)

        if root.right is not None:
            self.getNoneInfo(root.right, depth + 1, root)

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(4)
# root.right.right=TreeNode(5)

r=Solution().isCousins(root, 2, 3)
print(r)


