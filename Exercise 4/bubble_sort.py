def bubble_sort(array: list) -> None:
    n = len(array)
    for i in range(n):
        swapped = False
        
        # The last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
                
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break



if __name__ == "__main__":
    # Test bubble_sort
    sample_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {sample_array}")
    
    bubble_sort(sample_array)
    
    print(f"Sorted array: {sample_array}")