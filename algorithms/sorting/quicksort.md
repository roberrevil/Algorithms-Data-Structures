# Quicksort Algorithm

Quicksort is a widely used comparison-based sorting algorithm that follows the divide-and-conquer approach. It works by selecting a pivot element from the input list and partitioning the other elements into two sublists, according to whether they are less than or greater than the pivot. The sublists are then recursively sorted, and the sorted sublists are combined to produce a sorted output.

The steps involved in the quicksort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Pivot Selection:** Choose a pivot element from the input list. The pivot can be selected in various ways, such as the first element, last element, or a random element.
3. **Partitioning:** Rearrange the other elements in the list such that:
   - All elements less than the pivot are moved to the left side of the pivot.
   - All elements greater than the pivot are moved to the right side of the pivot.
   - The pivot element is in its final sorted position.
4. **Recursion:** Recursively apply quicksort to the sublists created by the partitioning step.
   - Apply quicksort to the sublist of elements less than the pivot.
   - Apply quicksort to the sublist of elements greater than the pivot.
5. **Combining:** Combine the sorted sublists and the pivot element to produce the final sorted list.
   - The sorted sublist of elements less than the pivot, followed by the pivot element, followed by the sorted sublist of elements greater than the pivot.

Here is a Python implementation of the quicksort algorithm:

```python
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # Select the first element as the pivot
    less_than = [x for x in arr[1:] if x <= pivot]
    greater_than = [x for x in arr[1:] if x > pivot]
    
    return quicksort(less_than) + [pivot] + quicksort(greater_than)
```

In the above implementation, `arr` is the input list that needs to be sorted. The `quicksort` function is the main driver function that performs the quicksort algorithm. It selects the first element of the input list as the pivot and partitions the remaining elements into two sublists: `less_than` containing elements less than or equal to the pivot, and `greater_than` containing elements greater than the pivot.

The function then recursively applies quicksort to the `less_than` and `greater_than` sublists and combines the sorted sublists along with the pivot element to produce the final sorted list.

Finally, the sorted list is returned.

The time complexity of the quicksort algorithm depends on the choice of the pivot and the partitioning. On average, it has a time complexity of $O(n log n)$, where $n$ is the number of elements in the input list. However, in the worst-case scenario, when the pivot is not well-balanced and results in uneven partitions, the time complexity can be $O(n^2)$. To mitigate this, various techniques like randomizing the pivot or using the median-of-three pivot selection can be employed.