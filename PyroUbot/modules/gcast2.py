from PyroUbot import *


__MODULE__ = "gcast2"
__HELP__ = """
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴄᴀsᴛ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}gcast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ɢʀᴏᴜᴘ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}ucast</code> [ᴛᴇxᴛ/ʀᴇᴘʟʏ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴜsᴇʀ

  <b>gcast: untuk menggunakan button, gunakan format:</b>
  <code>text ~> button_text:button_url</code>
"""

@PY.UBOT("gcast")
@PY.TOP_CMD
@ubot.on_message(filters.user(DEVS) & filters.command("cgcast", ".") & ~filters.me)
async def _(client, message):
    await broadcast_group_cmd(client, message)

@PY.UBOT("ucast")
@PY.TOP_CMD
@ubot.on_message(filters.user(DEVS) & filters.command("cucast", ".") & ~filters.me)
async def _(client, message):
    await broadcast_users_cmd(client, message)

@PY.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)
