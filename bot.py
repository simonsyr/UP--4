import os
import aiohttp
import logging
import asyncio
from aiohttp import web
from plugins.config import Config
from pyrogram import Client as Ntbot
from pyrogram import filters
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

async def handle_request(request):
    return web.Response(text="𝗛𝗲𝗹𝗹𝗼, 𝗪𝗲𝗯 𝗦𝗲𝗿𝘃𝗲𝗿")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_request)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8080)
    print("Starting web server on 0.0.0.0:8080")
    await site.start()

if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(root="plugins")
    Ntbot = Ntbot(
        "@URL_UPLOAD_TG_BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_web_server())
    loop.run_until_complete(Ntbot.run())
