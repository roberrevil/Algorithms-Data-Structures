import heapq

# Creating a priority queue
priority_queue = []
heapq.heappush(priority_queue, (3, "Task 1"))  # (priority, data)
heapq.heappush(priority_queue, (1, "Task 2"))
heapq.heappush(priority_queue, (2, "Task 3"))

# Accessing the element with the highest priority
highest_priority = heapq.heappop(priority_queue)
print(highest_priority)  # Output: (1, "Task 2")