#
# Copyright (C) 2021-2022 by CoderXKrishna@Github, < https://github.com/CoderXKrishna >.
#
# This file is part of < https://github.com/CoderXKrishna/Kanishka_Music_Bot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/CoderXKrishna/Kanishka_Music_Bot/blob/master/LICENSE >
#
# All rights reserved.

from KanishkaMusic.core.bot import KanishkaBot
from KanishkaMusic.core.dir import dirr
from KanishkaMusic.core.git import git
from KanishkaMusic.core.userbot import Userbot
from KanishkaMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = KanishkaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
