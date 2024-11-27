# Write a program that removes all non-alphabetic characters from a string.
def remove_non_alpha(s):
    return ''.join(char for char in s if char.isalpha())

string = "hello@123"
print(remove_non_alpha(string))
