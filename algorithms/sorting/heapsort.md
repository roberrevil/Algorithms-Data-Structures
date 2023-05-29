# Heapsort Algorithm

Heapsort is a comparison-based sorting algorithm that utilizes a binary heap data structure. It works by creating a max-heap from the input list, repeatedly extracting the maximum element (root) from the heap, and placing it at the end of the list. This process continues until the entire list is sorted in ascending order.

The steps involved in the heapsort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Heap Construction:** Build a max-heap from the input list.
   - Convert the input list into a binary heap data structure.
   - Starting from the first non-leaf node (i.e., the parent of the last element), heapify the elements downwards to ensure that each parent is greater than its children.
3. **Sorting:** Extract the maximum element from the max-heap and place it at the end of the list.
   - Swap the root element (maximum) with the last element in the heap.
   - Reduce the heap size by 1.
   - Heapify the updated heap to maintain the max-heap property.
   - Repeat this process until all elements have been extracted and placed in their correct positions.
4. **Sorted List:** The list is now sorted in ascending order.

Here is a Python implementation of the heapsort algorithm:

```python
def heapsort(arr):
    n = len(arr)
    
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from the max-heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root (maximum) with last element
        heapify(arr, i, 0)
    
    return arr

def heapify(arr, n, i):
    largest = i  # Initialize largest as the root
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # Check if right child is larger than root
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # Swap root if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

In the above implementation, `arr` is the input list that needs to be sorted. The `heapsort` function is the main driver function that performs the heapsort algorithm. It first builds a max-heap by calling the `heapify` function on each non-leaf node of the heap. The `heapify` function ensures that the given node and its children satisfy the max-heap property.

After constructing the max-heap, the function performs the sorting process by extracting the maximum element (root) from the heap and placing it at the end of the list. It then reduces the heap size and performs the `heapify` operation to restore the max-heap property. This process continues until all elements have been extracted and placed in their correct positions.

Finally, the sorted list is returned.

The time complexity of the heapsort algorithm is $O(n log n)$, where $n$ is the number of elements in the input list. Heap construction takes $O(n)$ time, and extracting the maximum element and heapifying take $O(log n)$ time, and these operations are performed $n$ times. Heapsort has the advantage of an in-place sorting algorithm with relatively good performance.