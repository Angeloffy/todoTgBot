import os
from dotenv import load_dotenv
load_dotenv()

Bot_cfg = {
    "token": os.getenv("BOT_TOKEN"),
}
