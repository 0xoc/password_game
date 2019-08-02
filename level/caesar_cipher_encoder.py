import json
def caesar_cipher_encoder(msg, key):
    j = 0
    len_key = len(key)
    
    encoded = []

    for i in range(len(msg)):
        if j == len_key:
            j = 0
        encoded += [ ord(msg[i]) + ord(key[j]) ]
        j += 1

    return encoded