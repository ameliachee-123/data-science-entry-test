def check_divisibility(num, divisor):
    """
    This function checks if one number is divisible by another.
    It returns True if divisible, otherwise False.
    """

    # Check if both inputs are numbers
    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1

    # Use modulus (%) to check for remainder
    if num % divisor == 0:
        return True
    else:
        return False


# Testing the function
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
