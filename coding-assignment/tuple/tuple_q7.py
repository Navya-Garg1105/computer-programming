# Find the Maximum and Minimum Element in a Tuple of Integers
#Take a tuple of integers from the user and find the maximum and minimum values.
input_tuple = tuple(map(int, input("Enter tuple values separated by commas: ").split(',')))
print(f"The maximum value in the tuple is: {max(input_tuple)}")
print(f"The minimum value in the tuple is: {min(input_tuple)}")
