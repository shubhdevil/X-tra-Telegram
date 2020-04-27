import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "No name set yet nibba"

@command(outgoing=True, pattern="^.alive$")
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**`YO BRO JABTAK YE KHEL KHATAM NHI HOTA APUN IDHARICH HAI ψ(｀∇´)ψ`**\n\n"
                     "`Telethon version: 61.9.0\nPython: 53.7.3\nBot by:` @ShubhDevil\n")
