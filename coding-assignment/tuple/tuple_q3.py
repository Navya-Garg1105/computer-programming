# Find the Index of an Element in a Tuple
input_tuple = tuple(input("Enter tuple values separated by commas: ").split(','))
element = input("Enter element to find index: ")

if element in input_tuple:
    index = input_tuple.index(element)
    print(f"The element '{element}' is at index {index}.")
else:
    print(f"The element '{element}' is not in the tuple.")
