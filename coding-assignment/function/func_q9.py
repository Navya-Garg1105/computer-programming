# Find the Sum of Digits
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = int(input("Enter a number: "))
print(f"The sum of digits of {number} is {sum_of_digits(number)}.")
