from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


class Database():

    def __init__(self):
        self.engine = create_engine('sqlite:///api-todo-sql/database.db')

        self.db_session = scoped_session(
            sessionmaker(
                autocommit=False,
                bind=self.engine
            )
        )


    def __exit__(self):
        self.db_session.close()



database = Database()

Base = declarative_base()
Base.query = database.db_session.query_property()

class Users(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    def __repr__(self):
        return f'<User {self.name} - {self.age}>'

    def save(self):
        database.db_session.add(self)
        database.db_session.commit()
    
    
    def delete(self):
        database.db_session.delete(self)
        database.db_session.commit()
    

class Todos(Base):
    __tablename__='todos'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users')

    def __repr__(self):
        return f'<Todos {self.name} - {self.age} - {self.user.name}> '

    def save(self):
        database.db_session.add(self)
        database.db_session.commit()
    
    def delete(self):
        database.db_session.delete(self)
        database.db_session.commit()
        

def init_db():
    Base.metadata.create_all(bind=database.engine)


if __name__ == '__main__':
    init_db()