# Task 1: Difference between in-place and out-of-place sorting algorithms
# - An "in-place" sorting algorithm sorts the array by modifying the original 
#   array directly, using a minimal amount of extra memory (O(1) auxiliary space).
# - An "out-of-place" sorting algorithm creates and returns a completely new 
#   sorted array or list while leaving the original input data unchanged, 
#   typically requiring O(n) additional memory.



def selection_sort(array: list) -> None:
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element of the unsorted part
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]



if __name__ == "__main__":
    # Test selection_sort
    sample_array = [64, 25, 12, 22, 11]
    print(f"Original array: {sample_array}")
    
    selection_sort(sample_array)
    
    print(f"Sorted array: {sample_array}")