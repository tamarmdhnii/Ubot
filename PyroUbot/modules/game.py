from PyroUbot import *

__MODULE__ = "game"
__HELP__ = """
<blockquote>
<b>◖Bantuan Untuk Game◗</b>

  <b>❑ ᴄᴍᴅ:</b> <code>{0}catur</code> 
  <b>➠ ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> untuk mengeluarkan game catur 
</blockquote>
"""

@PY.UBOT("catur")
@PY.TOP_CMD
async def _(client, message):
    await catur_cmd(client, message)
