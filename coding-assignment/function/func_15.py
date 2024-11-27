#  Find All Divisors
def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]

number = int(input("Enter a number: "))
print(f"Divisors of {number} are: {find_divisors(number)}.")
