# Red-black Trees
a
A red-black tree is a self-balancing binary search tree that maintains its balance through the use of color properties and rotations. It guarantees a logarithmic time complexity for insertion, deletion, and searching operations. Each node in a red-black tree has an additional attribute, color, which can be either red or black. The tree must satisfy the following properties:

1. Every node is either red or black.
2. The root node is always black.
3. All leaves (NIL or null nodes) are black.
4. If a node is red, both its children are black.
5. Every path from a node to its descendant leaves contains the same number of black nodes.

In Python, a red-black tree can be implemented using a class that represents the nodes. Each node has a value, a color, and references to its left and right children (or NIL nodes if they are absent). Here's an example of creating and using a red-black tree in Python:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.color = 'RED'  # 'RED' or 'BLACK'
        self.left = None
        self.right = None
        self.parent = None

# Inserting elements into the red-black tree
def insert(root, value):
    def fix_violations(node):
        while node.parent and node.parent.color == 'RED':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        rotate_left(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle and uncle.color == 'RED':
                    node.parent.color = 'BLACK'
                    uncle.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        rotate_right(node)
                    node.parent.color = 'BLACK'
                    node.parent.parent.color = 'RED'
                    rotate_left(node.parent.parent)

    def rotate_left(node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    new_node = Node(value)
    current = None
    temp = root

    while temp:
        current = temp
        if new_node.value < temp.value:
            temp = temp.left
        else:
            temp = temp.right

    new_node.parent = current
    if not current:
        root = new_node
    elif new_node.value < current.value:
        current.left = new_node
    else:
        current.right = new_node

    fix_violations(new_node)
    root.color = 'BLACK'

# Creating a red-black tree and performing operations
root = None
insert(root, 5)
insert(root, 2)
insert(root, 7)
insert(root, 1)
insert(root, 4)
```

In the above example, `Node` represents a single node in the red-black tree. Each node has a `value` attribute to store the data, a `color` attribute to store the color ('RED' or 'BLACK'), and `left`, `right`, and `parent` attributes to store references to its left child, right child, and parent nodes, respectively.

To insert elements into the red-black tree, we use the `insert()` function. It performs a standard BST insertion and then fixes any violations of the red-black tree properties using rotations and color adjustments.

The `fix_violations()` function is used to handle different cases when a node is inserted into a red-black tree, ensuring that all the red-black tree properties are maintained.

The `rotate_left()` and `rotate_right()` functions perform left and right rotations, respectively, to balance the tree when needed.

Red-black trees are efficient self-balancing binary search trees that provide guaranteed logarithmic time complexity for various operations. They are commonly used in applications that require efficient searching, such as in-memory databases and language compilers.
