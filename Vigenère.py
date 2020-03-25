msg = "ATTACKATDAWN"
key = "test"
key_len = len(key)
ciphertext = ""
for i in range(len(msg)):
    tag = ord(key[i%key_len])
    if(tag>90):
        tag-=32
    if(ord(msg[i])+(tag%65)>90):
        ciphertext+=chr(ord(msg[i])+(tag%65)-26)
    else:
        ciphertext+=chr(ord(msg[i])+(tag%65))
print(ciphertext)
    