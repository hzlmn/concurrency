import socket

body = b"""
GET /index.html HTTP/1.0
"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    ip = socket.gethostbyname("www.python.org")
    sock.connect((ip, 443))
    print(f"Established connection to www.python.org")
    sock.sendall(b"GET /index.html HTTP/1.0\r\n\r\n")
    chunks = bytearray()
    while True:
        data = sock.recv(1024)
        print(f"Received chunk {data}")
        if not data:
            break
        chunks += data
    print(f"Received response {chunks}")
