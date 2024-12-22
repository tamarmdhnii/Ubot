import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "profil"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏꜰɪʟ 』</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}setbio</code> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴀɴᴅᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}setname</ᴄᴏᴅᴇ> [ᴛᴇxᴛ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴀɴᴅᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}setpp</ᴄᴏᴅᴇ> [Reply Media]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> Untuk mengubah foto profile anda

  <b>❑ ᴄᴍᴅ:</b> <code>{0}block</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unblock</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ ᴘᴇɴɢɢᴜɴᴀ
</blockquote>  
"""

@PY.UBOT("unblock")
@PY.TOP_CMD
async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴀᴛᴀᴜ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit("ᴏᴋ ᴅᴏɴᴇ.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙᴇʙᴀꜱᴋᴀɴ</b> {umention}")

@PY.UBOT("block")
@PY.TOP_CMD
async def block_user_func(client, message):
    user_id = await extract_user(message)
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if not user_id:
        return await tex.edit(f"ʙᴇʀɪᴋᴀɴ ɴᴀᴍᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜɴᴛᴜᴋ ᴅɪʙʟᴏᴋɪʀ.")
    if user_id == client.me.id:
        return await tex.edit("ᴏᴋ ᴅᴏɴᴇ.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴅɪʙʟᴏᴋɪʀ</b> {umention}")

@PY.UBOT("setname")
@PY.TOP_CMD
async def setname(client: Client, message: Message):
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ɴᴀᴍᴀ ᴍᴇɴᴊᴀᴅɪ</b> <code>{name}</code>"
            )
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ɴᴀᴍᴀ ᴀɴᴅᴀ.")

@PY.UBOT("setbio")
@PY.TOP_CMD
async def set_bio(client: Client, message: Message):
    tex = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<b>ʙᴇʀʜᴀꜱɪʟ ᴍᴇɴɢᴜʙᴀʜ ʙɪᴏ ᴍᴇɴᴊᴀᴅɪ</b> <code>{bio}</code>")
        except Exception as e:
            await tex.edit(f"<b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit("ʙᴇʀɪᴋᴀɴ ᴛᴇᴋꜱ ᴜɴᴛᴜᴋ ᴅɪᴛᴇᴛᴀᴘᴋᴀɴ ꜱᴇʙᴀɢᴀɪ ʙɪᴏ.")

@PY.UBOT("setpp")
@PY.TOP_CMD
async def set_pfp(client, message):
    po = "storage/TM_BLACK.png"
    replied = message.reply_to_message
    pros = await message.reply(
        "<blockquote><b>Proses mengubah foto profil ..</b></blockquote>"
    )
    if (
        replied
        and replied.media
        and (
            replied.photo
            or (replied.document and "image" in replied.document.mime_type)
        )
    ):
        prop = await client.download_media(message=replied, file_name=po)
        await client.set_profile_photo(photo=prop)
        await client.send_photo(
            message.chat.id,
            prop,
            caption="<blockquote><b>Berhasil mengubah Foto Profil anda.</b></blockquote>",
        )
        if os.path.exists(prop):
            os.remove(prop)
        return await pros.delete()
    else:
        return await pros.edit(
            "<blockquote><b>Balas foto/gambar, atau dokumen yang berupa foto/gambar untuk dijadikan Foto Profil.</b></blockquote>"
            )
