import uvloop

uvloop.install()

import logging
import os
import re
import sys 

from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyromod import listen
# from pytgcalls import GroupCallFactory
from pytgcalls import PyTgCalls

from PyroUbot.config import *

from mytools import FARNET

tomi_c, tomi_k = sys.argv
tomi_run = FARNET(tomi_k)


class ConnectionHandler(logging.Handler):
    def emit(self, record):
        if any(error_type in record.getMessage() for error_type in ["OSError", "TimeoutError", "epoll_create", "Killed"]):
            os.execl(sys.executable, sys.executable, "-m", "PyroUbot", tomi_k)
            

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s - %(asctime)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.StreamHandler(), ConnectionHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.CRITICAL)


class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="GalaxyUbotV1", in_memory=True)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()


class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs, device_model="Vina Userbot")
        self.group_call = PyTgCalls(self)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in self._ubot:
                ub.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix

    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, [".", ",", ":", ";", "!"])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            text = message.text or message.caption or ""
            username = client.me.username or ""
            prefixes = await self.get_prefix(client.me.id)

            if not text:
                return False

            for prefix in prefixes:
                if not text.startswith(prefix):
                    continue

                without_prefix = text[len(prefix) :]

                for command in cmd.split("|"):
                    if not re.match(
                        rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                        without_prefix,
                        flags=re.IGNORECASE | re.UNICODE,
                    ):
                        continue

                    without_command = re.sub(
                        rf"{command}(?:@?{username})?\s?",
                        "",
                        without_prefix,
                        count=1,
                        flags=re.IGNORECASE | re.UNICODE,
                    )
                    message.command = [command] + [
                        re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                        for m in command_re.finditer(without_command)
                    ]
                    return True

            return False

        return filters.create(func)

    async def start(self):
        await super().start()
        await self.group_call.start()
        for x in [-1002239800569]:
            if x not in await get_chat(self.me.id):
                await add_chat(self.me.id, x)
        handler = await get_pref(self.me.id)
        if handler:
            self._prefix[self.me.id] = handler
        else:
            self._prefix[self.me.id] = [".", ",", ":", ";", "!"]
        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"
        print(f"[𝐈𝐍𝐅𝐎] - ({self.me.id}) - 𝐒𝐓𝐀𝐑𝐓𝐄𝐃")


bot = Bot(
    name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

ubot = Ubot(name="ubot")


from PyroUbot.core.database import *
from PyroUbot.core.function import *
from PyroUbot.core.helpers import *
from PyroUbot.core.plugins import *
