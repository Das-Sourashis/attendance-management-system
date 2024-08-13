# Sets up the database.

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    pass

class Subject(Base):
    __tablename__ = 'subjects'

    sid = Column(Integer, primary_key=True, autoincrement=True)
    subjectname = Column(String(50), unique=True, nullable=False)
    teacher = Column(String(50), nullable=False)
    type = Column(String(1), nullable=False)

    def __init__(self, sid, subjectname, teacher, type):
        self.sid = sid
        self.subjectname = subjectname
        self.teacher = teacher
        self.type = type

class Class(Base):
    __tablename__ = 'classes'

    date = Column(Date, primary_key=True)
    day = Column(Integer, nullable=False)
    sid = Column(Integer, ForeignKey('subjects.sid'), nullable=False, primary_key=True)
    duration = Column(Integer, nullable=False)
    studenttime = Column(Integer, nullable=False)

    subject = relationship('Subject', backref='classes')

    def __init__(self, argv):
        self.date = argv[0]
        self.day = argv[1]
        self.sid = argv[2]
        self.duration = argv[3]
        self.studenttime = argv[4]

class Date(Base):
    __tablename__ = 'startdate'

    sdate = Column(Date, primary_key=True)

def create_session():
    url = "sqlite:///attendance.db"
    engine = create_engine(url)
    
    # Check if database exists
    if not database_exists(engine.url): 
        create_database(engine.url)
    
    # Create tables
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

session = create_session()

