# Check if Dictionary is Empty
my_dict = {}
num_items = int(input("How many items do you want to add? "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

if not my_dict:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")
