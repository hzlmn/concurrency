import asyncio


async def handle_echo(reader, writer):
    data = await reader.read(1024)
    message = data.decode()
    print(f"Received message {message}")

    writer.write(data)
    await writer.drain()

    writer.close()


async def main():
    server = await asyncio.start_server(handle_echo, "127.0.0.1", 9000)
    print(f"Started server on ::9000")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
