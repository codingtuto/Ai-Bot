# Copyright New-dev0 & Coding Team 2022

import logging
from .configs import Var
from telethon import TelegramClient
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("BingBot")

if not Var.BOT_TOKEN:
    LOG.error("'BOT_TOKEN' non trouvée!\nQuitte...")
    exit()

client = TelegramClient(None, api_id=Var.API_ID, api_hash=Var.API_HASH)
client.start(bot_token=Var.BOT_TOKEN)

from .db import JSONDB, save_json

sched = AsyncIOScheduler()
sched.add_job(save_json, "interval", minutes=Var.DB_UPDATE_DELAY)
sched.start()
LOG.info(f"Auto enregistrement de la base de données activée chaque {Var.DB_UPDATE_DELAY} MINUTES.")
