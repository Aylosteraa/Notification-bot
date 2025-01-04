import os
import requests 
from dotenv import load_dotenv

def send_message(token, chat_id, message):
    """
    Функція для відправки повідомлення через Telegram Bot API.
    """
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Повідомлення успішно надіслано!")
    else:
        print(f"Помилка при надсиланні повідомлення: {response.text}")


# Отримуємо токен і chat_id з секретів GitHub
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID1 = os.getenv("CHAT_ID1")
CHAT_ID2 = os.getenv("CHAT_ID2")
# Текст повідомлення
MESSAGE = os.getenv("MESSAGE")

if not BOT_TOKEN or not CHAT_ID1 or not CHAT_ID2 or not MESSAGE:
    raise ValueError("Необхідно налаштувати секрети BOT_TOKEN і CHAT_ID.")

# Відправка повідомлення
send_message(BOT_TOKEN, CHAT_ID1, MESSAGE)
send_message(BOT_TOKEN, CHAT_ID2, MESSAGE)
