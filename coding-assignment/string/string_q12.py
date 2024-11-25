# Write a Python program that takes an encrypted message and a shift value, then prints the decrypted message.
message = input("enter your message")
shift = int(input("enter the shift: "))
decrypt = ''
for i in message:
    if 'A' <= i <= 'Z':
        new_i = chr(((ord(i) - ord('A') - shift )%2 )+ ord('A'))
        decrypt = decrypt + new_i 
    elif 'a' <= i<= 'z':
        new_i = chr(((ord(i) - ord('a')-shift)%2 + ord('a')))
        decrypt = decrypt + new_i
    else:
        decrypt = decrypt + i
print(decrypt)
