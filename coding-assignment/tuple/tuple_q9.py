# Unpack a Tuple into Multiple Variables
# Take a tuple from the user and unpack it into separate variables.
input_tuple = tuple(input("Enter tuple values separated by commas: ").split(','))
if len(input_tuple) >= 3:
    a, b, c = input_tuple[:3]
    print(f"Unpacked values: a = {a}, b = {b}, c = {c}")
else:
    print("Tuple does not have enough elements to unpack into three variables.")
