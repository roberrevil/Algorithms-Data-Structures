def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # Select the first element as the pivot
    less_than = [x for x in arr[1:] if x <= pivot]
    greater_than = [x for x in arr[1:] if x > pivot]
    
    return quicksort(less_than) + [pivot] + quicksort(greater_than)