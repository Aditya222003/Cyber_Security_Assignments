import socket
from xor_crypto import xor_encrypt_decrypt, KEY

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    
    print("Server listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        encrypted_message = conn.recv(1024)
        if not encrypted_message:
            break
        
        # Display encrypted message
        print(f"Encrypted message: {encrypted_message}")
        
        # Decrypt the message
        message = xor_encrypt_decrypt(encrypted_message, KEY).decode()
        print(f"Decrypted message: {message}")
        
        # Prepare and send response
        response = f"Server received: {message}"
        encrypted_response = xor_encrypt_decrypt(response.encode(), KEY)
        
        # Display encrypted response
        print(f"Encrypted response: {encrypted_response}")
        
        conn.sendall(encrypted_response)

    conn.close()

if __name__ == "__main__":
    start_server()
