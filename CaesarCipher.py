LetterToIndex = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))) # Integer Output
IndexToLetter = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ")) # Char Output

def CaesarEncode(plaintext, key):
    ciphertext = ''
    for i in plaintext.upper():
        if i.isalpha():
            ciphertext += IndexToLetter[ (LetterToIndex[i] + key)%26 ]
        else:
            ciphertext += i
    print(ciphertext)


def CaesarDecode(cipherText, key):
    plaintext = ''
    for i in cipherText.upper():
        if i.isalpha():
            plaintext += IndexToLetter[ (LetterToIndex[i] - key)%26 ]
        else:
            plaintext += i
    print(plaintext)


# Testing algorithms
CaesarEncode('lomrlo', 4)
CaesarDecode('PSQVPS', 4)