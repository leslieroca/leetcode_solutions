"""
Return sum of all nodes in a binary tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumBinaryTree(self, root):
        if not root:
            return 0

        suma = 0
        suma += root.val

        left = self.sumBinaryTree(root.left)
        right = self.sumBinaryTree(root.right)

        suma += left
        suma += right

        return suma


root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, None, None),TreeNode(2, None, None)), None), TreeNode(8, TreeNode(13, None, None), TreeNode(4, None, TreeNode(1, None, None))))

S = Solution()
print(S.sumBinaryTree(root))
assert(S.sumBinaryTree(root) == 55)

