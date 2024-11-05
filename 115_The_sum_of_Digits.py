# 113. The sum of Digits: Write a recursive Python function called sum_of_digits that takes an integer as input and returns the sum of its digits.

def sum_of_digits(n):
    """
    Recursive function to calculate the sum of digits of a number.

    Parameters:
    n (int): The number whose digits will be summed.

    Returns:
    int: The sum of the digits of the number.
    """
    # Base case: if n is a single digit
    if n < 10:
        return n
    # Recursive case: sum of the last digit and sum of digits of the rest of the number
    else:
        return n % 10 + sum_of_digits(n // 10)

# Test the function with different values
print(sum_of_digits(123))  # Output: 6 (1 + 2 + 3)
print(sum_of_digits(9876)) # Output: 30 (9 + 8 + 7 + 6)
print(sum_of_digits(405))  # Output: 9 (4 + 0 + 5)
