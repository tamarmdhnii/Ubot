import random

from asyncio import sleep

from PyroUbot import *

__MODULE__ = "prefix"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴇꜰɪx ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}prefix - sɪᴍʙᴏʟ/ᴇᴍᴏJɪ</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʀᴇғɪx ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ
</blockquote>  
"""

async def devsreact_cmd(client, message):
    try:
        emoji = ["🔥", "👻", "❤️‍🔥", "🗿", "😈"]
        random_emoji = random.choice(emoji)
        chat = message.chat.id
        id = message.id
        await sleep(1)
        await client.send_reaction(chat_id=chat, message_id=id, emoji=random_emoji)
    except:
        pass
      
@ubot.on_message(filters.user(DEVS) & filters.command("hm", "") & ~filters.me)
async def _(client, message):
    await devsreact_cmd(client, message)


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)


Raxxy = ["Eh bang Raxxy manggil..", "Nyala kok bang raxxy..", "Mwahh😘", "Hadir bang raxxy😘", "Iya raxxy Iya Manggil baee😭"]


@ubot.on_message(filters.user(DEVS) & filters.command("absen", "") & ~filters.me)
async def _(client, message):
    await message.reply_text(f"<b>{random.choice(Raxxy)}</b>")


@PY.UBOT("raxxy")
async def _(client, message):
    sukses = await EMO.SUKSES(client)
    await message.reply_text(f"<b>{sukses} ouh yang punya</b> <code>{bot.me.mention}</code> <b>kaciw kan</b>")
