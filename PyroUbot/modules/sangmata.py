from PyroUbot import *

__MODULE__ = "sangmata"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀɴɢᴍᴀᴛᴀ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}sg</code> [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ʜɪsᴛᴏʀɪ ɴᴀᴍᴀ/ᴜsᴇʀɴᴀᴍᴇ
</blockquote>  
"""


@PY.UBOT("sg")
@PY.TOP_CMD
async def _(client, message):
    await sg_cmd(client, message)
