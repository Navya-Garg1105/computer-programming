Write a Python program that replaces all the asterisks in the input string with vowels, in the order a, e, i, o, u, repeatedly.
str = input()
v = 'aeiou'
a = -1
st = ''
for i in str:
    if i == '*':
        a= a + 1
        st = st + v[a]
        if a == len(v)-1:
            a = -1
    else:
        st = st + i
print(st)
