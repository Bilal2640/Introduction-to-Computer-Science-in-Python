def search_linear(a: list[str], item: str) -> int | None:
    for i in range(len(a)):
        if a[i] == item:
            return i
    return None



def search_binary(a: list[str], item: str) -> int | None:
    left = 0
    right = len(a) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == item:
            return mid
        elif a[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
            
    return None



def search_linear_cmp_count(a: list[str], item: str) -> int:
    comparisons = 0
    for i in range(len(a)):
        comparisons += 1
        if a[i] == item:
            return comparisons
    return comparisons



def search_binary_cmp_count(a: list[str], item: str) -> int:
    left = 0
    right = len(a) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if a[mid] == item:
            return comparisons
        
        comparisons += 1
        if a[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
            
    return comparisons



if __name__ == "__main__":
    bookshelf = ["Algorithm Design", "Clean Code", "Introduction to Algorithms", "Python Crash Course", "Refactoring"]
    
    target = "Clean Code"
    
    print(f"Searching for '{target}'...")
    print("Linear Search Index:", search_linear(bookshelf, target))
    print("Binary Search Index:", search_binary(bookshelf, target))
    
    print("Linear Search Comparisons:", search_linear_cmp_count(bookshelf, target))
    print("Binary Search Comparisons:", search_binary_cmp_count(bookshelf, target))