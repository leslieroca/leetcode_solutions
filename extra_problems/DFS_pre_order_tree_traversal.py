Print TreeNode values Pre-Order
Return a string with the TreeNode values Pre-Ordes

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def pre_order(root):
    if not root:
        return

    print(root.val)
    pre_order(root.left)
    pre_order(root.right)


def pre_order_string(root):
    if not root:
        return ""

    left = pre_order_string(root.left)
    right = pre_order_string(root.right)
    return root.val + left + right


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

pre_order(a)
print(pre_order_string(a))

