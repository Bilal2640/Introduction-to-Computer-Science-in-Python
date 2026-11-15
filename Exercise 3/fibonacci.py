# Task 2: Tree recursion explanation comment block
# Tree recursion happens when a function calls itself multiple times within a single
# execution branch. For fib1(n), every call to fib1 branches into two additional
# recursive calls (fib(n-1) and fib(n-2)), causing the number of function calls
# to grow exponentially like a binary tree (approximately 2^n growth).


number_recursive_calls = 0
number_loop_iterations = 0



def fib1(n: int) -> int:
    global number_recursive_calls
    number_recursive_calls += 1
    
    if n == 0 or n == 1:
        return 1
    return fib1(n - 2) + fib1(n - 1)



def fib2(n: int) -> int:
    global number_loop_iterations
    number_loop_iterations = 0
    
    if n == 0 or n == 1:
        return 1
    
    a = 1
    b = 1
    for _ in range(2, n + 1):
        number_loop_iterations += 1
        next_val = a + b
        a = b
        b = next_val
        
    return b



if __name__ == "__main__":
    # 1. Print out the first 15 Fibonacci numbers using fib1
    print("First 15 Fibonacci numbers (using fib1):")
    for i in range(15):
        print(f"fib1({i}) = {fib1(i)}")
        
    print("\n" + "="*40 + "\n")
    
    # 4. Calculate the 23rd Fibonacci number using both functions and count calls/iterations
    number_recursive_calls = 0
    val_fib1 = fib1(23)
    calls_fib1 = number_recursive_calls
    
    number_loop_iterations = 0
    val_fib2 = fib2(23)
    iterations_fib2 = number_loop_iterations
    
    print(f"23rd Fibonacci number (fib1): {val_fib1} with {calls_fib1} recursive calls.")
    print(f"23rd Fibonacci number (fib2): {val_fib2} with {iterations_fib2} loop iterations.")