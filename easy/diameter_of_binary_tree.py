https://leetcode.com/problems/diameter-of-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 1
        
        def deep(node):
            if not node:
                return 0
            right = deep(node.right)
            left = deep(node.left)
            
            self.result = max(self.result, left + right + 1)
            return max(right, left) + 1

        deep(root)
        return self.result - 1
