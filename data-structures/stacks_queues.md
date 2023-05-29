# Stacks

A stack is a linear data structure that follows the Last-In-First-Out (LIFO) principle. It can be visualized as a stack of items where the last item added is the first one to be removed. The two primary operations on a stack are `push`, which adds an item to the top of the stack, and `pop`, which removes the top item from the stack. 

In Python, a stack can be implemented using a list. Here's an example:

```python
stack = []

# Pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
```

In the above example, a list `stack` is used as the underlying data structure for the stack. The `append()` method is used to push elements onto the stack, and the `pop()` method is used to remove and return the top element from the stack.

# Queues

A queue is a linear data structure that follows the First-In-First-Out (FIFO) principle. It can be visualized as a queue of items, where the first item added is the first one to be removed. The two primary operations on a queue are `enqueue`, which adds an item to the rear of the queue, and `dequeue`, which removes and returns the front item from the queue.

In Python, a queue can be implemented using the `deque` class from the `collections` module. Here's an example:

```python
from collections import deque

queue = deque()

# Enqueuing elements into the queue
queue.append(1)
queue.append(2)
queue.append(3)

# Dequeuing elements from the queue
print(queue.popleft())  # Output: 1
print(queue.popleft())  # Output: 2
print(queue.popleft())  # Output: 3
```

In the above example, a `deque` object `queue` is used as the underlying data structure for the queue. The `append()` method is used to enqueue elements into the queue, and the `popleft()` method is used to dequeue and return the front element from the queue.

Both stack and queue data structures are commonly used in various algorithms and applications to manage and process data in a specific order.