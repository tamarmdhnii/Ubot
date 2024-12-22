from PyroUbot import *


__MODULE__ = "locks"
__HELP__ = """
<blockquote><b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏᴄᴋꜱ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}lock</code> [ᴛʏᴘᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴄɪ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}unlock</code> [ᴛʏᴘᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴋᴀ ɪᴢɪɴ ɢʀᴏᴜᴘ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{0}locks</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ɪᴢɪɴ ꜱᴀᴀᴛ ɪɴɪ.

  <b>• ᴛʏᴘᴇ : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`</blockquote>
"""


@PY.UBOT("lock|unlock")
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await locks_func(client, message)


@PY.UBOT("locks")
@PY.GROUP
@PY.TOP_CMD
async def _(client, message):
    await locktypes(client, message)
