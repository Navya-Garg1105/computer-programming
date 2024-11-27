# Remove a Key-Value Pair from a Dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

key = input("Enter the key to remove: ")
if key in my_dict:
    del my_dict[key]
    print(f"Key '{key}' removed.")
else:
    print("Key not found.")

print(my_dict)
