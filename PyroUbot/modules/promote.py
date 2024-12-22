import asyncio
from pyrogram import Client, filters
from pyrogram.types import ChatPrivileges
from pyrogram.errors import ChatAdminRequired, PeerIdInvalid, UsernameInvalid
from PyroUbot import *

__MODULE__ = "promote"
__HELP__ = """
 <blockquote><b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘʀᴏᴍᴏᴛᴇ ◗</b></blockquote>
 <blockquote>
  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}admin</code> [ɴᴀᴍᴀ/ᴛɪᴛʟᴇ]
  <code>ᴜɴᴛᴜᴋ ᴍᴇᴍᴘʀᴏᴍᴏsɪᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ sᴇʙᴀɢᴀɪ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ</code>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}fulladmin</code> [ɴᴀᴍᴀ/ᴛɪᴛʟᴇ]
  <code>ᴜɴᴛᴜᴋ ᴍᴇᴍᴘʀᴏᴍᴏsɪᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ sᴇʙᴀɪ ᴡᴀᴋɪʟ ᴘᴇᴍɪᴍᴘɪɴ ᴅɪ ɢʀᴏᴜᴘ</code>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unadmin</code>
  <code>ᴜɴᴛᴜᴋ ᴍᴇɴᴜʀᴜɴᴋᴀɴ ᴊᴀʙᴀᴛᴀɴ ᴀᴅᴍɪɴ ᴅɪ ɢʀᴏᴜᴘ</code>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}pin</code>  
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴʏᴇᴍᴀᴛᴋᴀɴ ᴘᴇsᴀɴ

 <b>❑ ᴄᴍᴅ:</b> <code>{0}unpin</code>  
 <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀsᴋᴀɴ sᴇᴍᴀᴛᴀɴ ᴘᴇsᴀɴ
 </blockquote>
"""

@PY.UBOT("fulladmin", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def full_promote(client: Client, message: Message):
    user_id = None
    custom_title = None

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        custom_title = ' '.join(message.command[1:]) if len(message.command) > 1 else None
    else:
        if len(message.command) > 1:
            user_input = message.command[1].strip()
            try:
                user = await client.get_users(user_input)
                user_id = user.id
            except (PeerIdInvalid, UsernameInvalid):
                return await message.reply("Username atau ID pengguna tidak valid.")
            
            custom_title = ' '.join(message.command[2:]) if len(message.command) > 2 else None
        else:
            return await message.reply(f"<blockquote>ʙᴇʀɪ ᴘᴇsᴀɴ ᴅᴇɴɢᴀɴ ᴄᴀʀᴀ ʀᴇᴘʟʏ ᴀᴛᴀᴜ ʙᴇʀɪ ᴜsᴇʀɴᴀᴍᴇ</blockquote>")

    Tm = await message.reply(f"ᴘʀᴏᴄᴇssɪɴɢ...")
    
    if not user_id:
        return await Tm.edit(f"ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.")

    try:
        member = await client.get_chat_member(message.chat.id, client.me.id)
        if not member.privileges:
            return await Tm.edit(f"sᴀʏᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ sɪɴɪ!")

        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        await client.set_administrator_title(
            message.chat.id, user_id, custom_title or "👑 Admin"
        )
        await Tm.edit(f"{umention} sᴜᴋsᴇs ᴍᴇɴᴊᴀᴅɪ ᴄᴇᴏ\nᴅᴇɴɢᴀɴ ᴛɪᴛʟᴇ: {custom_title or '👑 Admin'}")

    except ChatAdminRequired:
        await Tm.edit(f"sᴀʏᴀ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ ᴅɪ sɪɴɪ!")
    except (PeerIdInvalid, UsernameInvalid):
        await Tm.edit("ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ɪᴅ ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ.")
    except Exception as e:
        await Tm.edit(f"Terjadi kesalahan: {str(e)}")


@PY.UBOT("admin", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def promote(client: Client, message: Message):
    user_id = None
    custom_title = None

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        custom_title = ' '.join(message.command[1:]) if len(message.command) > 1 else None
    else:
        if len(message.command) > 1:
            user_input = message.command[1].strip()
            try:
                user = await client.get_users(user_input)
                user_id = user.id
            except (PeerIdInvalid, UsernameInvalid):
                return await message.reply("ᴜsᴇʀɴᴀᴍᴇ ᴀᴛᴀᴜ ɪᴅ ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
            
            custom_title = ' '.join(message.command[2:]) if len(message.command) > 2 else None
        else:
            return await message.reply(f"<blockquote>ʙᴇʀɪ ᴘᴇsᴀɴ ᴅᴇɴɢᴀɴ ᴄᴀʀᴀ ʀᴇᴘʟʏ ᴀᴛᴀᴜ ʙᴇʀɪ ᴜsᴇʀɴᴀᴍᴇ</blockquote>")

    Tm = await message.reply("Processing...")
    
    if not user_id:
        return await Tm.edit("Pengguna tidak ditemukan.")

    try:
        member = await client.get_chat_member(message.chat.id, client.me.id)
        if not member.privileges:
            return await Tm.edit("Saya bukan admin di grup ini!")

        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        await client.set_administrator_title(
            message.chat.id, user_id, custom_title or "Admin"
        )
        await Tm.edit(f"{umention} ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴊᴀᴅɪ ᴀᴅᴍɪɴ\nᴅᴇɴɢᴀɴ ᴛɪʟᴛʟᴇ {custom_title or 'Admin'}")

    except ChatAdminRequired:
        await Tm.edit("Saya bukan admin di grup ini!")
    except (PeerIdInvalid, UsernameInvalid):
        await Tm.edit("Username atau ID pengguna tidak valid.")
    except Exception as e:
        await Tm.edit(f"Terjadi kesalahan: {str(e)}")


@PY.UBOT("unadmin", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def demote(client: Client, message: Message):
    user_id = await extract_user(client, message)
    Tm = await message.reply("Processing...")
    if not user_id:
        return await Tm.edit("Pengguna tidak ditemukan")
    if user_id == client.me.id:
        return await Tm.edit("Tidak bisa demote diri sendiri.")

    try:
        await client.promote_chat_member(
            message.chat.id,
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        await asyncio.sleep(1)
        umention = (await client.get_users(user_id)).mention
        await Tm.edit(f"{umention} ʙᴇʀʜᴀsɪʟ ᴅɪ ᴜɴᴀᴅᴍɪɴ")
    except ChatAdminRequired:
        await Tm.edit("Saya bukan admin di grup ini!")
    except (PeerIdInvalid, UsernameInvalid):
        await Tm.edit("Username atau ID pengguna tidak valid.")


async def extract_user(client, message):
    """Extracts user id from command"""
    if message.reply_to_message and message.reply_to_message.from_user:
        return message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        user_input = message.command[1].strip()
        try:
            user = await client.get_users(user_input)
            return user.id
        except (PeerIdInvalid, UsernameInvalid):
            return None
    return None

@PY.UBOT("pin|unpin")
@PY.TOP_CMD
async def pin_message(client, message):
    if not message.reply_to_message:
        return await message.edit("Balas ke pesan untuk pin/unpin.")
    r = message.reply_to_message
    await message.edit("Processing...")
    if message.command[0][0] == "u":
        await r.unpin()
        return await message.edit(
            f"Unpinned [this]({r.link}) message.",
            disable_web_page_preview=True,
        )
    try:
        await r.pin(disable_notification=True)
        await message.edit(
            f"Pinned [this]({r.link}) message.",
            disable_web_page_preview=True,
        )
    except ChatAdminRequired:
        await message.edit("anda bukan admin di grup ini!")
        await message.delete()
