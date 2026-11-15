def is_prime(n: int) -> bool:
    """Takes an integer n and returns True if and only if n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n: int) -> int:
    """Returns the next prime number p that is larger than or equal to n."""
    current = n
    while True:
        if is_prime(current):
            return current
        current += 1

def main():
    # Suitable test cases for the functions
    print("--- Testing is_prime ---")
    print(f"is_prime(2) -> {is_prime(2)}")    # Expected: True
    print(f"is_prime(4) -> {is_prime(4)}")    # Expected: False
    print(f"is_prime(11) -> {is_prime(11)}")  # Expected: True
    print(f"is_prime(1) -> {is_prime(1)}")    # Expected: False

    print("\n--- Testing next_prime ---")
    print(f"next_prime(14) -> {next_prime(14)}")  # Expected: 17
    print(f"next_prime(11) -> {next_prime(11)}")  # Expected: 11

if __name__ == "__main__":
    main()