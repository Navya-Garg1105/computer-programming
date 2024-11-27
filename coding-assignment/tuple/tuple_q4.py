# Concatenate Two Tuples
# Take two tuples from the user and concatenate them.
tuple1 = tuple(input("Enter first tuple values separated by commas: ").split(','))
tuple2 = tuple(input("Enter second tuple values separated by commas: ").split(','))
result = tuple1 + tuple2
print(f"The concatenated tuple is: {result}")
