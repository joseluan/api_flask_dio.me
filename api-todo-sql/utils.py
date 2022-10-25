from models import Users, Database


database = Database()

def search():
    user = Users.query.all()
    print(user)


def insert_user():
    person = Users(name='maria', age=78)
    database.db_session.add(person)
    database.db_session.commit()
    print(person)


def update_user():
    person = Users.query.filter_by(name='chico').first()
    person.age = 90
    database.db_session.add(person)
    database.db_session.commit()


def delete_user():
    person = Users.query.filter_by(name='maria').first()
    database.db_session.delete(person)
    database.db_session.commit()

if __name__ == '__main__':
    #insert_user()
    #update_user()
    #delete_user()
    search()