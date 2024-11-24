import random
import math

# Define the mathematical function
def f(x):
    return -1 * (x**2) + 5 * x + 10  # Example: f(x) = -x^2 + 5x + 10

# Hill Climbing Algorithm
def hill_climb(start, step_size, iterations):
    current_x = start
    current_value = f(current_x)

    for _ in range(iterations):
        # Generate a new candidate in the neighborhood
        next_x = current_x + random.uniform(-step_size, step_size)
        next_value = f(next_x)

        # If the new candidate is better, move to it
        if next_value > current_value:
            current_x, current_value = next_x, next_value

    return current_x, current_value

# Parameters
start = random.uniform(-10, 10)  # Random starting point
step_size = 0.1                 # Step size for exploring neighborhood
iterations = 1000               # Number of iterations

# Run Hill Climbing
max_x, max_value = hill_climb(start, step_size, iterations)
print(f"Maximum value found: f({max_x:.2f}) = {max_value:.2f}")
