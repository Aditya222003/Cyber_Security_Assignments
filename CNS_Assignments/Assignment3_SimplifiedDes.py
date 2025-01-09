# Helper functions for bit manipulations
def permute(original, permutation):
    return ''.join(original[i - 1] for i in permutation)

def left_shift(bits, num_shifts):
    return bits[num_shifts:] + bits[:num_shifts]

def xor(bits1, bits2):
    return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bits1, bits2))

# S-Boxes for substitution step
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def s_box(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')

# Key generation: generates two 8-bit subkeys from a 10-bit key
def generate_keys(key):
    # P10 permutation
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    # P8 permutation
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    
    # Apply P10 to key
    key = permute(key, P10)
    
    # Split into two 5-bit halves
    left, right = key[:5], key[5:]
    
    # Left shift both halves by 1
    left, right = left_shift(left, 1), left_shift(right, 1)
    
    # Generate first subkey K1 by applying P8
    K1 = permute(left + right, P8)
    
    # Left shift both halves by 2
    left, right = left_shift(left, 2), left_shift(right, 2)
    
    # Generate second subkey K2 by applying P8
    K2 = permute(left + right, P8)
    
    return K1, K2

# The round function (F)
def fk(bits, subkey):
    # Expansion/Permutation (EP)
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    P4 = [2, 4, 3, 1]
    
    # Split into two halves
    left, right = bits[:4], bits[4:]
    
    # Apply expansion/permutation to right half
    expanded_right = permute(right, EP)
    
    # XOR with the subkey
    xor_result = xor(expanded_right, subkey)
    
    # Split into two halves for S-box substitution
    left_xor, right_xor = xor_result[:4], xor_result[4:]
    
    # S-box substitution
    sbox_output = s_box(left_xor, S0) + s_box(right_xor, S1)
    
    # Apply P4 permutation to the S-box output
    sbox_output = permute(sbox_output, P4)
    
    # XOR the output with the left half
    return xor(left, sbox_output) + right

# Simplified DES Encryption
def sdes_encrypt(plaintext, key):
    # Initial Permutation (IP)
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    
    # Generate subkeys K1 and K2
    K1, K2 = generate_keys(key)
    
    # Apply initial permutation
    bits = permute(plaintext, IP)
    
    # Apply the first round function using K1
    bits = fk(bits, K1)
    
    # Swap the two halves
    bits = bits[4:] + bits[:4]
    
    # Apply the second round function using K2
    bits = fk(bits, K2)
    
    # Apply the inverse initial permutation
    ciphertext = permute(bits, IP_inv)
    
    return ciphertext, K1, K2  # Return ciphertext along with keys

# Simplified DES Decryption (reverse process)
def sdes_decrypt(ciphertext, key):
    # Initial Permutation (IP)
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    
    # Generate subkeys K1 and K2
    K1, K2 = generate_keys(key)
    
    # Apply initial permutation
    bits = permute(ciphertext, IP)
    
    # Apply the first round function using K2 (reverse order of subkeys)
    bits = fk(bits, K2)
    
    # Swap the two halves
    bits = bits[4:] + bits[:4]
    
    # Apply the second round function using K1
    bits = fk(bits, K1)
    
    # Apply the inverse initial permutation
    plaintext = permute(bits, IP_inv)
    
    return plaintext

# Get user input for plaintext and key
plaintext = input("Enter 8-bit plaintext: ")
key = input("Enter 10-bit key: ")

# Validate inputs
if len(plaintext) != 8 or len(key) != 10 or not (set(plaintext) <= {'0', '1'}) or not (set(key) <= {'0', '1'}):
    print("Invalid input! Make sure the plaintext is 8 bits and the key is 10 bits, both binary.")
else:
    # Print user inputs
    print(f"\nPlaintext: {plaintext}")
    print(f"Key: {key}")

    # Encrypt the plaintext
    ciphertext, K1, K2 = sdes_encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    print(f"Subkey K1: {K1}")
    print(f"Subkey K2: {K2}")

    # Decrypt the ciphertext
    decrypted_text = sdes_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")
