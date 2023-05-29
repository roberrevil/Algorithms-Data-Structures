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