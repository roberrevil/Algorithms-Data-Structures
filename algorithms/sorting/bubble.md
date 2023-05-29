# Bubble Sort Algorithm

Bubble sort is a simple comparison-based sorting algorithm. It works by repeatedly swapping adjacent elements if they are in the wrong order. In each pass, the largest element "bubbles" up to its correct position at the end of the list. This process is repeated until the entire list is sorted.

The steps involved in the bubble sort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Iteration:** Repeat the following steps for `n-1` passes, where `n` is the number of elements in the list.
3. **Comparison:** Compare each pair of adjacent elements from the beginning of the list.
4. **Swap:** If the two adjacent elements are in the wrong order, swap them.
5. **Repeat:** Repeat steps 3-4 until the end of the list is reached.
6. **Decrement:** After each pass, the largest element will be at the end of the unsorted sublist. Decrement the number of elements to be considered in the next pass.
7. **Repeat:** Repeat steps 3-6 until the entire list is sorted.

Here is a Python implementation of the bubble sort algorithm:

```python
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the two adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr
```

In the above implementation, `arr` is the input list that needs to be sorted. The outer loop iterates `n-1` times, where `n` is the number of elements in the input list. The inner loop compares each pair of adjacent elements from the beginning of the list and swaps them if they are in the wrong order.

After each pass, the largest element in the unsorted sublist moves to the end. Thus, the inner loop can be shortened by decrementing `n` with each iteration, as the last `i` elements are already sorted.

Finally, the sorted list is returned.

The time complexity of the bubble sort algorithm is $O(n^2)$, where $n$ is the number of elements in the input list. However, it can be optimized with a flag to check if any swaps were made during a pass, allowing early termination if the list is already sorted.