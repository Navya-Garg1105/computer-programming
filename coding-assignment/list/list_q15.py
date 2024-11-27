# Remove All Negative Numbers
print("Remove All Negative Numbers")
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
non_negative = [x for x in my_list if x >= 0]
print("List after removing negative numbers:")
for x in non_negative:
    print(x)
