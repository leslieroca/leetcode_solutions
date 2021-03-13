Print TreeNode values In-Order 
Return a string with the TreeNode values In-Order

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def in_order(root):
    if not root:
        return

    in_order(root.left)
    print(root.val)
    in_order(root.right)

def in_order_string(root):
    if not root:
        return ""

    left = in_order_string(root.left)
    right = in_order_string(root.right)
    return left + root.val + right



# Tests
a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.left = b
a.right = c
b.left = d
c.right = e


in_order(a)
print(in_order_string(a))

