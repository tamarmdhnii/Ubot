import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait

from PyroUbot import *
from PyroUbot.config import *

__MODULE__ = "spam gcast"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜱᴘᴀᴍ ɢᴄᴀꜱᴛ 』</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}spamg</code> (ᴊᴜᴍʟᴀʜ) - ᴛᴇxᴛ/ʀᴇᴘʟʏ_ᴍsɢ
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴀᴋᴜᴋᴀɴ sᴘᴀᴍ ɢᴄᴀsᴛ sᴇᴄᴀʀᴀ ʙᴇʀsᴀᴍᴀᴀɴ sᴇᴄᴀʀᴀ ʀᴇᴀʟ-ᴛɪᴍᴇ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopspamg</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀʜᴇɴᴛɪᴋᴀɴ sᴘᴀᴍ ɢᴄᴀsᴛ ʏᴀɴɢ sᴇᴅᴀɴɢ ʙᴇʀʟᴀɴɢsᴜɴɢ
  

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}setdelay</code> (ᴄᴏᴜɴᴛ) 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴅᴇʟᴀʏ sᴇᴛɪᴀᴘ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪ ᴋɪʀɪᴍ

  <b>NB:</b> ᴊᴀɴɢᴀɴ ᴛᴇʀʟᴀʟᴜ sᴇʀɪɴɢ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴍᴏᴅᴜʟᴇ ɪɴɪ
</blockquote>  
"""

total_spam_gcast = {}
spam_tasks = {}

def extract_type_and_msg(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None
    msg_type = args[1]
    msg = message.reply_to_message if message.reply_to_message else args[2] if len(args) > 2 else None
    return msg_type, msg

async def SpamGcast(client, message, send):
    blacklist = await get_chat(client.me.id)
    total_spam_gcast[client.me.id] = 0

    async def send_message(target_chat):
        await asyncio.sleep(0.8)
        if message.reply_to_message:
            await send.copy(target_chat)
        else:
            await client.send_message(target_chat, send)

    async def handle_flood_wait(exception, target_chat):
        await asyncio.sleep(exception.value)
        await send_message(target_chat)

    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            if dialog.chat.id not in blacklist and dialog.chat.id not in BLACKLIST_CHAT:
                try:
                    await send_message(dialog.chat.id)
                    total_spam_gcast[client.me.id] += 1
                except FloodWait as e:
                    await handle_flood_wait(e, dialog.chat.id)
                    total_spam_gcast[client.me.id] += 1
                except Exception as e:
                    print(f"Exception during spam: {e}")
                  

@PY.UBOT("stopspamg")
@PY.TOP_CMD
async def stop_spam(client, message):
    spam_id = message.from_user.id
    if spam_id in spam_tasks:
        spam_task = spam_tasks[spam_id]
        spam_task.cancel()
        del spam_tasks[spam_id]
        
        # Edit the message indicating that the spam has been stopped
        if hasattr(spam_task, 'reply_message'):
            await spam_task.reply_message.edit(f"<b><emoji id=6113647841459047673>✅</emoji> Spam Gcast berhasil dihentikan.</b>")
        
        await message.reply(f"<b><emoji id=6113647841459047673>✅</emoji> Spam telah dihentikan.</b>")
    else:
        await message.reply(f"<b><emoji id=6278161560095426411>❌</emoji> Tidak ada spam yang sedang berjalan.</b>")


@PY.UBOT("spamg")
@PY.TOP_CMD
async def spamg(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    gcast_done = await get_vars(client.me.id, "GCAST_DONE") or "6289678459065077018"
    send_done = await get_vars(client.me.id, "SEND_DONE") or "6296577138615125756"
    
    r = await message.reply(f"<b><emoji id={proses}>⏳</emoji> Sedang memproses....</b>")
    
    count, msg = extract_type_and_msg(message)

    if not msg:
        return await r.edit(f"<b><emoji id={gagal}>❎</emoji> <code>{message.text.split()[0]}</code> Jumlah - teks/reply_msg</b>")

    try:
        count = int(count)
    except ValueError:
        return await r.edit(f"<b><emoji id={gagal}>❎</emoji> <code>{message.text.split()[0]}</code> Jumlah harus berupa angka</b>")

    async def run_spam():
        total_spam_gcast[client.me.id] = 0  # Initialize the key before starting tasks
        spam_gcast_tasks = [SpamGcast(client, message, msg) for _ in range(count)]
        for task in spam_gcast_tasks:
            await task  
        del spam_tasks[client.me.id]

    spam_task = asyncio.create_task(run_spam())
    spam_task.reply_message = r  
    spam_tasks[client.me.id] = spam_task

    await spam_task

    total_spam_count = total_spam_gcast.get(client.me.id, 0)
    
    await r.edit(f"<b>Spam Gcast telah selesai dilakukan <emoji id={gcast_done}>⚠️</emoji>\n<b><emoji id={sukses}>✅</emoji> Berhasil terkirim dalam <code>{int(total_spam_count / count)}</code> grup\n<emoji id={send_done}>⛔️</emoji> Dalam putaran <code>{count}</code> kali</b>")
     
    del total_spam_gcast[client.me.id]


@PY.UBOT("setdelay")
@PY.TOP_CMD
async def set_delay(client, message):
    r = await message.reply("<b>Tunggu sebentar....</b>")
    count, msg = extract_type_and_msg(message)

    if count is None:
        return await r.edit(f"<b><emoji id={gagal}>❎</emoji> <code>{message.text.split()[0]}</code> Jumlah tidak boleh kosong</b>")

    if count.lower() == "none":
        await set_vars(client.me.id, "SPAM", 0)
        return await r.edit("<b>Spam delay berhasil di setting</b>")

    try:
        count = int(count)
    except ValueError:
        return await r.edit(f"<b><emoji id={gagal}>❎</emoji> <code>{message.text.split()[0]}</code> Jumlah harus berupa angka</b>")

    if count <= 0:
        return await r.edit(f"<b><code>{message.text.split()[0]}</code> Jumlah harus lebih dari 0</b>")

    await set_vars(client.me.id, "SPAM", count)
    return await r.edit("<b>Spam delay berhasil di setting</b>")
