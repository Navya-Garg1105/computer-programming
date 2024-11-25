#write a program that removes all whitespaces from a string
text = input("enter string")

# Removing all whitespaces
result = "".join(char for char in text if not char.isspace())

print("String without whitespaces:", result)
