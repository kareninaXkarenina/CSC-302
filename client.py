# Name; TERHILE-SENDE S. KAREN
# Mat. No.; VUG/CSC/22/8233

import socket

HOST = "127.0.0.1"  # Match the server's IP
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print("Connected to the server. Type 'exit' to disconnect.")

while True:
    # Send a message to the server
    message = input("Client: ")
    client_socket.sendall(message.encode("utf-8"))

    if message.lower() == "exit":
        break  # Close connection if client sends "exit"

    # Receive and print the server's response
    response = client_socket.recv(1024).decode("utf-8")
    print(f"Server: {response}")

client_socket.close()
