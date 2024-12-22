from asyncio import sleep
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

# from pytgcalls import GroupCallFactory


from PyroUbot import *

__MODULE__ = "vctools"
__HELP__ = """
<blockquote>
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴠᴄᴛᴏᴏʟs 』</b>

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}startvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> uɴᴛᴜᴋ ᴍᴇᴍᴜʟᴀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ 

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}stopvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋʜɪʀɪ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}joinvc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ʙᴇʀɢᴀʙᴜɴɢ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}leavevc</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɪɴɢɢᴀʟᴋᴀɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ɢʀᴜᴘ

  <b>❑ ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}listeners</code>
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> buat melihat siapa saja yang berada di obrolan suara 
</blockquote>
"""


@PY.UBOT("startvc")
@PY.TOP_CMD
async def _(client, message):
    await opengc(client, message)


@PY.UBOT("stopvc")
@PY.TOP_CMD
async def _(client, message):
    await end_vc_(client, message)


async def get_group_call(client: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await client.send(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False

@PY.UBOT("joinvc")
@PY.TOP_CMD
@ubot.on_message(filters.user(DEVS) & filters.command("cjoinvc", ".") & ~filters.me)
async def joinvc(client, message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6181594215491832601"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.group_call.play(chat_id)
        await client.group_call.mute_stream(chat_id)
    except Exception as e:
        return await msg.edit(f"<emoji id={gagal}>❌</emoji>ERROR: {e}")
    return await msg.edit(
        f"<blockquote><b><emoji id={sukses}>✅</emoji>ʙᴇʀʜᴀsɪʟ ɴᴀɪᴋ ᴋᴇ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>\n<b><emoji id=6113647841459047673>✅</emoji><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : **{bot.me.mention}</b></blockquote>"
    )
    # await sleep(1)
    # await client.group_call.set_is_mute(True)

@PY.UBOT("leavevc")
@PY.TOP_CMD
@ubot.on_message(filters.user(DEVS) & filters.command("cleavevc", ".") & ~filters.me)
async def leavevc(client: Client, message: Message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6181594215491832601"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.group_call.leave_call(chat_id)
    except Exception as e:
        return await msg.edit(
            f"<emoji id={gagal}>❌</emoji>ERROR: {e}"
        )
    return await msg.edit(
        f"<blockquote><b><emoji id={sukses}>✅</emoji>ʙᴇʀʜᴀsɪʟ ᴛᴜʀᴜɴ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ</b>\n<b><emoji id=6113647841459047673>✅</emoji><b>ᴘᴏᴡᴇʀᴇᴅ ʙʏ : {bot.me.mention}</b></b></blockquote>"
    )


async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6246660083808210143"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<blockquote><b><emoji id={sukses}>✅</emoji> ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴛᴇʟᴀʜ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ</b></blockquote>\n<blockquote><emoji id={alasan}>⚠️</emoji> <b>ɢʀᴏᴜᴘ ᴄʜᴀᴛ</b> : {message.chat.title}</blockquote>"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


async def end_vc_(client: Client, message: Message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6247033234861853924"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    message.chat.id
    if not (group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await ky.edit(f"<blockquote><emoji id={gagal}>❎</emoji> <b>ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ʙᴇʀʜᴀsɪʟ ᴅɪ ᴍᴀᴛɪᴋᴀɴ</b></blockquote>\n<blockquote><emoji id={alasan}>⚠️</emoji> <b>ɢʀᴏᴜᴘ ᴄʜᴀᴛ</b> : {message.chat.title}</blockquote>")


@PY.UBOT("listeners")
@PY.TOP_CMD
async def lisen_os(client, message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113891550788324241"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6181594215491832601"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ....</b>")

    chat = message.command[1] if len(message.command) > 1 else message.chat.id

    try:
        if isinstance(chat, int):
            chat_id = chat
        else:
            chat_info = await client.get_chat(chat)
            chat_id = chat_info.id

        try:
            info = await client.get_chat(chat_id)
            title = info.title if info.title else f"{chat_id}"
        except:
            title = f"{chat_id}"

        try:
            total_org = await client.group_call.get_participants(chat_id)
            total_men = []
            for bocah in total_org:
                user_id = bocah.user_id
                try:
                    user = await client.get_users(user_id)
                    mention = user.mention
                    status = "Diam" if bocah.muted else "Berbicara"
                    total_men.append(f"{mention} status {status}")
                except Exception as e:
                    print(f"{e}")
                    total_men.append(f"{user_id} status Unknown")

            total_orang = len(total_org)
            if total_orang == 0:
                return await msg.edit(
                    f"<blockquote><blockquote><emoji id={gagal}>❎</emoji><b>Tidak ada orang di Obrolan suara.</b></blockquote>"
                )

            men_teks = "\n".join(
                [
                    (f"┣ {mention}" if i < total_orang - 1 else f"┖ {mention}")
                    for i, mention in enumerate(total_men)
                ]
            )

            text = f"""
<emoji id={sukses}>✅</emoji> <b>Data Pendengar Obrolan Suara:</b>
<emoji id={alasan}>💫</emoji> <b>Chat: <code>{title}</code>.</b>
<emoji id={alasan}>💫</emoji> <b>Total: <code>{total_orang}</code> orang.</b>

❒ Peserta:
{men_teks}
"""
            return await msg.edit(f"<blockquote>{text}</blockquote>")

        except Exception as e:
            await msg.edit(
                f"<blockquote>emoji id={gagal}>❎</emoji><b>Error:</b>\n<code>{e}</code></blockquote>"
            )
    except Exception as e:
        await msg.edit(
            f"<blockquote>emoji id={gagal}>❎</emoji><b>Error:</b>\n<code>{e}</code></blockquote>"
        )
