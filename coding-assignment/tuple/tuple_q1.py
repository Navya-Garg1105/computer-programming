# Take multiple values from the user and create a tuple
input_values = input("Enter values separated by commas: ").split(',')
input_tuple = tuple(input_values)
print(f"The tuple is: {input_tuple}")
