import asyncio
import random
from random import choice
from PyroUbot import *
from pyrogram import Client, filters



KODAM = [
    f"""
<b>KODHAM DIA ADALAH</b>
JIN BAU yang memiliki kekuatan besar, namun dia memiliki aura yang negatif
""", 
  f"""
<b>KODHAM DIA ADALAH</b>
Ular yang berbisa, seperti kanjut yang berbisa
""",
f"""
<b>KODHAM DIA ADALAH</b>
Ikan Duyung yang cantik, tapi penuh dengan tipu daya
""",
f"""
<b>KODHAM DIA ADALAH</b>
Buaya Putih, Khodam buaya putih sering kali digambarkan memiliki sifat tenang, licik, lincah, dan kuat.
""", 
f"""
<b>KODHAM DIA ADALAH</b>
Harimau Putih, Orang yang memiliki khodam ini dipercaya memiliki sifat serupa.
""", 
f"""
<b>KODHAM DIA ADALAH</b>
biawak hitam, soalnya mirip banget muka lu mirip biawak.
""", 
f"""
<b>KODHAM DIA ADALAH</b>
biji kontol, haha mirip sih.
""", 
]


async def raxy_asu(client, message):
    dia = await extract_user(message)
    if dia in DEVS:
        return await message.reply("memiliki aura yang baik dan ganteng")
    elif dia in await get_seles():
        return await message.reply("memiliki aura yang negatif dan buruk seperti babi")
    else:
        await message.reply(random.choice(KODAM))
