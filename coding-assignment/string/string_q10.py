'''capitalizing first letter of each word in a scentence
# Taking input from the user
line = input("Enter a string: ")

# Capitalize each word manually
words = line.split()
result = ""
for word in words:
    # Convert the first character to uppercase and the rest to lowercase
    capitalized_word = word[0].upper() + word[1:].lower()
    result += capitalized_word + " "

# Remove the trailing space
result = result.strip()

# Output the result
print(result)
