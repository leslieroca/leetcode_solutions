https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.result = None
        
        def rec(original, cloned):
            if original:
                rec(original.left, cloned.left)
                if original is target:
                    self.result = cloned
                rec(original.right, cloned.right)
               
        rec(original, cloned)
        
        return self.result
   
