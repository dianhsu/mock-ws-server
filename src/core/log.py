import sys
from loguru import logger

logger.configure(
    handlers=[
        dict(sink=sys.stderr, format="[{level}][{time}][{file}:{line}]: {message}", level="DEBUG"),
    ]
)