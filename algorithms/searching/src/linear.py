def linear_search(arr, target):
    found = False
    
    for i in range(len(arr)):
        if arr[i] == target:
            found = True
            return i
    
    if not found:
        return "Target value not found."