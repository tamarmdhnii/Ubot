from PyroUbot import *

__MODULE__ = "secret"
__HELP__ = """
<blockquote>
<b>◖ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴇᴄʀᴇᴛ ◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}msg</code> [ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ - ᴛᴇxᴛ]
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ sᴇᴄᴀʀᴀ ʀᴀʜᴀsɪᴀ
</blockquote>  
"""


@PY.UBOT("msg")
@PY.TOP_CMD
async def _(client, message):
    await msg_cmd(client, message)


@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
