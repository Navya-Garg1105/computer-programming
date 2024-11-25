#check whether the given string is anagram or not
str = input()
count = 0
str2 = input()
for i in range(len(str)):
  for j in range(len(str2)):
    if i == j :
      count = count + 1
if count == len(str):
  print("anagram")
else:
  print("not anagram")
