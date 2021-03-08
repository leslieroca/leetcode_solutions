https://leetcode.com/problems/range-sum-of-bst


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        suma = 0
        
        if root.val >= low and root.val <= high:
            suma += root.val
            
        if root.left is not None and root.val >= low:
            suma += self.rangeSumBST(root.left, low, high)
            
        if root.right is not None and root.val <= high:
            suma += self.rangeSumBST(root.right, low, high)        
        
        return suma 
