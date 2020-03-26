from pycipher import ADFGVX
key='ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8'
keyword='HELLO'
plaintext = "Attack at once"
ciphertext = ADFGVX(key,keyword).encipher(plaintext)
print(ciphertext)
plaintext = ADFGVX(key,keyword).decipher(ciphertext) 
print(plaintext)