from sqlalchemy import Column, String, Integer, Date
from base import Base, Session

session = Session()


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String())
    responsible = Column(String())
    date = Column(Date())

    def __init__(self, name=None, description=None, responsible=None, date=None):
        self.name = name
        self.description = description
        self.responsible = responsible
        self.date = date

    @staticmethod
    def db_addition(note):
        session.commit()
        session.close()
        session.add(note)

    @staticmethod
    def db_get():
        return Task.query.all()
