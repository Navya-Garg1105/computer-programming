# Find the Longest Palindromic Substring
def longest_palindromic_substring(s):
    n = len(s)
    max_length = 1
    start = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > max_length:
                max_length = len(substring)
                start = i
    return s[start:start + max_length]

string = input("Enter a string: ")
print(f"The longest palindromic substring is: {longest_palindromic_substring(string)}.")

