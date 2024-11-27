# Calculate Power
def power(base, exp):
    return base ** exp

base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} raised to the power {exponent} is {power(base, exponent)}.")
