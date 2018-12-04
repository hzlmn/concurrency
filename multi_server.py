import selectors
import socket
import time

sel = selectors.DefaultSelector()


def accept(sock, mask):
    conn, addr = sock.accept()
    print(f"accepted {conn} from {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1024)

    print(f"Received {data} from {conn}")

    conn.send(data)
    sel.unregister(conn)
    conn.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 9000))

print("Started server on 127.0.0.1:9000")

sock.listen()
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)


while True:
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(key.fileobj, mask)
