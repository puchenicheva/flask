from task import Task
from base import Session, engine, Base
from main import task_post


def validation_date(self):
    name_task, task_description, responsible_for_the_task, task_end_date = task_post()
    self.note = Task(name_task, task_description, responsible_for_the_task, task_end_date)
    return self.note


Base.metadata.create_all(engine)

session = Session()

Note = validation_date()
session.add(Note)
session.commit()
session.close()
