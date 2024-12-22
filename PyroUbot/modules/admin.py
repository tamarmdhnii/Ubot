import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from PyroUbot import *


__MODULE__ = "admin"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴍɪɴ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}kick</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙʟᴏᴋɪʀ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}mute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unmute</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙʟᴏᴋɪʀᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ 

  <b>❑ ᴄᴍᴅ:</b> <code>{0}unban</code> [ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟᴇᴘᴀs ᴘᴇᴍʙɪsᴜᴀɴ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}staff</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴅᴀꜰᴛᴀʀ sᴇᴍᴜᴀ ᴀᴅᴍɪɴ ᴅɪᴅᴀʟᴀᴍ ɢʀᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ
</blockquote>
"""



@PY.UBOT("kick", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_kick(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇɴᴇɴᴅᴀɴɢ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴅɪᴛᴇɴᴅᴀɴɢ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("ban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_ban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal}ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴀɴɴᴇᴅ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴅɪʙᴀɴɴᴇᴅ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("mute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_mute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"{gagal} ᴀᴋᴜ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴅɪʀɪᴋᴜ sᴇɴᴅɪʀɪ, ᴀᴋᴜ ʙɪsᴀ ᴘᴇʀɢɪ ᴊɪᴋᴀ ᴋᴀᴍᴜ ᴍᴀᴜ.")
    if user_id == OWNER_ID:
        return await message.reply_text(f"{gagal} ᴀɴᴅᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪɴɪ")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙɪsᴜᴋᴀɴ ᴀᴅᴍɪɴ, ᴀɴᴅᴀ ᴛᴀʜᴜ ᴀᴛᴜʀᴀɴɴʏᴀ, sᴀʏᴀ ᴊᴜɢᴀ.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} ᴍᴇᴍʙɪsᴜᴋᴀɴ:</b> {mention}\n<b>{admin} ᴀᴅᴍɪɴ:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} ᴀʟᴀsᴀɴ:</b> {reason}"
    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unmute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unmute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>{sukses} {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴄʜᴀᴛ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} sᴀʏᴀ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴᴇᴍᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ɪᴛᴜ.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<b>{sukses} {mention} sᴜᴅᴀʜ ʙɪsᴀ ᴊᴏɪɴ ʟᴀɢɪ</b>")
    except Exception as error:
        await message.reply(error)


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
      

@PY.UBOT("staff")
@PY.TOP_CMD
async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    bot_admins = []

    async for x in message.chat.get_members():
        mention = f"<a href=tg://user?id={x.user.id}>{x.user.first_name} {x.user.last_name or ''}</a>"
        custom_title = x.custom_title or "Admin"  # Default title if custom title is not set

        # Check if the user is a bot and an admin
        if x.user.is_bot and x.status.value == "administrator":
            bot_admins.append(f" ┣ {mention} - {custom_title}")
        else:
            # Check if the user is an administrator with promotion privileges
            if x.status.value == "administrator" and x.privileges and x.privileges.can_promote_members:
                co_founder.append(f" ┣ {mention} - {custom_title}")
            # Check if the user is an administrator without promotion privileges
            elif x.status.value == "administrator":
                admin.append(f" ┣ {mention} - {custom_title}")
            # Check if the user is the owner
            elif x.status.value == "owner":
                creator.append(f" ┗ {mention} - {custom_title}")

    result = f"<b>sᴛᴀꜰꜰ ɢʀᴜᴘ\n{chat_title}\n\n"

    if creator:
        result += f"👑 ᴏᴡɴᴇʀ:\n{creator[0]}\n\n"
    if co_founder:
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result += f"👮 ᴄᴏ-ꜰᴏᴜɴᴅᴇʀ:\n" + "\n".join(co_founder) + "\n\n"
    if admin:
        adm = admin[-1].replace(" ┣", " ┗")
        admin.pop(-1)
        admin.append(adm)
        result += f"👮 ᴀᴅᴍɪɴ:\n" + "\n".join(admin) + "\n\n"
    if bot_admins:
        bot_adm = bot_admins[-1].replace(" ┣", " ┗")
        bot_admins.pop(-1)
        bot_admins.append(bot_adm)
        result += f"🤖 ʙᴏᴛ ᴀᴅᴍɪɴ:\n" + "\n".join(bot_admins)

    result += "</b>"

    await message.reply(result)
