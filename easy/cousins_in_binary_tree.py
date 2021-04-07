https://leetcode.com/problems/cousins-in-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = None
        self.is_cousin = False
        
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.DFS(root, 0, x, y)
        return self.is_cousin
        
    def DFS(self, node, depth, x, y):
        if node is None:
            return False

        if self.depth and depth > self.depth:
            return False

        if node.val == x or node.val == y:
            if self.depth is None:
                
                self.depth = depth
            
            return self.depth == depth

        left = self.DFS(node.left, depth+1, x, y)
        right = self.DFS(node.right, depth+1, x, y)

        
        if left and right and self.depth != depth + 1:
            self.is_cousin = True

        return left or right
        
