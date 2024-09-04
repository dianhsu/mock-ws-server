
from .log import logger
async def greet(websocket, data):
    logger.debug(data)