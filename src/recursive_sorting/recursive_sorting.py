# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    merged_arr[:len(arrA)] = arrA
    merged_arr[len(arrA):] = arrB
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        split1 = arr[:midpoint]
        split2 = arr[midpoint:]
        merge_sort(split1)
        merge_sort(split2)
        
        # Sort
        i = j = k = 0
        
        while i < len(split1) and j < len(split2):
            if split1[i] > split2[j]:
                arr[k] = split1[i]
                i += 1
            elif split1[i] < split2[i]:
                arr[k] = split2[j]
                j += 1
                
            k += 1
            
        # Catch Stragglers
        while i < len(split1):
            arr[k] = split1[i]
            i += 1
            k += 1
            
        while j < len(split2):
            arr[k] = split2[j]
            j += 1
            k += 1

    arr = arr[::-1]
            
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
