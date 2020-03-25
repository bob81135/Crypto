msg = "ATTACKATDAWN"
key = "test"
key_len = len(key)
ciphertext = ""
for i in range(len(msg)):
    ciphertext += chr(ord(key[i%key_len])^ord(msg[i]))
print(ciphertext)
ans = ""
for i in range(len(ciphertext)):
    ans += chr(ord(key[i%key_len])^ord(ciphertext[i]))
print(ans)

    