import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensaje recibido: {message}")

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):  # Cambiado de "localhost" a "0.0.0.0"
        print("Servidor WebSocket iniciado en ws://0.0.0.0:8765/")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
