

import random


def _pad_key(plaintext, key):
    padded_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            padded_key += key[i % len(key)]
            i += 1
        else:
            padded_key += ' '
    return padded_key


def _encrypt_decrypt_char(plaintext_char, key_char, mode='encrypt'):


    if plaintext_char.isalpha():


        first_alpha = 'a'


        if plaintext_char.isupper():


            first_alpha = 'A'

        old_char_position = ord(plaintext_char) - ord(first_alpha)


        key_char_position = ord(key_char.lower()) - ord('a')


        if mode == 'encrypt':
            new_char_position = (old_char_position + key_char_position) % 26
        else:
            new_char_position = (old_char_position - key_char_position + 26) % 26



        return chr(new_char_position + ord(first_alpha))


    return plaintext_char

def encrypt(plaintext, key):
    ciphertext = ''
    padded_key = _pad_key(plaintext, key)


    for plaintext_char, key_char in zip(plaintext, padded_key):


        ciphertext += _encrypt_decrypt_char(plaintext_char, key_char)


    return ciphertext

def decrypt (ciphertext, key):
    plaintext = ''
    padded_key = _pad_key(ciphertext, key)

    for ciphertext_char, key_char in zip(ciphertext, padded_key):


        plaintext += _encrypt_decrypt_char(ciphertext_char, key_char, mode ='decrypt')



    return plaintext

def generateRandomKeyword():

    alphabets = 'ABCDEFGHIJKLMNOPQRSTUCWXYZ'

    length = random.randint(2, 12)

    sample = random.sample(alphabets, length)

    return ''.join(sample)


plaintext = input('Enter text: ').upper()

key = generateRandomKeyword()

ciphertext = encrypt(plaintext, key)


decrypted_plaintext = decrypt(ciphertext, key)

print(f'Text entered: {plaintext} ')

print(f'keyword: {key} ')

print(f'ciphertext: {ciphertext}')


print(f'decrypted plaintext: {decrypted_plaintext}')
