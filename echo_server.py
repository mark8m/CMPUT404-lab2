import socket
from threading import Thread

BYTES_TO_READ = 4096
HOST = "127.0.0.1" # localhost IP
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ) # Wait for a request; when you get request, you (server) receieve a bytestring
            if not data:
                break
            print(data)
            conn.sendall(data)

# Start single threaded echo server
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # Initialize server socket
        s.bind((HOST, PORT)) # Bind to IP and port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Setting reuse bind address to true?
        s.listen() # Listen for incoming connections
        conn, addr = s.accept() # Accepting the client connection; conn = client socket, addr = IP and Port of client
        handle_connection(conn, addr) # Send client a response

# Start multi-threaded echo server
def start_threaded_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen(2) # Allow backlog of up to 2 connections ==> queue [waiting conn1, waiting conn2]
        while True:
            conn, addr = s.accept()
            thread = Thread(target=handle_connection, args=(conn, addr))
            thread.run()

start_server()
#start_threader_server()

