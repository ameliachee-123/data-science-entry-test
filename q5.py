def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    if not isinstance(num, (int, float)) or not isinstance(divisor, (int, float)):
        return -1

    if num % divisor == 0:
        return True
    else:
        return False


# Task 2
print(check_divisibility(10, 2))
print(check_divisibility(7, 3))
