# Write a program to flatten a nested list into a single list.
def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

nested_list = eval(input("Enter a nested list (e.g., [1, [2, 3], [4, [5, 6]]]): "))
print("Flattened list:", flatten(nested_list))
