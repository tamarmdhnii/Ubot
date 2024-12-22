from datetime import datetime

import pytz
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent

from PyroUbot import *

__MODULE__ = "absen"
__HELP__ = """
<blockquote><b>『 bantuan untuk absen 』</b></blockquote>

  <blockquote><b>• perintah:</b> <code>{0}absen</code>
  <b>• penjelasan:</b> untuk membuat list absen kamu.

  <b>• perintah:</b> <code>{0}delabsen</code>
  <b>• penjelasan:</b> untuk menghapus list absen kamu.</blockquote>
"""

hadir_list = {}


def get_hadir_list(group_id):
    if group_id in hadir_list:
        return "\n".join([f"👤 {user['mention']} - {user['jam']}" for user in hadir_list[group_id]])
    return ""


@PY.UBOT("absen")
@PY.GROUP
@PY.TOP_CMD
async def absen_command(c, m):
    try:
        x = await c.get_inline_bot_results(bot.me.username, f"absen_hadir {m.chat.id}")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await m.reply(error)


@PY.UBOT("delabsen")
@PY.GROUP
@PY.TOP_CMD
async def clear_absen_command(c, m):
    group_id = m.chat.id
    if group_id in hadir_list:
        hadir_list[group_id].clear()

    await m.reply("Semua absen berhasil dihapus.")


@PY.INLINE("absen_hadir")
async def absen_inline(c, iq):
    query = iq.query
    group_id = int(query.split()[1])
    user_id = iq.from_user.id
    mention = iq.from_user.mention
    timestamp = datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%H:%M:%S")

    if group_id not in hadir_list:
        hadir_list[group_id] = []

    if any(user["user_id"] == user_id for user in hadir_list[group_id]):
        hadir_list[group_id].append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list(group_id)
    text = f"Daftar hadir untuk grup pada tanggal {timestamp}:\n{hadir_text}"

    buttons = [[InlineKeyboardButton("Tambah Hadir", callback_data=f"add_absen {group_id}")]]
    keyboard = InlineKeyboardMarkup(buttons)

    result = InlineQueryResultArticle(
        title="Daftar Hadir", input_message_content=InputTextMessageContent(text), reply_markup=keyboard
    )

    await c.answer_inline_query(iq.id, results=[result], cache_time=0)


@PY.CALLBACK("add_absen")
async def hadir_callback(c, cq):
    group_id = int(cq.data.split()[1])
    user_id = cq.from_user.id
    mention = cq.from_user.mention
    timestamp = datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone("Asia/Jakarta")).strftime("%H:%M:%S")

    if group_id not in hadir_list:
        hadir_list[group_id] = []

    if any(user["user_id"] == user_id for user in hadir_list[group_id]):
        await cq.answer("Anda sudah melakukan absen sebelumnya.", show_alert=True)
    else:
        hadir_list[group_id].append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list(group_id)
        text = f"Daftar hadir untuk grup pada tanggal {timestamp}:\n{hadir_text}"
        buttons = [[InlineKeyboardButton("Tambah Hadir", callback_data=f"add_absen {group_id}")]]
        keyboard = InlineKeyboardMarkup(buttons)
        await cq.edit_message_text(text, reply_markup=keyboard)
