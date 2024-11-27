# Reverse Each String in a List
#Write a program to reverse each string in a list of user-input strings.
print("Reverse Each String in a List")
my_list = input("Enter strings separated by spaces: ").split()
reversed_list = [x[::-1] for x in my_list]
print("Reversed strings:")
for x in reversed_list:
    print(x)


