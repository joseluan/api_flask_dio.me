from flask import Flask, request
from flask_restful import Resource, Api
from models import Users, Todos

app = Flask(__name__)
api = Api(app)


class User(Resource):
    
    def get(self, name):        
        try:
            user = Users.query.filter_by(name=name).first()        
            response = {
                'id': user.id,
                'name': user.name,
                'age': user.age,
            }        
        except AttributeError:
            response = {
                'status': 'erro',
                'mesage': "User not found"
            }
        except Exception as e:
            print(e)
            response = {
                'status': 'erro',
                'mesage': "General error"
            }
    
    
    def put(self, name):        
        try:
            user = Users.query.filter_by(name=name).first()        
            payload = request.get_json()
            if payload.get('name') is not None:
                user.name = payload.get('name')
            
            if payload.get('age') is not None:
                user.age = int()
            
            user.save()
            response = {
                'status': 'ok',
                'mesage': "User update with success"
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mesage': "User not found"
            }
        except Exception as e:
            print(e)
            response = {
                'status': 'erro',
                'mesage': "General error"
            }
   
   
    def delete(self, name):        
        try:            
            user = Users.query.filter_by(name=name).first()        
            user.delete()
            response = {
                'status': 'ok',
                'mesage': "User deleted with success"
            }
        except AttributeError:
            response = {
                'status': 'erro',
                'mesage': "User not found"
            }
        except Exception as e:
            print(e)
            response = {
                'status': 'erro',
                'mesage': "General error"
            }


        return response

class ListUsers(Resource):
    
    
    def get(self): 
        users = Users.query.all()
        users = [{'id': u.id, 'name': u.name, 'age': u.age} for u in users]
        return users

class ListTodos(Resource):

    def get(self):
        todos = Todos.query.all()

        todos = [{'id': t.id, 'name': t.name, 'name_user': t.user.name} for t in todos]
        return todos

    def post(self):
        payload = request.get_json()
        try:        
            user = Users.query.filter_by(name=payload.get('user')).first()        
            if user is None:
                raise AttributeError

            todo = Todos(name=payload.get('name'), user=user)
            todo.save()

            response = {
                'id': todo.id,
                'name': todo.name,
                'name_user': todo.user.name,
            }        
        except AttributeError:
            response = {
                'status': 'erro',
                'mesage': "User not found"
            }
        except Exception as e:
            print(e)
            response = {
                'status': 'erro',
                'mesage': "General error"
            }
            

        return response

api.add_resource(User, '/user/<string:name>')
api.add_resource(ListUsers, '/users/')
api.add_resource(ListTodos, '/todos/')

if __name__ == '__main__':
    app.run(debug=True)