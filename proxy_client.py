import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET \ HTTP/1.1\nHost: www.google.com\n\n"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port)) # Connect to server
        s.send(request) # Send request to server
        s.shutdown(socket.SHUT_WR) # Tell server I'm done sending!
        chunk = s.recv(BYTES_TO_READ) # Keep reading incoming data
        result = b'' + chunk # Convert received data from server into bytestring for client socket
        
        while (len(chunk) > 0):
            result = s.recv(BYTES_TO_READ)
            result += chunk        
        s.close()
        return result

print(get("127.0.0.1", 8080))