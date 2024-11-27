# Find All Indices of a Given Element
print("Find All Indices of a Given Element")
my_list = input("Enter elements of the list separated by spaces: ").split()
element = input("Enter the element to find: ")
indices = []
for i in range(len(my_list)):
    if my_list[i] == element:
        indices.append(i)
if indices:
    print(f"The element '{element}' is found at indices: {indices}")
else:
    print(f"The element '{element}' is not in the list.")
