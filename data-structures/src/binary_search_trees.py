class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Inserting elements into the BST
def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Searching for an element in the BST
def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    else:
        return search(root.right, value)

# Creating a BST and performing operations
root = None
root = insert(root, 5)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 1)
root = insert(root, 4)

print(search(root, 2))  # Output: <__main__.Node object at 0x...>
print(search(root, 6))  # Output: None