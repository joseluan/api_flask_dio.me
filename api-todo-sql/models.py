from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///api-todo-sql/todo.db', convert_unicode=True)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        bind=engine
    )
)


Base = declarative_base()
Base.query = db_session.query_property()

class People(Base):
    __tablename__='people'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    def __repr__(self):
        return f'<People {self.name} - {self.age}> '


class Todo(Base):
    __tablename__='todo'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), index=True)
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship('People')

    def __repr__(self):
        return f'<Todo {self.name} - {self.age}> '

def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()