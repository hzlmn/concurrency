import socketserver


class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        print(f"Connection from {self.request.getpeername()}")
        data = self.request.recv(1024)
        print(f"Received message {data}")
        self.request.sendall(data)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 9000
    server = socketserver.TCPServer((HOST, PORT), Handler)
    print(f"Started server on {HOST}:{PORT}")
    try:
        server.serve_forever()
    except Exception:
        server.shutdown()
