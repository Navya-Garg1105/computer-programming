# Find the Maximum Value in a Dictionary 
my_dict = {}
num_items = int(input("How many items do you want to add? "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = int(input("Enter value: "))  # Convert the value to integer
    my_dict[key] = value

max_key = max(my_dict, key=my_dict.get)
print(f"The key with the maximum value is '{max_key}' with value {my_dict[max_key]}")
