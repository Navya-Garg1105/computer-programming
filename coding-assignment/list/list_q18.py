# Interleave Two Lists
# Write a program to interleave two user-input lists element by element.
print("Interleave Two Lists")
list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ")
interleaved = []
for i in range(max(len(list1), len(list2))):
    if i < len(list1):
        interleaved.append(list1[i])
    if i < len(list2):
        interleaved.append(list2[i])
print("Interleaved list:")
for x in interleaved:
    print(x)
