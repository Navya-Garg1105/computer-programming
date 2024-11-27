# Check if a Tuple Contains a Specific Element
# Take a tuple and an element from the user, then check if the element exists in the tuple.
input_tuple = tuple(input("Enter tuple values separated by commas: ").split(','))
element = input("Enter element to check if it exists: ")

if element in input_tuple:
    print(f"The element '{element}' is in the tuple.")
else:
    print(f"The element '{element}' is not in the tuple.")
