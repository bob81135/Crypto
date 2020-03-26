from pycipher import ADFGX
key='phqgmeaylnofdxkrcvszwbuti'
keyword='HELLO'
plaintext = "Attack at once"
ciphertext = ADFGX(key,keyword).encipher(plaintext)
print(ciphertext)
plaintext = ADFGX(key,keyword).decipher(ciphertext) 
print(plaintext)