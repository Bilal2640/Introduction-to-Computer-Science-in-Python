def transform_to_dual(dec: int) -> str:
    """Transforms a positive integer from base 10 to a binary string (base 2)."""
    if dec <= 0:
        return "0"
    
    binary_str = ""
    while dec > 0:
        remainder = dec % 2  # Find the remainder (0 or 1)
        binary_str = str(remainder) + binary_str  # Prepend to the front of the string
        dec = dec // 2  # Integer division to reduce the number
        
    return binary_str

def main():
    # Task 2: Test cases
    print("--- Testing transform_to_dual ---")
    print(f"transform_to_dual(13) -> {transform_to_dual(13)}")  # Expected: "1101"
    print(f"transform_to_dual(2) -> {transform_to_dual(2)}")    # Expected: "10"
    print(f"transform_to_dual(8) -> {transform_to_dual(8)}")    # Expected: "1000"
    print(f"transform_to_dual(1) -> {transform_to_dual(1)}")    # Expected: "1"

if __name__ == "__main__":
    main() 