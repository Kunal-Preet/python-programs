import math

# Initialize the initial position
x, y = 0, 0

# Define the movements
movements = [("UP", 5), ("DOWN", 3), ("LEFT", 3), ("RIGHT", 2)]

# Process each movement
for direction, steps in movements:
    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

# Calculate the Euclidean distance from the origin
distance = math.sqrt(x**2 + y**2)

print(f"Current position: ({x}, {y})")
print(f"Distance from the origin: {distance:.2f}")
