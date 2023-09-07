def is_divisible_by_5(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number % 5 == 0

# Read input binary numbers from the user
input_numbers = input("Enter comma-separated 4-digit binary numbers: ").split(',')

# Check and filter numbers divisible by 5
divisible_by_5 = [num for num in input_numbers if is_divisible_by_5(num.strip())]

# Print the result
output = ",".join(divisible_by_5)
print("Output:", output)
