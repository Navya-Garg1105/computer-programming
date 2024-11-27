# Find the First Non-Repeating Character
string = "swiss"
found = False

for char in string:
    if string.count(char) == 1:
        print(char)
        found = True
        break

if not found:
    print(None)
