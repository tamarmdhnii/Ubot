from pyrogram import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from PyroUbot import *

__MODULE__ = "joinleave"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴊᴏɪɴ-ʟᴇᴀᴠᴇ 』</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}kickme</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}join</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴊᴏɪɴ ᴋᴇ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallgc</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallch</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ꜱᴇᴍᴜᴀ ᴄʜᴀɴɴᴇʟ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leave</code> [ᴜꜱᴇʀɴᴀᴍᴇɢᴄ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴜᴘ ᴍᴇʟᴀʟᴜɪ ᴜꜱᴇʀɴᴀᴍᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}leaveallmute</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ ɢʀᴏᴜᴘ ɢʀᴏᴜᴘ ʏᴀɴɢ ᴅɪ ᴍᴜᴛᴇ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}listmute</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʙᴇʀᴀᴘᴀ ɢʀᴜᴘ ʏᴀɴɢ ɴɢᴇᴍᴜᴛᴇ ᴀɴᴅᴀ
</blockquote>
"""


@PY.UBOT("join")
@PY.TOP_CMD
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    try:
        await xxnx.edit(f"<blockquote><emoji id=5206607081334906820>✅</emoji>ʙᴇʀʜᴀꜱɪʟ ʙᴇʀɢᴀʙᴜɴɢ ᴋᴇ ᴄʜᴀᴛ ɪᴅ `{Man}`</blockquote>")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply("ᴍᴇᴍᴘʀᴏꜱᴇꜱ...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit("<b>ᴘᴇʀɪɴᴛᴀʜ ɪɴɪ ᴅɪʟᴀʀᴀɴɢ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ ɪɴɪ</b>")
    try:
        await xxnx.edit_text(f"<blockquote><emoji id=5206607081334906820>✅</emoji>{client.me.first_name} ᴛᴇʟᴀʜ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ɢʀᴜᴘ ɪɴɪ, ʙʏᴇ!!</blockquote>")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def kickmeall(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴏᴜᴘ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"<blockquote><emoji id=5206607081334906820>✅</emoji><b>ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ɢʀᴏᴜᴘ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ɢʀᴏᴜᴘ</b></blockquote>"
    )

@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def kickmeallch(client: Client, message: Message):
    Man = await message.reply("ɢʟᴏʙᴀʟ ʟᴇᴀᴠᴇ ᴅᴀʀɪ ᴄʜᴀɴɴᴇʟ...")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"<blockquote><emoji id=5206607081334906820>✅</emoji><b>ʙᴇʀʜᴀꜱɪʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {done} ᴄʜᴀɴɴᴇʟ, ɢᴀɢᴀʟ ᴋᴇʟᴜᴀʀ ᴅᴀʀɪ {er} ᴄʜᴀɴɴᴇʟ</b></blockquote>"
    )


@PY.UBOT("leaveallmute")
async def _(client, message):
    done = 0
    Tk = await message.reply(f"<b><emoji id=6113844439292054570>⏳</emoji>sᴀʙᴀʀ ʏᴀᴋ ʟᴀɢɪ ɴɪɴɢɢᴀʟɪɴ ɢᴇᴄᴇ ᴛᴏʟᴏʟ ʙᴀᴘᴇʀᴀɴ</b>...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat)
                    done += 1
            except Exception:
                pass
    await Tk.edit(f"<blockquote><b><emoji id=5206607081334906820>✅</emoji>Succes Leave {done} Group Muted!!</b></blockquote>")


@PY.UBOT("listmute")
async def _(client, message):
    output = ""
    msg = await message.reply("Sedang memeriksa group")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            try:
                member = await client.get_chat_member(dialog.chat.id, client.me.id)
                if member.status == ChatMemberStatus.RESTRICTED:
                    chat = await client.get_chat(dialog.chat.id)
                    output += f"{chat.title} | [`{chat.id}`]\n"
            except Exception:
                output += f"{dialog.chat.id}\n"
    text = f"Daftar group yang membisukan anda adalah\n{output}" if output else "Daftar group yang membisukan anda kosong"
    await msg.edit(text)
