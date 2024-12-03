import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Gojo import LOGGER, app, userbot
from Gojo.core.call import Gojo
from Gojo.misc import sudo
from Gojo.plugins import ALL_MODULES
from Gojo.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ᴀssɪsᴛᴀɴᴛ ᴄʟɪᴇɴᴛ ᴠᴀʀɪᴀʙʟᴇs ɴᴏᴛ ᴅᴇғɪɴᴇᴅ, ᴇxɪᴛɪɴɢ...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Gojo.plugins" + all_module)
    LOGGER("Gojo.plugins").info("sᴜᴄᴄᴇssғᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ ᴍᴏᴅᴜʟᴇs...")
    await userbot.start()
    await Gojo.start()
    try:
        await Gojo.stream_call("https://telegra.ph/file/3c9b53024f150d99032e1.mp4")
    except NoActiveGroupCall:
        LOGGER("Gojo").error(
            "ᴘʟᴇᴀsᴇ sᴛᴀʀᴛ ʏᴏᴜʀ ʟᴏɢ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ\n\n ʙᴏᴛ sᴛᴏᴘᴘᴇᴅ......"
        )
        exit()
    except:
        pass
    await Gojo.decorators()
    LOGGER("Gojo").info(
        "\x43\x68\x61\x6D\x70\x75\x20\x42\x6F\x74\x20\x68\x61\x73\x20\x62\x65\x65\x6E\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x6C\x79\x20\x73\x74\x61\x72\x74\x65\x64\x2E\x0A\x0A\x40\x54\x68\x65\x43\x68\x61\x6D\x70\x75\x20"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Gojo").info("sᴛᴏᴘᴘɪɴɢ ᴄʜᴀᴍᴘᴜ ᴍᴜsɪᴄ ʙᴏᴛ...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
