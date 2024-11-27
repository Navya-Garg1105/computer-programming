#Remove Elements at Even Indices
print("Remove Elements at Even Indices")
my_list = input("Enter elements of the list separated by spaces: ").split()
filtered_list = [my_list[i] for i in range(len(my_list)) if i % 2 != 0]
print("List after removing elements at even indices:")
for x in filtered_list:
    print(x)
