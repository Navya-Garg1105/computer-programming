#Count Occurrences of Each Element
# Write a program to count and display how many times each element appears in a user-input list.
print("Count Occurrences of Each Element")
my_list = input("Enter elements of the list separated by spaces: ").split()
frequency = {}
for item in my_list:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Occurrences of each element:")
for key, value in frequency.items():
    print(f"{key}: {value} times")

