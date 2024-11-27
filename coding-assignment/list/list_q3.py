# Sort the list in ascending order.
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]  # Convert to integers
my_list.sort()
print("Sorted list:", my_list)
