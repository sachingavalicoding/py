def sort_sentences(text):
    # Split the input into sentences
    sentences = text.split(".")
    
    # Remove extra spaces and empty strings
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    # Sort the sentences alphabetically
    sorted_sentences = sorted(sentences)
    
    # Combine back into a single string
    result = ". ".join(sorted_sentences) + "."
    return result


# Example usage
text = "The cat sat on the mat. Apples are tasty. Zebras live in Africa. Dogs are loyal."
sorted_text = sort_sentences(text)
print("Sorted Sentences:")
print(sorted_text)
