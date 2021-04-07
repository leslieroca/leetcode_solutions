https://leetcode.com/problems/cousins-in-binary-tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        parents = [root]
        while len(parents) > 0:
            children_nodes = []
            children_values = set()
            
            for parent in parents:
                p_children_values = set()
                
                if parent.left is not None:
                    children_nodes.append(parent.left)
                    children_values.add(parent.left.val)
                    p_children_values.add(parent.left.val)
                
                if parent.right is not None:
                    children_nodes.append(parent.right) 
                    children_values.add(parent.right.val)
                    p_children_values.add(parent.right.val)
                    
                if p_children_values == set([x, y]):
                    return False
                
                if (x in children_values) and (y in children_values):
                    return True
     
            parents = children_nodes
        
        return False
