import string

def remove_punctuation(input_string):
    return ''.join(char for char in input_string if char not in string.punctuation)

# Example usage
text = "Hello, world! How's it going?"
clean_text = remove_punctuation(text)
print("Original:", text)
print("Without punctuation:", clean_text)
