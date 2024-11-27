# Iterate Over Dictionary Keys
my_dict = {}
num_items = int(input("How many items do you want to add? "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

for key in my_dict:
    print(key)
