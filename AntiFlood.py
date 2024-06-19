from cachetools import TTLCache
from typing import Callable, Awaitable, Dict, Any
from aiogram import BaseMiddleware
from aiogram.types import Message


class AntiFloodMiddleware(BaseMiddleware):
    def __init__(self, time_limit: int = 0.3):
        self.limit = TTLCache(maxsize=10000, ttl=time_limit)

    async def __call__(
                self,
                handler: Callable[[Message, Dict[str, any]],
                Awaitable[Any]], event: Message,
                data: Dict[str, Any]
        ):
            if event.chat.id in self.limit:
                return
            else:
                self.limit[event.chat.id] = None
            return await handler(event, data)
