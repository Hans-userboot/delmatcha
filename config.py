# Codexbotz # @mrismanaziz

import logging
import os
from distutils.util import strtobool
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv("config.env")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

API_ID = int(os.environ.get("API_ID", "24571271"))
API_HASH = os.environ.get("API_HASH", "c66be78368878e1e1c5c25296a8572ed")

CHANNEL_DB = int(os.environ.get("CHANNEL_DB", "-1002227460255"))
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://delmatcha:delvanilla@cluster0.2wzbg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

RESTRICT = strtobool(os.environ.get("RESTRICT", "True"))

FORCE_SUB_1 = int(os.environ.get("FORCE_SUB_1", "0"))
FORCE_SUB_2 = int(os.environ.get("FORCE_SUB_2", "0"))
FORCE_SUB_3 = int(os.environ.get("FORCE_SUB_3", "0"))
FORCE_SUB_4 = int(os.environ.get("FORCE_SUB_4", "0"))

WORKERS = int(os.environ.get("WORKERS", "4"))

START_MESSAGE = os.environ.get(
    "START_MESSAGE",
    "Halo {mention}!"
    "\n\n"
    "Saya dapat menyimpan file pribadi di Channel tertentu dan pengguna lain dapat mengaksesnya dari link khusus.",
)
FORCE_MESSAGE = os.environ.get(
    "FORCE_MESSAGE",
    "Halo {mention}!"
    "\n\n"
    "Anda harus bergabung di Channel/Group terlebih dahulu untuk melihat file yang saya bagikan."
    "\n\n"
    "Silakan Join Ke Channel/Group terlebih dahulu.",
)

try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "6141496735 5178772086").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")
    
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
DISABLE_BUTTON = strtobool(os.environ.get("DISABLE_BUTTON", "False"))


LOGS_FILE = "logs.txt"
logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOGS_FILE, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
