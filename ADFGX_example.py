from pycipher import ADFGX
key='phqgmeaylnofdxkrcvszwbuti'
keyword='HELLO'
ciphertext = "Attack at once"
plaintext = ADFGX(key,keyword).encipher(ciphertext)
print(plaintext)
ciphertext = ADFGX(key,keyword).decipher(plaintext) 
print(ciphertext)