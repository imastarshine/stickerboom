import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
SOCKS5_PROXY_URL= str(os.getenv("SOCKS5_PROXY_URL"))
