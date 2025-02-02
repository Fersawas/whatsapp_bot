import pydantic
from datetime import time


class ReminderSchema(pydantic.BaseModel):
    title: str
    time: str

    @classmethod
    def from_orm(cls, reminder):
        reminder_time = (
            reminder.time.isoformat()
            if isinstance(reminder.time, time)
            else reminder.time
        )
        return cls(
            title=reminder.title,
            time=reminder_time,
        )
