# Merge Two Dictionaries
dict1 = {}
dict2 = {}

num_items1 = int(input("How many items for the first dictionary? "))
for _ in range(num_items1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

num_items2 = int(input("How many items for the second dictionary? "))
for _ in range(num_items2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Merging the two dictionaries
merged_dict = dict1.copy()  # Create a copy of the first dictionary
for key, value in dict2.items():
    merged_dict[key] = value

print(merged_dict)
