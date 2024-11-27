#  Iterate Over Dictionary Values
my_dict = {}
num_items = int(input("How many items do you want to add? "))
for _ in range(num_items):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value

for value in my_dict.values():
    print(value)
