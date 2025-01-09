def vigenere_cipher_encrypt(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    for i in range(len(plaintext_int)):
        if plaintext[i].isalpha():
            ascii_offset = ord('A') if plaintext[i].isupper() else ord('a')
            value = (plaintext_int[i] + key_as_int[i % key_length] - 2 * ascii_offset) % 26
            encrypted_text += chr(value + ascii_offset)
        else:
            encrypted_text += plaintext[i]
    return encrypted_text

def vigenere_cipher_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        if ciphertext[i].isalpha():
            ascii_offset = ord('A') if ciphertext[i].isupper() else ord('a')
            value = (ciphertext_int[i] - key_as_int[i % key_length] + 26) % 26
            decrypted_text += chr(value + ascii_offset)
        else:
            decrypted_text += ciphertext[i]
    return decrypted_text

plaintext = "HELLO VIGENERE CIPHER"
key = "KEY"
encrypted_text = vigenere_cipher_encrypt(plaintext, key)
decrypted_text = vigenere_cipher_decrypt(encrypted_text, key)

print(f"Original: {plaintext}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
