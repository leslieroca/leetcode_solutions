https://leetcode.com/problems/path-sum


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
            
        q = deque()
        q.append((root, root.val))
        
        while q:
            node, suma = q.popleft()
            
            if node.left is None and node.right is None:
                if suma == targetSum:
                    return True
            else: # inner node
                if node.left:
                    q.append((node.left, suma + node.left.val))
                if node.right:
                    q.append((node.right, suma + node.right.val))
                
        return False
