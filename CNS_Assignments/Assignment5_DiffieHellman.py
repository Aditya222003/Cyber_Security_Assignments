from random import randint

# Prime modulus and base
p = 23  # A prime number
g = 5   # A primitive root modulo p

def generate_private_key():
    return randint(1, p - 2)

def generate_public_key(private_key):
    return pow(g, private_key, p) # g^x mod p

def compute_shared_key(their_public, private_key):
    return pow(their_public, private_key, p) # s=B^a mod p

# Alice and Bob generate their private keys
alice_private = generate_private_key()
bob_private = generate_private_key()

# Alice and Bob compute their public keys
alice_public = generate_public_key(alice_private)
bob_public = generate_public_key(bob_private)

# --- MITM Attack Begins ---
# Eve generates her private key and computes public key
eve_private = generate_private_key()
eve_public = generate_public_key(eve_private)

# Eve intercepts public keys exchanged between Alice and Bob
alice_public_intercepted = eve_public  # Eve sends her public key to Alice
bob_public_intercepted = eve_public    # Eve sends her public key to Bob

# Alice computes the shared key using Eve's fake public key
alice_shared_with_eve = compute_shared_key(alice_public_intercepted, alice_private)

# Bob computes the shared key using Eve's fake public key
bob_shared_with_eve = compute_shared_key(bob_public_intercepted, bob_private)

# Eve computes the shared keys with Alice and Bob
eve_shared_with_alice = compute_shared_key(alice_public, eve_private)
eve_shared_with_bob = compute_shared_key(bob_public, eve_private)

# --- Output Results ---
print(f"Prime modulus (p): {p}")
print(f"Base (g): {g}")

print("\n--- Keys ---")
print(f"Alice's private key: {alice_private}")
print(f"Alice's public key: {alice_public}")
print(f"Bob's private key: {bob_private}")
print(f"Bob's public key: {bob_public}")
print(f"Eve's private key: {eve_private}")
print(f"Eve's public key: {eve_public}")

print("\n--- Shared Keys ---")
print(f"Alice's shared key with Eve: {alice_shared_with_eve}")
print(f"Eve's shared key with Alice: {eve_shared_with_alice}")
print(f"Bob's shared key with Eve: {bob_shared_with_eve}")
print(f"Eve's shared key with Bob: {eve_shared_with_bob}")

