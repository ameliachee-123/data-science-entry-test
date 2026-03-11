def swap(x, y):
    """
    This function swaps the values of x and y.
    If either value is not a number, it returns -1.
    If both are numeric, it prints the swapped values.
    """

    # Check if both inputs are numbers (int or float)
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return -1

    # Swap the values of x and y
    x, y = y, x

    # Print the swapped values
    print(x, y)


# Testing the function with the given scenarios
print(swap("Apple", 10))
swap(9, 17)
