def caesar_encrypt(plaintext, shift):
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            shift %= 26
            if c.isupper():
                ciphertext += chr((ord(c) - 65 + shift) % 26 + 65)
            else:
                ciphertext += chr((ord(c) - 97 + shift) % 26 + 97)
        else:
            ciphertext += c
    return ciphertext

def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            shift %= 26
            if c.isupper():
                plaintext += chr((ord(c) - 65 - shift) % 26 + 65)
            else:
                plaintext += chr((ord(c) - 97 - shift) % 26 + 97)
        else:
            plaintext += c
    return plaintext

plaintext = "Dies ist ein geheimer Text"
shift = 3

ciphertext = caesar_encrypt(plaintext, shift)
print(ciphertext)  # "Glhw lvw whaw jlrw whawjvw vwkhqj"

decrypted_text = caesar_decrypt(ciphertext, shift)
print(decrypted_text)  # "Dies ist ein geheimer Text"
