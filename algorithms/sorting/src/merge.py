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