#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "22371286"))
API_HASH = environ.get("API_HASH", "0a8636c4ec34557e1e9bcb62665748fb")
BOT_TOKEN = environ.get("BOT_TOKEN", "8047092841:AAGsFk_3QxSA4meJoJu0j7nc3cbkBQ5Vmtc")

OWNER = int(environ.get("OWNER", "7815387564"))
CREDIT = environ.get("CREDIT", "ADX")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7815387564').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

