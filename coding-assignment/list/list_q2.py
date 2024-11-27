# Modify an Element
# Modify a specific element in the list.
my_list = input("Enter elements of the list separated by spaces: ").split()
index = int(input("Enter the index to modify: "))
new_value = input("Enter the new value: ")
my_list[index] = new_value
print("Modified list:", my_list)
