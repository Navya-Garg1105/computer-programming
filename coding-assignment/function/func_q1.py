# Calculate Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")
