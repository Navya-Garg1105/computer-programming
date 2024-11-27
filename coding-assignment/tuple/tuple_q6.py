# Remove an Element from a Tuple 
# Take a tuple and an element from the user, then remove the first occurrence of the element from the tuple.
input_tuple = tuple(input("Enter tuple values separated by commas: ").split(','))
element = input("Enter element to remove: ")

if element in input_tuple:
    temp_list = list(input_tuple)  # Convert tuple to list
    temp_list.remove(element)
    input_tuple = tuple(temp_list)  # Convert list back to tuple
    print(f"The tuple after removal is: {input_tuple}")
else:
    print(f"The element '{element}' is not in the tuple.")
