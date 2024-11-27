# Check Armstrong Number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    return n == sum(int(digit) ** num_digits for digit in num_str)

number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
