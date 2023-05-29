class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Linking nodes
node1.next = node2
node2.next = node3

# Accessing elements in the linked list
print(node1.value)      # Output: 1
print(node1.next.value) # Output: 2
print(node2.next.value) # Output: 3

# Traversing the linked list
current_node = node1
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next