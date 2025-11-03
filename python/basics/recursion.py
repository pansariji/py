# def factorial(n):
#     if n==1 or 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)    
# 5 * 4 * 3 * 2 * factorial(1) 
# 5 * 4 * 3 * 2 * 1 = 120


#--------febunacci series using recursion--------
def fibonacci_recursive(n):
    """
    Recursive function to return the nth Fibonacci number.
    """
    # Base cases for the recursion
    if n <= 1:
        return n
    # Recursive step
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

## For printing at a particular value n
print(fibonacci_recursive(num_terms))

## For printing sequence
# if num_terms <= 0:
#     print("Please enter a positive number of terms.")
# else:
#     print("Fibonacci sequence:")
#     for i in range(num_terms):
#         print(fibonacci_recursive(i), end=" ")
#     print() # For a clean newline at the end
