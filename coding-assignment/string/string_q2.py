'''palindrome of a string'''
str = input()
v = str[::-1]
if v == str:
    print("palindrome")
else:
    print("not palindrame")
