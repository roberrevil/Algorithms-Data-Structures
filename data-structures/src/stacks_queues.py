stack = []

# Pushing elements onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Popping elements from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1

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