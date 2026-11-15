def insertion_sort(array: list) -> None:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        
        # Move elements of array[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            
        array[j + 1] = key



if __name__ == "__main__":
    # Test insertion_sort
    sample_array = [12, 11, 13, 5, 6]
    print(f"Original array: {sample_array}")
    
    insertion_sort(sample_array)
    
    print(f"Sorted array: {sample_array}")