def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read input from the user
number = int(input("Enter a number: "))

# Compute and display the factorial
result = factorial(number)
print(f"The factorial of {number} is {result}")
