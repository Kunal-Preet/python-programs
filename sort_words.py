def sort_words(sequence):
    words = sequence.split(',')
    words.sort()
    sorted_sequence = ','.join(words)
    return sorted_sequence

# Read input from the user
input_sequence = input("Enter a comma-separated sequence of words: ")

# Sort and print the words
sorted_sequence = sort_words(input_sequence)
print("Sorted sequence:", sorted_sequence)
