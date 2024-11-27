# Find the Length of a Dictionary
my_dict = {}

num_items = int(input("How many items do you want to add? "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

print(f"The dictionary has {len(my_dict)} items.")
