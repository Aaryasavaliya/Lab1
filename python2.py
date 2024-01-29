# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))

# Generate and print the Fibonacci sequence
fibonacci_result = generate_fibonacci(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_result}")
