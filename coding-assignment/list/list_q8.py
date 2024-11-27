# Write a program to check if an element is present in a list.
my_list = input("Enter elements of the list separated by spaces: ").split()
element = input("Enter the element to check: ")
print(f"{element} is in the list: {element in my_list}")
