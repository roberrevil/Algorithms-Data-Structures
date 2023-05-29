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