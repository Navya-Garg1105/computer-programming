# Find Elements Greater than a Given Value
# Write a program to find all elements in a list greater than a user-specified value.
print("Find Elements Greater than a Given Value")
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
threshold = int(input("Enter the threshold value: "))
greater_elements = [x for x in my_list if x > threshold]
print("Elements greater than the threshold:")
for x in greater_elements:
    print(x)
