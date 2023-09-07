def generate_2d_array(X, Y):
    array = []
    for i in range(X):
        row = []
        for j in range(Y):
            row.append(i * j)
        array.append(row)
    return array

# Read input from the user
X = int(input("Enter the value of X: "))
Y = int(input("Enter the value of Y: "))

# Generate and print the 2-dimensional array
result = generate_2d_array(X, Y)
for row in result:
    print(row)
