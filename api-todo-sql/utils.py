from models import People, db_session

def search():
    people = People.query.all()
    print(people)


def insert_people():
    person = People(name='chico', age=24)
    db_session.add(person)
    db_session.commit()
    print(person)


def update_people():
    person = People.query.filter_by(name='chico').first()
    person.age = 90
    db_session.add(person)
    db_session.commit()


def delete_people():
    person = People.query.filter_by(name='maria').first()
    db_session.delete(person)
    db_session.commit()

if __name__ == '__main__':
    #insert_people()
    #update_people()
    delete_people()
    search()