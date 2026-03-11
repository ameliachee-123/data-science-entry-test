def find_first_negative(lst):
    """
    This function finds the first negative number in a list.
    If there are no negative numbers, it returns "No negatives".
    """

    # Start checking from the first index
    i = 0

    # Use a while loop to go through the list
    while i < len(lst):
        # Check if the current number is negative
        if lst[i] < 0:
            return lst[i]

        # Move to the next item in the list
        i += 1

    # If no negative numbers were found
    return "No negatives"


# Testing the function
print(find_first_negative([3, 5, -1, 7, -2, 8]))
print(find_first_negative([2, 10, 7, 0]))
