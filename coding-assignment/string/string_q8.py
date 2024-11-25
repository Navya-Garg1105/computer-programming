#town market sale
# input 123 456 789
#output 321 654 987 
str = input()
for i in str.split():
    print(i[::-1],end=' ')
