# Count Occurrences of an Element in a Tuple
# Take a tuple and an element from the user, then count how many times the element appears in the tuple.
input_tuple = tuple(input("Enter tuple values separated by commas: ").split(','))
element = input("Enter element to count: ")
count = input_tuple.count(element)
print(f"The element '{element}' appears {count} time(s) in the tuple.")
