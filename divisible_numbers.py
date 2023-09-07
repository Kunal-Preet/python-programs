#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

# Initialize an empty list to store the numbers
result = []

# Iterate through the range from 2000 to 3200 (both included)
for num in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        result.append(num)

# Print the result as a comma-separated sequence on a single line
print(','.join(map(str, result)))
