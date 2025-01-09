# XOR encryption/decryption function
def xor_encrypt_decrypt(data, key):
    return bytes([b ^ key for b in data])

# Example fixed key
KEY = 0x42  # A simple key for XOR encryption
