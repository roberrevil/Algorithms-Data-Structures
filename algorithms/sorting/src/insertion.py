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