from models import Task
from base import Session, engine, Base


Base.metadata.create_all(engine)
session = Session()

note = Task("", "", "", "")

app = Flask(__name__)
Session.add(note)