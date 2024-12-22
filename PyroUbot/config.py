import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "26544825")) 
API_HASH = os.getenv("API_HASH", "602ce7378e8cc80485663eb7df57decb") 
BOT_TOKEN = os.getenv("BOT_TOKEN", "7907929712:AAFzHM3hUzQtB-ZiAFzGyx-IPykdjQT9hhs") 
OWNER_ID = int(os.getenv("OWNER_ID", "7722544952")) 
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002442350320"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002367286705 -1002315219516 -1002239800569").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "50"))
RMBG_API = os.getenv("RMBG_API", "")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "")
DEVS = list(map(int, os.getenv("DEVS", "7722544952 #927338035").split()))
MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
