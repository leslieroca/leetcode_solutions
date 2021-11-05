https://leetcode.com/problems/binary-tree-inorder-traversal



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorderDFS(node):
            if node is not None:
                inorderDFS(node.left)
                result.append(node.val)
                inorderDFS(node.right)
                
        inorderDFS(root)
        
        return result
    
