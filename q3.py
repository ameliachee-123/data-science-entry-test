# q3.py
def update_dictionary(dct, key, value):
    """
    This function updates a dictionary with a new key-value pair.
    If the key already exists, it prints the original value first
    before updating it.
    """

    # Check if the key already exists in the dictionary
    if key in dct:
        # Print the current value before updating
        print(dct[key])

    # Add or update the key with the new value
    dct[key] = value

    # Return the updated dictionary
    return dct


# Testing the function
print(update_dictionary({}, "name", "Alice"))
print(update_dictionary({"age": 25}, "age", 26))
