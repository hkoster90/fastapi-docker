from hypercorn.config import Config
import asyncio
import uvloop
from hypercorn.asyncio import serve
from app.app import app

config = Config()
config.bind = ["0.0.0.0:8080"]

uvloop.install()
asyncio.run(serve(app, config))