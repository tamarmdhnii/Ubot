from PyroUbot import *

__MODULE__ = "cek khodam"
__HELP__ = """
<blockquote>
 Bantuan Untuk cek khodam

• Perintah: <code>{0}kodam</code>
• Penjelasan: Untuk melihat kodam yang ga guna.
</blockquote>
"""



@PY.UBOT("kodam")
async def _(client, message):
    await raxy_asu(client, message)
