def median(a: int, b: int, c: int) -> int:
    """Calculates the median using conditional (if-else) logic."""
    if (a >= b and a <= c) or (a <= b and a >= c):
        return a
    elif (b >= a and b <= c) or (b <= a and b >= c):
        return b
    else:
        return c

def median2(a: int, b: int, c: int) -> int:
    """Calculates the median by sorting the numbers in a list."""
    numbers = [a, b, c]
    numbers.sort()
    return numbers[1] # The middle element of 3 items after sorting is at index 1

def main():
    # Task 3: Test cases for both functions
    print("--- Testing median (Task 1) ---")
    print(f"median(25, 11, 33) -> {median(25, 11, 33)}")  # Expected: 25
    print(f"median(1, 1, 2) -> {median(1, 1, 2)}")        # Expected: 1
    print(f"median(10, 20, 5) -> {median(10, 20, 5)}")    # Expected: 10

    print("\n--- Testing median2 (Task 2) ---")
    print(f"median2(25, 11, 33) -> {median2(25, 11, 33)}") # Expected: 25
    print(f"median2(1, 1, 2) -> {median2(1, 1, 2)}")      # Expected: 1
    print(f"median2(10, 20, 5) -> {median2(10, 20, 5)}")  # Expected: 10

if __name__ == "__main__":
    main()