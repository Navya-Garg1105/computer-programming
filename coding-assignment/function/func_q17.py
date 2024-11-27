#  Check if Two Strings are Anagrams
def are_anagrams(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
if are_anagrams(str1, str2):
    print(f'"{str1}" and "{str2}" are anagrams.')
else:
    print(f'"{str1}" and "{str2}" are not anagrams.')
