from db.database import Session
from db.models import Reminder
import datetime as dt
from db.schema import ReminderSchema


def save_reminder(user, message, time) -> None:
    '''
    Создаем напоминание в БД
    '''

    db: Session = Session()
    try:
        if isinstance(time, dt.datetime):
            time = time.time()
        reminder = Reminder(user=user, title=message, time=time)
        db.add(reminder)
        db.commit()
        return reminder
    except Exception as e:
        db.rollback()
        print(e)
        return e
    finally:
        db.close()

def remind(user) -> None:
    '''
    Получаем все напоминания
    '''
    db: Session = Session()
    try:
        reminders = db.query(Reminder).filter(Reminder.user == user).all()
        return [ReminderSchema.from_orm(reminder) for reminder in reminders]
    except Exception as e:
        db.rollback()
        return e
    finally:
        db.close()

def del_remind(user, title):
    '''
    Удаление напоминания фильтр по пользователю и заголовку
    '''

    db: Session = Session()
    try:
        db.query(Reminder).filter(Reminder.user == user, Reminder.title == title).delete()
        db.commit()
    except Exception as e:
        db.rollback()
        return e
    finally:
        db.close()
