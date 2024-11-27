# Check if String is Numeric
string = "12345"
is_numeric = True

for char in string:
    if not char.isdigit():
        is_numeric = False
        break

if is_numeric:
    print("The string is numeric.")
else:
    print("The string is not numeric.")
