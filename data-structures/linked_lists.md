# Linked Lists

A linked list is a data structure that consists of a sequence of nodes, where each node contains a value and a reference (or link) to the next node in the sequence. Unlike arrays, linked lists do not require contiguous memory allocation. Instead, each node can be stored at any location in memory, and they are connected through their references.

In Python, a linked list can be implemented using a class that represents the nodes. Each node has two attributes: `value` to store the data and `next` to store the reference to the next node. Here's an example of creating and using a linked list in Python:

```python
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
```

In the above example, `Node` represents a single node in the linked list. The `value` attribute stores the data, and the `next` attribute holds the reference to the next node. The nodes are linked by assigning the `next` attribute of one node to another node. 

To access elements in the linked list, you can use dot notation (`node.next`) to follow the references and retrieve the values. 

To traverse the linked list, you can start from the head node (`node1` in this example) and iterate through each node by updating the current node using `current_node = current_node.next`. The traversal continues until reaching the end of the linked list, which is indicated by a `None` reference.