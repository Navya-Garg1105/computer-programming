# find the longest word in a scentence
str = input("enter any scentence")
l = str.split()
largest = 0
for i in l:
    if len(i) > largest:
        largest = len(i)
        lword = i
print(lword)     
