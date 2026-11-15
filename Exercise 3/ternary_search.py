import time
import random


def binary_search(a: list[int], item: int) -> int | None:
    def helper(left: int, right: int) -> int | None:
        if left > right:
            return None
        
        mid = (left + right) // 2
        if a[mid] == item:
            return mid
        elif a[mid] < item:
            return helper(mid + 1, right)
        else:
            return helper(left, mid - 1)

    return helper(0, len(a) - 1)



def ternary_search(a: list[int], item: int) -> int | None:
    def helper(left: int, right: int) -> int | None:
        if left > right:
            return None
        
        # Calculate two mid points dividing the range into three parts
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        
        if a[mid1] == item:
            return mid1
        if a[mid2] == item:
            return mid2
            
        if item < a[mid1]:
            return helper(left, mid1 - 1)
        elif item > a[mid2]:
            return helper(mid2 + 1, right)
        else:
            return helper(mid1 + 1, mid2 - 1)

    return helper(0, len(a) - 1)



def time_binary_search(a: list[int], search_values: list[int]) -> float:
    start_time = time.perf_counter()
    for val in search_values:
        binary_search(a, val)
    return time.perf_counter() - start_time



def time_ternary_search(a: list[int], search_values: list[int]) -> float:
    start_time = time.perf_counter()
    for val in search_values:
        ternary_search(a, val)
    return time.perf_counter() - start_time



if __name__ == "__main__":
    # Generate sorted array and search values for testing (Task 3)
    array_size = 10000
    array = sorted(random.randint(0, 100000) for _ in range(array_size))
    search_vals = [random.choice(array) for _ in range(1000)]
    
    bin_time = time_binary_search(array, search_vals)
    tern_time = time_ternary_search(array, search_vals)
    
    print(f"Binary Search Time: {bin_time:.6f} seconds")
    print(f"Ternary Search Time: {tern_time:.6f} seconds")