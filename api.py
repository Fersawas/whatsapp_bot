import requests
import os

from dotenv import load_dotenv


load_dotenv()


def send_remind(user, message):
    """
    Отправка сообщения ботом через Green API
    """

    url = f"https://1103.api.green-api.com/waInstance{os.getenv('API_ID_INSTANCE')}/sendMessage/{os.getenv('API_TOKEN_INSTANCE')}"

    payload = {"chatId": user, "message": f"Remind you: {message}"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    return response.status_code
