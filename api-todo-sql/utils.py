from models import Users, db_session

def search():
    user = Users.query.all()
    print(user)


def insert_user():
    person = Users(name='maria', age=78)
    db_session.add(person)
    db_session.commit()
    print(person)


def update_user():
    person = Users.query.filter_by(name='chico').first()
    person.age = 90
    db_session.add(person)
    db_session.commit()


def delete_user():
    person = Users.query.filter_by(name='maria').first()
    db_session.delete(person)
    db_session.commit()

if __name__ == '__main__':
    insert_user()
    #update_user()
    #delete_user()
    search()