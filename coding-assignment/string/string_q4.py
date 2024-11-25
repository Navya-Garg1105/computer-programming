'''implement a program that counts the frequency of each character in a string'''
st = input('enter string  ')
reg = ''
str = ''
dict = {}
for i in st:
    if i not in reg:
        v = st.count(i)
        dict[i] = v
print(dict)
