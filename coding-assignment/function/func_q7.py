# Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

string = input("Enter a string: ")
print(f"The number of vowels in the string is {count_vowels(string)}.")
