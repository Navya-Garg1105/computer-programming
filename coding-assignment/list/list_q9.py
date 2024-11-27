# Write a program to find the maximum and minimum elements in a numeric list.
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
print("Maximum:", max(my_list))
print("Minimum:", min(my_list))

