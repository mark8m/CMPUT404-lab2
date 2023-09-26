import socket

BYTES_TO_READ = 4096

def get(host, port):
    request = b"GET \ HTTP/1.1\nHost: " + host.encode('utf-8') + b"\n\n"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Open up a socket here; AF_INET = use IPv4; SOCK_STREAM = use UDP
    s.connect((host, port)) # Connect to server
    s.send(request) # Send request to server
    s.shutdown(socket.SHUT_WR) # Tell server I'm done sending!
    result = s.recv(BYTES_TO_READ) # Keep reading incoming data
    while (len(result) > 0):
        print(result)
        result = s.recv(BYTES_TO_READ)
    
    s.close()

#get("www.google.com", 80)
get("localhost", 8080)