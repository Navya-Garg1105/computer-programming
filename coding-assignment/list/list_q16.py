#Shift Elements by One Position
#Write a program to cyclically shift all elements in a list by one position to the right.
print("Cyclically Shift Elements by One Position")
my_list = input("Enter elements of the list separated by spaces: ").split()
if my_list:
    shifted_list = [my_list[-1]] + my_list[:-1]
    print("List after shifting:")
    for x in shifted_list:
        print(x)
else:
    print("The list is empty!")
