# Fibonacci Sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the number of Fibonacci terms to generate: "))
print(f"Fibonacci sequence: {fibonacci(n)}")
