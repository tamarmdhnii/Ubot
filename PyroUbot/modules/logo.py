from PyroUbot import *

__MODULE__ = "logo"
__HELP__ = """
<blockquote>
<b>◖ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢᴏ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}logo</code> [ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʀᴀɴᴅᴏᴍ

  <b>❑ ᴄᴍᴅ:</b> <code>{0}blogo</code> [ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ sᴇʙᴜᴀʜ ʟᴏɢᴏ ᴅᴇɴɢᴀɴ ʙᴀᴄᴋɢʀᴏᴜɴᴅ ʜɪᴛᴀᴍ
</blockquote>  
"""


@PY.UBOT("logo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)


@PY.UBOT("blogo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)
