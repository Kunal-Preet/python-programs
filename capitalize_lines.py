def capitalize_lines(lines):
    capitalized_lines = [line.upper() for line in lines]
    return capitalized_lines

# Read input lines from the user
input_lines = []
print("Enter lines (Enter an empty line to stop):")
while True:
    line = input()
    if not line:
        break
    input_lines.append(line)

# Capitalize and print the lines
capitalized_lines = capitalize_lines(input_lines)
print("Capitalized lines:")
for line in capitalized_lines:
    print(line)
