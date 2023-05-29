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