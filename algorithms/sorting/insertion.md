## Insertion Sort Algorithm

Insertion sort is a simple comparison-based sorting algorithm. It works by dividing the input into two parts: the sorted sublist and the unsorted sublist. The algorithm repeatedly takes an element from the unsorted sublist and inserts it into its correct position in the sorted sublist. This process continues until the entire list is sorted.

The steps involved in the insertion sort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Initialization:** Start with the first element and consider it as the sorted sublist.
3. **Insertion:** Take the next element from the unsorted sublist and insert it into its correct position in the sorted sublist.
   - Compare the element with each element in the sorted sublist, moving elements to the right until the correct position is found.
   - Insert the element at the correct position in the sorted sublist.
4. **Repeat:** Repeat step 3 until all elements in the unsorted sublist have been inserted into the sorted sublist.
5. **Sorted List:** The sorted sublist represents the final sorted list.

Here is a Python implementation of the insertion sort algorithm:

```python
def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements of sorted sublist greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position in the sorted sublist
        arr[j+1] = key
    
    return arr
```

In the above implementation, `arr` is the input list that needs to be sorted. The outer loop iterates from the second element (`i = 1`) to the last element of the input list. Inside the loop, the key element is extracted from the unsorted sublist. Then, a comparison loop is executed to find the correct position in the sorted sublist to insert the key.

During the comparison loop, each element greater than the key is moved one position to the right to make space for the key. Once the correct position is found, the key is inserted at that position.

Finally, the sorted list is returned.

The time complexity of the insertion sort algorithm is O(n^2), where n is the number of elements in the input list. However, it has an advantage over other quadratic time complexity sorting algorithms, such as bubble sort and selection sort, as it performs well on partially sorted or small-sized lists.