import os
import asyncio
from websockets.asyncio.server import serve
from dotenv import load_dotenv
import json
from core.route import routers
from core.log import logger
load_dotenv()

HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT", 4001)) 

async def dispatch(websocket, request: dict[str, str], route: dict[str, callable]):
    if "action" not in request:
        raise KeyError(f"Invalid request: {request}")
    if request["action"] not in route:
        raise KeyError(f"Invalid action: {request['action']}")
    if "data" not in request:
        request["data"] = {}
    await route[request["action"]](websocket, request["data"])

async def handler(websocket):
    try:
        async for raw_req in websocket:
            request = json.loads(raw_req)
            await dispatch(websocket, request, routers)
    finally:
        pass

async def server():
    async with serve(handler, HOST, PORT):
        logger.debug(f"Start listening on {HOST}:{PORT}")
        await asyncio.get_running_loop().create_future()  # run forever

if __name__ == "__main__":
    asyncio.run(server())