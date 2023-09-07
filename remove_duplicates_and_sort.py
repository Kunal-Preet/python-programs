def remove_duplicates_and_sort(words):
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    return sorted_words

# Read input words from the user
input_words = input("Enter whitespace-separated words: ").split()

# Remove duplicates and sort the words
sorted_unique_words = remove_duplicates_and_sort(input_words)

# Print the result
output = " ".join(sorted_unique_words)
print("Output:", output)
