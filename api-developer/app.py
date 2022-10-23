from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developer(id):
    if request.method == 'GET':    
        try:
            response =  jsonify(developers[id])
        except IndexError:
            response = jsonify({
                'status': 'erro',
                'mesage': "Developer not found"
            })
        except Exception:
            response = jsonify({
                'status': 'erro',
                'mesage': "Mysterious error"
            })


        return response
    elif request.method == 'PUT':
        developers[id] = request.get_json()
        return jsonify({
            'status': 'ok',
            'mesage': "Developer update with success"
        })
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({
            'status': 'ok',
            'mesage': "Developer removed with success"
        })    



@app.route('/dev/', methods=['GET', 'POST'])
def list_developers():
    if request.method == 'GET':
        return jsonify(developers)
    elif request.method == 'POST':
        pos = len(developers)
        developers.append(request.get_json())
        return jsonify({
            'status': 'ok',
            'mesage': "Developer create with success",
            'id': pos
        }) 


if __name__ == '__main__':
    app.run(debug=True)