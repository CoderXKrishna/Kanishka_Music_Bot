#
# Copyright (C) 2021-2022 by CoderXKrishna@Github, < https://github.com/CoderXKrishna >.
#
# This file is part of < https://github.com/CoderXKrishna/Kanishka_Music_Bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/CoderXKrishna/Kanishka_Music_Bot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from KanishkaMusic import LOGGER, app, userbot
from KanishkaMusic.core.call import Kanishka
from KanishkaMusic.plugins import ALL_MODULES
from KanishkaMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("KanishkaMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("KanishkaMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
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
        importlib.import_module("KanishkaMusic.plugins" + all_module)
    LOGGER("Kanishkamusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Kanishka.start()
    try:
        await Kanishka.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("KanishkaMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await Kanishka.decorators()
    LOGGER("KanishkaMusic").info("Kanishka Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("KanishkaMusic").info("Stopping Kanishka Music Bot! GoodBye")
