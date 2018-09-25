from sqlalchemy import Column, String, Integer, Date
from base import Session, Base

session = Session()


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String())
    responsible = Column(String())
    date = Column(Date())

    def __init__(self, name, description, responsible, date):
        self.name = name
        self.description = description
        self.responsible = responsible
        self.date = date

    def __repr__(self):
        return '<Task %r>' % self.name

    @staticmethod
    def db_addition(note):
        session.add(note)
        session.commit()
        session.close()

    @staticmethod
    def db_get():
        return session.query(Task,
                            Task.name,
                            Task.description,
                            Task.responsible,
                            Task.date).all()
