
from PyroUbot import *

__MODULE__ = "filters"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ғɪʟᴛᴇʀs 』</b></blockquote>
  <blockquote>
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}filter</code>ᴏɴ/ᴏғғ 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ғɪʟᴛᴇʀs
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}addfilter</code> ɴᴀᴍᴀ - ʀᴇᴘʟʏ_ᴍsɢ
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ғɪʟᴛᴇʀs ᴋᴇ ᴅᴀᴛᴀʙᴀsᴇ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}delfilter</code> ɴᴀᴍᴀ ғɪʟᴛᴇʀs
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ғɪʟᴛᴇʀs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}filters</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ sᴇᴍᴜᴀ ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs
  </blockquote>
"""


def extract_type_and_msg(message):
    args = message.text.split(None, 2)

    if len(args) < 2:
        return None, None

    type = args[1]
    msg = message.reply_to_message if message.reply_to_message else args[2] if len(args) > 2 else None

    return type, msg


@PY.NO_CMD_UBOT("FILTER_MSG")
async def filter_message(client, message):
    try:
        chat_logs = await get_vars(client.me.id, "ID_LOGS")
        all_filters = await all_vars(client.me.id, "FILTERS") or {}
        
        for key, value in all_filters.items():
            if key == message.text.split()[0]:
                msg = await client.get_messages(int(chat_logs), int(value))
                return await msg.copy(message.chat.id, reply_to_message_id=message.id)
    except Exception:
        pass




@PY.UBOT("filter")
@PY.TOP_CMD
async def _(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    txt = await message.reply(f"{proses} Sedang memproses")
    arg = get_arg(message)

    if not arg or arg.lower() not in ["off", "on"]:
        return await txt.edit(f"{gagal} harap baca menu bantuan terlebih dahulu")

    type = True if arg.lower() == "on" else False
    await set_vars(client.me.id, "FILTER_ON_OFF", type)
    return await txt.edit(f"{sukses} filters berhasil di settings ke {type}")


@PY.UBOT("addfilter")
@PY.TOP_CMD
async def _(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    txt = await message.reply(f"{proses} Sedang memproses")
    type, reply = extract_type_and_msg(message)

    if not type and message.reply_to_message:
        return await txt.edit(f"{gagal} harap balas pesan dan kasih nama")

    logs = await get_vars(client.me.id, "ID_LOGS")
    if bool(logs):
        try:
            msg = await reply.copy(int(logs))
            await set_vars(client.me.id, type, msg.id, "FILTERS")
            await txt.edit(f"{sukses} filters {type} berhasil di simpan")
        except Exception as error:
            await txt.edit(error)
    else:
        return await txt.edit(f"{gagal} Tidak bisa membuat filters baru")


@PY.UBOT("delfilter")
@PY.TOP_CMD
async def _(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    txt = await message.reply(f"{proses} tunggu sebentar")
    arg = get_arg(message)

    if not arg:
        return await txt.edit(f"{gagal} {message.text.split()[0]} nama filter")

    logs = await get_vars(client.me.id, "ID_LOGS")
    all = await all_vars(client.me.id, "FILTERS")

    if arg not in all:
        return await txt.edit(f"{gagal} filter {arg} tidak ditemukan")

    await remove_vars(client.me.id, arg, "FILTERS")
    await client.delete_messages(logs, all[arg])
    return await txt.edit(f"{sukses} filter {arg} berhasil dihapus")


@PY.UBOT("filters")
@PY.TOP_CMD
async def _(client, message):
    vars = await all_vars(client.me.id, "FILTERS")
    if vars:
        alasan = await EMO.ALASAN(client)
        msg = f"<b>{alasan} ᴅᴀғᴛᴀʀ ғɪʟᴛᴇʀs</b>\n"
        for x in vars.keys():
            msg += f"<b> ├ <code>{x}</code></b>\n"
        msg += f"<b> ╰ ᴛᴏᴛᴀʟ ғɪʟᴛᴇʀs: {len(vars)}</b>"
    else:
        gagal = await EMO.GAGAL(client)
        msg = f"<b>{gagal} ᴛɪᴅᴀᴋ ᴀᴅᴀ ғɪʟᴛᴇʀs ʏᴀɴɢ ᴛᴇʀsɪᴍᴘᴀɴ</b>"

    return await message.reply(msg, quote=True)
