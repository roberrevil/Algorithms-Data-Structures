# Merge Sort Algorithm

Merge sort is a comparison-based sorting algorithm that follows the divide-and-conquer approach. It works by recursively dividing the input list into smaller sublists, sorting them, and then merging them to produce a sorted output. The merging process combines two sorted sublists into a single sorted sublist.

The steps involved in the merge sort algorithm are as follows:

1. **Input:** Take an input list of elements to be sorted.
2. **Divide:** Divide the input list into two equal-sized sublists (or approximately equal-sized).
   - If the list has fewer than two elements, it is already considered sorted.
   - Otherwise, split the list into two sublists at the middle index.
3. **Conquer:** Recursively sort the two sublists using merge sort.
   - Apply merge sort to the first sublist.
   - Apply merge sort to the second sublist.
4. **Merge:** Merge the two sorted sublists into a single sorted sublist.
   - Start with two pointers, one for each sublist, initially pointing to the first element.
   - Compare the elements at the pointers and select the smaller one to be added to the merged sublist.
   - Move the pointer of the selected element to the next position.
   - Repeat the comparison and selection process until all elements from both sublists are merged into the sorted sublist.
5. **Sorted List:** The merged sublist represents the final sorted list.

Here is a Python implementation of the merge sort algorithm:

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the input list into two sublists
    mid = len(arr) // 2
    left_sublist = arr[:mid]
    right_sublist = arr[mid:]
    
    # Recursively sort the two sublists
    left_sublist = merge_sort(left_sublist)
    right_sublist = merge_sort(right_sublist)
    
    # Merge the sorted sublists
    return merge(left_sublist, right_sublist)

def merge(left, right):
    merged = []
    i = j = 0
    
    # Merge the two sublists into a sorted sublist
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Append the remaining elements of either sublist
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged
```

In the above implementation, `arr` is the input list that needs to be sorted. The `merge_sort` function is the main driver function that divides the input list into two sublists, recursively applies merge sort to each sublist, and then merges the sorted sublists using the `merge` function.

The `merge` function takes two sorted sublists (`left` and `right`) and merges them into a single sorted sublist. It compares the elements from both sublists and adds the smaller element to the merged sublist. The process continues until all elements from both sublists are merged.

Finally, the sorted list is returned.

The time complexity of the merge sort algorithm is $O(n log n)$, where $n$ is the number of elements in the input list. Merge sort has a better worst-case and average-case time complexity compared to quadratic time complexity sorting algorithms like bubble sort and insertion sort.