# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        sum=self.walkThrough("", root)
        # print(sum)
        return sum

    def walkThrough(self, superString , root : TreeNode) -> int:
        thisSuperString=superString+str(root.val)
        sum = 0
        if root.left == None and root.right == None:
            sum = int(thisSuperString, 2)
            return sum
        if root.left is not None:
            sum += self.walkThrough(thisSuperString, root.left)
        if root.right is not None:
            sum += self.walkThrough(thisSuperString, root.right)
        return sum


node3 = [TreeNode(0),TreeNode(1),TreeNode(0),TreeNode(1)]
node2 = [TreeNode(0),TreeNode(1)]
node2[0].left=node3[0]
node2[0].right=node3[1]

node2[1].left=node3[2]
node2[1].right=node3[3]

node1 = TreeNode(1)
node1.left=node2[0]
node1.right=node2[1]

solution=Solution()
solution.sumRootToLeaf(node1)






