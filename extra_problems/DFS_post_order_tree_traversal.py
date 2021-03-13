Print TreeNode values Post-Order
Return a string of TreeNode values Post-Order 


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def post_order(root):
    if not root:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val)

def post_order_str(root):
    l = []

    def iterate(root, l):
        if not root:
            return
        iterate(root.left, l)
        iterate(root.right, l)
        l.append(root.val)

    iterate(root, l)
    return  "".join(l)


def post_order_string(root):
    if not root:
        return ""

    left = post_order_string(root.left)
    right = post_order_string(root.right)
    return left + right + root.val



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


print("Post-Order")
post_order(a)

print("Post-Order-String")
print(post_order_string(a))

print(post_order_str(a))

