#!/usr/bin/python3
def remove_char_at(input_str, n):
    # Check if n is a valid index
    if n < 0 or n >= len(input_str):
        return input_str  # Return the original string if n is out of bounds

    # Create a new string by slicing before and after the character at index n
    return input_str[:n] + input_str[n+1:]

# Example usage:
original_str = "Hello, World!"
index_to_remove = 5  # Remove the character 'o' at index 5 (C array index)
result_str = remove_char_at(original_str, index_to_remove)
print(result_str)  # Output: "Hello World!"

