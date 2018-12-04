import asyncio


class TCPEchoServer(asyncio.Protocol):
    def connection_made(self, transport):
        print(f"Received connection from {transport.get_extra_info('peername')}")
        self.transport = transport

    def data_received(self, data):
        print(f"Received {data.decode()}")
        self.transport.write(data)
        self.transport.close()


async def main(loop):
    server = await loop.create_server(lambda: TCPEchoServer(),
                                      "127.0.0.1", 9000)

    print(f"Started server on ::9000")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
