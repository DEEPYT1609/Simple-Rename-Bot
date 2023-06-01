from pyrogram import Client
from config import *
import os
import logging
import asyncio
from aiohttp import web
from main.web_support import web_server
from main.web_support import ping_server

logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client):
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)

    def __init__(self):
        super().__init__(
            name="simple-renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=100,
            plugins={"root": "main"},
            sleep_threshold=10,
        )
    async def start(self):
        await super().start()
        me = await self.get_me()
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        PORT = "8080"
        await web.TCPSite(app, bind_address, PORT).start()
        asyncio.create_task(ping_server())
        logging.info("Web server started")
        logging.info("Pinging server")
        print(f"{me.first_name} | @{me.username} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳...⚡️")
       
    async def stop(self, *args):
       await super().stop()      
       print("Bot Restarting........")


bot = Bot()
bot.run()
