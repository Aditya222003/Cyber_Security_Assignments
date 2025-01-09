import socket
from xor_crypto import xor_encrypt_decrypt, KEY

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    messages = ["Hello, Server!", "How are you?", "Goodbye!"]
    for message in messages:
        # Encrypt the message
        encrypted_message = xor_encrypt_decrypt(message.encode(), KEY)
        
        # Display encrypted message
        print(f"Message to send: {message}")
        print(f"Encrypted message: {encrypted_message}")

        # Send encrypted message
        client_socket.sendall(encrypted_message)

        # Receive and decrypt response
        encrypted_response = client_socket.recv(1024)
        response = xor_encrypt_decrypt(encrypted_response, KEY).decode()
        
        # Display decrypted response
        print(f"Encrypted response from server: {encrypted_response}")
        print(f"Decrypted response: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
