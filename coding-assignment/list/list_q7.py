# Filter Even Numbers
my_list = input("Enter numbers separated by spaces: ").split()
my_list = [int(x) for x in my_list]
evens = [x for x in my_list if x % 2 == 0]
print("Even numbers:", evens)
