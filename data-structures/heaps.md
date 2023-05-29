# Heaps

A heap is a complete binary tree that satisfies the heap property. The heap property states that for every node `i` in the heap, the value of `i` is either greater than or equal to (in a max heap) or less than or equal to (in a min heap) the values of its children.

Heaps are commonly used to efficiently maintain the maximum (or minimum) element in a collection, as well as for implementing priority queues.

In Python, heaps can be implemented using the `heapq` module, which provides functions for creating and manipulating heaps. The `heapq` module provides a binary min heap implementation by default. Here's an example of using `heapq` to create and work with heaps in Python:

```python
import heapq

# Creating a min heap
min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)

# Creating a max heap
max_heap = []
for item in [3, 1, 2]:
    heapq.heappush(max_heap, -item)

# Accessing the minimum (or maximum) element
min_element = heapq.heappop(min_heap)
max_element = -heapq.heappop(max_heap)

print(min_element)  # Output: 1
print(max_element)  # Output: 3
```

In the above example, the `heapq` module is used to create a min heap and a max heap. Elements are inserted into the heaps using the `heappush()` function, and the `heappop()` function is used to remove and return the minimum (or maximum) element from the heaps.

To create a max heap, we can use the `-item` trick, where we negate the values before inserting them into the heap. This ensures that the heap property is maintained with respect to the maximum element.

Heap operations such as insertion and deletion take logarithmic time complexity in the worst case, making heaps efficient for maintaining the maximum or minimum elements. They are commonly used in algorithms like heap sort, priority queues, and graph algorithms like Dijkstra's algorithm.

Note: While Python's `heapq` module provides a built-in implementation for heaps, it specifically provides a min heap. If you need a max heap, you can use the `-item` trick or implement a custom comparison function.