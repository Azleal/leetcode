# -*- coding: utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        if len(S) == 0:
            return None
        dashArr = self.formatStr(S)

        root=self.buildNode(dashArr,0)
        return root


    def formatStr(self, dash):
        arr=[]
        prev=None
        for i in dash:
            if prev is not None:
                if i == prev:
                    # 一样
                    arr[-1] += i
                elif i != prev:
                    if prev == '-' or i == '-':
                        #之前是-, 现在是数字
                        arr.append(i)
                    else:
                        # 之前现在都不是 -
                        arr[-1] += i
            else:
                arr.append(i)

            prev = i
        return arr


    def buildNode(self, dash, depth):
        if dash is None or (len(dash)) < 1:
            return None
        currentDepth = depth
        thisNode = None

        if dash[0][:1] != '-':
            val = dash.pop(0)
            thisNode = TreeNode(val)
            if thisNode.left is None:
                thisNode.left = self.buildNode(dash, currentDepth + 1)
            if thisNode.right is None:
                thisNode.right = self.buildNode(dash, currentDepth + 1)
        elif dash[0][:1] == '-':
            if len(dash[0]) > currentDepth:
                #go down
                if thisNode.left is None:
                    thisNode.left = self.buildNode(dash, currentDepth + 1)
                elif thisNode.right is None:
                    thisNode.right = self.buildNode(dash, currentDepth + 1)
                else:
                    return thisNode
            elif len(dash[0]) == currentDepth:
                dash.pop(0)
                thisNode = self.buildNode(dash, currentDepth)

        return thisNode



dash="1-2--3---4-5--6---7"
r=Solution().recoverFromPreorder(dash)
print(r)

