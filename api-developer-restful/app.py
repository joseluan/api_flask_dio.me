from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

developers = [
    {
        'name': 'José Luan',
        'skills': ['Python', 'Flask']
    },
    {
        'name': 'Maria da silva',
        'skills': ['Java', 'Spring']
    }
]

class Developer(Resource):
    
    def get(self, id):
        try:
            response =  developers[id]
        except IndexError:
            response = {
                'status': 'erro',
                'mesage': "Developer not found"
            }
        except Exception:
            response = {
                'status': 'erro',
                'mesage': "Mysterious error"
            }


        return response
    def put(self, id):
        developers[id] = request.get_json()
        return {
            'status': 'ok',
            'mesage': "Developer update with success"
        } 
    def delete(self, id):
        developers.pop(id)
        return {
            'status': 'ok',
            'mesage': "Developer removed with success"
        }

class ListDevelopers(Resource):

    def get(self):
        return developers
    
    def post(self):
        pos = len(developers)
        developers.append(request.get_json())
        return {
            'status': 'ok',
            'mesage': "Developer create with success",
            'id': pos
        }        


api.add_resource(Developer, '/dev/<int:id>')
api.add_resource(ListDevelopers, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)