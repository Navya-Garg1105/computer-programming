# chcek whether the given string is rotation or not
str1 = input("enter the string1: ")
str2 = input("enter the string2: ")
flag = 0
for i in range(len(str1)):
     str1 = str1[-1] + str1[:len(str1)-1]
     if str1 == str2:
          flag = 1
          break
if flag == 1:
     print(True)
else:
     print(False)
