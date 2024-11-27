# Check if a Key Exists in a Dictionary 
my_dict = {'a': 1, 'b': 2, 'c': 3}

key = input("Enter the key to check: ")
if key in my_dict:
    print(f"Key '{key}' found with value: {my_dict[key]}")
else:
    print(f"Key '{key}' not found.")
