# Convert a Decimal Number to Binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary if binary else "0"

number = int(input("Enter a decimal number: "))
print(f"The binary representation of {number} is {decimal_to_binary(number)}.")
