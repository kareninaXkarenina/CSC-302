# Name; TERHILE-SENDE S. KAREN
# Mat. No.; VUG/CSC/22/8233

import socket

HOST = "127.0.0.1"  # Change this to "0.0.0.0" for external connections
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}...")

client_socket, client_address = server_socket.accept()  # Accept a client connection
print(f"Connected by {client_address}")

while True:
    # Receive data from client
    data = client_socket.recv(1024).decode("utf-8")  # Receive up to 1024 bytes
    if not data or data.lower() == "exit":
        print("Client disconnected.")
        break  # Exit loop if client sends "exit"

    print(f"Client: {data}")  # Print received message

    # Send a response
    response = input("Server: ")  # Get server's response from input
    client_socket.sendall(response.encode("utf-8"))  # Send response to client

client_socket.close()  # Close connection
server_socket.close()
