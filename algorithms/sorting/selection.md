# Selection Sort Algorithm

Selection sort is a simple comparison-based sorting algorithm. It works by dividing the input into two parts: the sorted sublist and the unsorted sublist. The algorithm repeatedly finds the minimum element from the unsorted sublist and swaps it with the element at the beginning of the unsorted sublist. This process continues until the entire list is sorted.

The steps involved in the selection sort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Initialization:** Set the index `i` to 0, representing the beginning of the unsorted sublist.
3. **Selection:** Find the minimum element in the unsorted sublist starting from index `i` until the end of the list.
4. **Swap:** Swap the minimum element found in step 3 with the element at index `i`.
5. **Increment:** Increment `i` by 1 to move the boundary of the sorted sublist.
6. **Repeat:** Repeat steps 3-5 until the entire list is sorted.

Here is a Python implementation of the selection sort algorithm:

```python
def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted sublist
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the minimum element with the element at index i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
```

In the above implementation, `arr` is the input list that needs to be sorted. The outer loop iterates over the indices of the input list, representing the boundary between the sorted and unsorted sublists. The inner loop finds the index of the minimum element in the unsorted sublist. After finding the minimum element, it is swapped with the element at the beginning of the unsorted sublist.

Finally, the sorted list is returned.

The time complexity of the selection sort algorithm is O(n^2), where n is the number of elements in the input list.
