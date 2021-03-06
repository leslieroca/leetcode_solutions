https://leetcode.com/problems/binary-tree-maximum-path-sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max = root.val
        
        def dfs(node):
            if node == None:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)
            m = max(l, 0) + node.val + max(r, 0)
            
            ret = max(node.val + l, node.val + r, node.val)
            self.max = max(m, self.max)
            
            return ret
        
        dfs(root)
        return self.max
