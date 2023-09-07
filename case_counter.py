def count_case(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# Read input sentence from the user
input_sentence = input("Enter a sentence: ")

# Calculate the count of uppercase and lowercase letters
upper, lower = count_case(input_sentence)

# Print the result
print("UPPER CASE", upper)
print("LOWER CASE", lower)
