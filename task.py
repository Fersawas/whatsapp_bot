from celery import Celery
from api import send_remind
import logging

from db.db_handlers import save_reminder, del_remind


app = Celery(
    "task",
    broker="redis://redis:6379/1",
    backend="redis://redis:6379/1",
)


app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
)

logger = logging.getLogger("celery")


@app.task
def time_await(user, message, time):
    logger.info("start task time_await")
    send_remind(user, message)
    logger.debug("end task")
    logger.debug("del remind")
    del_remind(user, message)
    logger.debug("deleted")
    return f"{user}, {message}, {time}"


@app.task
def update_db(user, message, time):
    logger.info("start task update_db")
    save_reminder(user, message, time)
    logger.debug("end update db")
