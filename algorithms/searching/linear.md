# Linear Search Algorithm

Linear search, also known as sequential search, is a simple searching algorithm that iterates through a list of elements to find a target value. It works by checking each element in the list one by one until the target value is found or the end of the list is reached.

The steps involved in the linear search algorithm are as follows:

1. **Input:** Take an input list of elements and a target value to search for.
2. **Initialization:** Set a variable `found` to `False` to indicate that the target value has not been found.
3. **Iterate:** Start iterating through the elements of the list, beginning from the first element.
4. **Comparison:** Compare each element with the target value.
5. **Found:** If the current element matches the target value, set `found` to `True` and break out of the loop.
6. **Not Found:** If the end of the list is reached without finding a match, the target value is not present.
7. **Output:** Return the index of the target value if found, or a message indicating it was not found.

Here is a Python implementation of the linear search algorithm:

```python
def linear_search(arr, target):
    found = False
    
    for i in range(len(arr)):
        if arr[i] == target:
            found = True
            return i
    
    if not found:
        return "Target value not found."
```

In the above implementation, `arr` is the input list and `target` is the value we are searching for. The algorithm iterates through each element in the list and compares it with the target value. If a match is found, the function returns the index of the element. If the end of the list is reached without finding a match, a message indicating the target value was not found is returned.

The time complexity of the linear search algorithm is O(n), where n is the number of elements in the list. This means that the time it takes to search for a target value grows linearly with the size of the list.