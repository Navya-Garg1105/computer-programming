# Generate a list of squares of numbers entered by the user.
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
squares = [x**2 for x in my_list]
print("Squares:", squares)
