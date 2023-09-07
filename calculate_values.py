import math

# Fixed values
C = 50
H = 30

# Read input from the user
input_sequence = input("Enter comma-separated values of D: ")

# Split the input sequence and calculate the values
values = input_sequence.split(',')
results = []

for item in values:
    D = int(item)
    Q = int(math.sqrt((2 * C * D) / H))
    results.append(Q)

# Print the calculated values
output = ', '.join(map(str, results))
print(f"The output of the program should be: {output}")
