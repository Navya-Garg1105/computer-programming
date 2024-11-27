# Merge Two Tuples and Remove Duplicates
# Take two tuples from the user, merge them, and remove any duplicate elements.
tuple1 = tuple(input("Enter the first tuple values separated by commas: ").split(','))
tuple2 = tuple(input("Enter the second tuple values separated by commas: ").split(','))

# Merge the two tuples and remove duplicates by converting to a set
merged_tuple = tuple(set(tuple1 + tuple2))

print(f"The merged tuple with no duplicates is: {merged_tuple}")
