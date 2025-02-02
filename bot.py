import os
import re

from dotenv import load_dotenv
from whatsapp_chatbot_python import GreenAPIBot, Notification
from datetime import datetime

from db.db_handlers import remind

from task import time_await, update_db


load_dotenv()

bot = GreenAPIBot(
    os.getenv("API_ID_INSTANCE"),
    os.getenv("API_TOKEN_INSTANCE"),
)

pattern = r"remember\s+message:'([^']+)'\s+time:'((?:[01]?[0-9]|2[0-3]):([0-5]?[0-9]))'"


@bot.router.message(text_message="help")
def message_handler(notification: Notification) -> None:
    notification.answer(
        "send message 'remember  message:<your message> time:<time in 24 hour format>'\n"
        "example: remember message:'my birthday' time:'17:30'"
    )


@bot.router.message(regexp=pattern)
def message_handler(notification: Notification) -> None:
    """
    Обработка сообщения для запоминания
    сравнение с pattern, если совпадает, то запускаем задачу
    и добавляем в бд напоминание
    """

    match = re.match(pattern, notification.get_message_text())
    message = match.group(1)
    time_now = match.group(2)
    time_now = datetime.strptime(time_now, "%H:%M").time()
    now_time = datetime.combine(datetime.today(), time_now)
    count = (now_time - datetime.now()).total_seconds()
    update_db.apply_async(args=[notification.sender, message, now_time])
    time_await.apply_async(
        args=[notification.sender, message, now_time], countdown=count
    )

    notification.answer("Get it!! Wait for notification!")


@bot.router.message(text_message="remind")
def message_handler(notification: Notification) -> None:
    """
    Получить все напоминания, если они есть
    """

    reminders = remind(notification.sender)
    notification.answer("in progress")
    if len(reminders) < 1:
        notification.answer("You have no reminders")
    else:
        answer = "Reminders:\n" + "\n".join([str(rem) for rem in reminders])
        notification.answer(answer)


if __name__ == "__main__":
    bot.run_forever()
