# 111. Factorial Calculation: Write a recursive Python function called factorial that takes a non-negative integer as input and returns its factorial.

def factorial(n):
    """
    Recursive function to calculate the factorial of a non-negative integer.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Test the function with different values
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(7))  # Output: 5040
