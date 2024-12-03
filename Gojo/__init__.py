from Gojo.core.bot import Gojo
from Gojo.core.dir import dirr
from Gojo.core.git import git
from Gojo.core.userbot import Userbot
from Gojo.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER
import uvloop


uvloop.install()
dirr()
git()
dbb()
heroku()

app = Gojo()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
