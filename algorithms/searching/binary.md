# Binary Search Algorithm

Binary search is an efficient searching algorithm used to find a target value in a sorted list of elements. It works by repeatedly dividing the search space in half and comparing the middle element with the target value. Based on the comparison, the algorithm eliminates half of the remaining search space and continues the process until the target value is found or the search space is empty.

The steps involved in the binary search algorithm are as follows:

1. **Input:** Take an input sorted list of elements and a target value to search for.
2. **Initialization:** Set variables `low` and `high` to the start and end indices of the search space, respectively.
3. **Search Space Check:** Check if the search space represented by `low` and `high` is empty (i.e., `low > high`).
4. **Middle Element:** Calculate the middle index of the search space as `mid = (low + high) // 2`.
5. **Comparison:** Compare the middle element of the search space with the target value.
6. **Match Found:** If the middle element is equal to the target value, return its index.
7. **Adjust Search Space:** If the middle element is greater than the target value, set `high = mid - 1` to search the left half of the search space. Otherwise, set `low = mid + 1` to search the right half of the search space.
8. **Repeat:** Repeat steps 3-7 until the target value is found or the search space is empty.
9. **Output:** Return a message indicating that the target value was not found.

Here is a Python implementation of the binary search algorithm:

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return "Target value not found."
```

In the above implementation, `arr` is the input sorted list and `target` is the value we are searching for. The algorithm repeatedly divides the search space in half by calculating the middle index (`mid`). It compares the middle element with the target value and adjusts the search space accordingly. If a match is found, the function returns the index of the element. If the search space is empty (i.e., `low > high`), a message indicating that the target value was not found is returned.

The time complexity of the binary search algorithm is O(log n), where n is the number of elements in the sorted list. This means that the time it takes to search for a target value grows logarithmically with the size of the list. Binary search is more efficient than linear search for large sorted lists.