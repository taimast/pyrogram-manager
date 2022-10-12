from pydantic import BaseModel
from pyrogram.handlers.handler import Handler

from patched import Client


class BaseDispatcher(BaseModel):
    client: Client
    handlers: list[Handler] = []

    class Config:
        arbitrary_types_allowed = True
        copy_on_model_validation = 'none'

    async def __aenter__(self):
        await self.start()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.stop()

    async def start(self):
        for handler in self.handlers:
            self.client.add_handler(handler)
        await self.client.start()

    async def stop(self):
        await self.client.__aexit__()

    def add_handler(self, handler: Handler):
        self.handlers.append(handler)
