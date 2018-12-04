import os
import socket
from concurrent.futures import ThreadPoolExecutor

HOST = "127.0.0.1"
PORT = 9000

executor = ThreadPoolExecutor(max_workers=os.cpu_count())


def read(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Started listening connections on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            result = executor.submit(read, conn)

    executor.shutdown()

    print("Closing connection")
