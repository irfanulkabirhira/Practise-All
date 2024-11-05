# 112. Fibonacci Series: Write a recursive Python function called Fibonacci that takes an integer N as input and returns the Nth number in the Fibonacci series. The Fibonacci series is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

def Fibonacci(n):
    """
    Recursive function to calculate the Nth number in the Fibonacci series.

    Parameters:
    n (int): The position in the Fibonacci series.

    Returns:
    int: The Nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Test the function with different values
print(Fibonacci(0))  # Output: 0
print(Fibonacci(1))  # Output: 1
print(Fibonacci(5))  # Output: 5
print(Fibonacci(10)) # Output: 55
