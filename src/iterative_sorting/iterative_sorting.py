# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
        # Assume the one we're on is the smallest
        min_value = arr[cur_index]
        smallest_index = i
        
        # Check if it's not
        for inner_i in range(cur_index+1, len(arr)):
            if arr[inner_i] < min_value:
                min_value = arr[inner_i]
                smallest_index = inner_i

        # TO-DO: swap
        old_value = arr[cur_index]
        arr[cur_index] = min_value
        arr[smallest_index] = old_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Instantiate swap count
    swap_count = 0

    # Bubbling action
    def bubble(arr):
        # Grab swap count
        nonlocal swap_count

        # Loop through array (except last one)
        for i in range(len(arr) - 1):
            # Swap if the next entry is smaller
            if arr[i + 1] < arr[i]:
                first = arr[i]
                second = arr[i + 1]
                arr[i] = second
                arr[i + 1] = first

                # Add to the swap count
                swap_count += 1
                # print(f"Swapped: {swap_count}")

        # Check the swap count
        if swap_count == 0:
            return arr

        elif swap_count > 0:
            # Reset and bubble again
            swap_count = 0
            return bubble(arr)

    result = bubble(arr)

    return result

# # Test bubble_sort
# lst = [1, 3, 2, 4, 6, 5]
# print(bubble_sort(lst))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr