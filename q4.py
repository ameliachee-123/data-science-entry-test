def string_reverse(s):
    """
    This function reverses a string.
    If the input is not a string, it returns -1.
    """

    # Check if the input is a string
    if not isinstance(s, str):
        return -1

    # Reverse the string using Python slicing
    return s[::-1]


# Testing the function
print(string_reverse("Hello World"))
print(string_reverse("Python"))
