def find_and_replace(lst, find_val, replace_val):
    """
    This function searches through a list and replaces all occurrences
    of a specific value with another value.
    It returns the modified list.
    """

    # Check if the input is actually a list
    if not isinstance(lst, list):
        return -1

    # Loop through the list and check each item
    for i in range(len(lst)):
        # If the item matches the value we want to find
        if lst[i] == find_val:
            # Replace it with the new value
            lst[i] = replace_val

    # Return the updated list
    return lst


# Testing the function
print(find_and_replace([1, 2, 3, 4, 2, 2], 2, 5))
print(find_and_replace(["apple", "banana", "apple"], "apple", "orange"))
