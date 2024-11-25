# counts the number of vowel in a string
str = input()
count = 0
v = 'aeiouAEIOU'
for i in str:
    if i in v:
        count += 1
print(count)
