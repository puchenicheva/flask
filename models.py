from sqlalchemy import Column, String, Integer, Date
from base import Base


class Task (Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    responsible = Column(String(50), nullable=False)
    date = Column(Date, nullable=False)

    def __init__(self,name, description, responsible, date):
        self.name = name
        self.description = description
        self.responsible = responsible
        self.date = date

    




