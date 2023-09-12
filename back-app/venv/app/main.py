from flask import Flask, request, jsonify
from prisma import Client

import os

os.environ['PRISMA_CLIENT_PYTHON_SCHEMA'] = '/Users/iairkaplun/Desktop/paginas/reactNative/prisma/schema.prisma'

from prisma import Client

app = Flask(__name__)
client = Client()


app = Flask(__name__)
client = Client()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = client.user.create({
        'data': {
            'email': data['email'],
            'password': data['password'],  
            'firstName': data.get('firstName'),
            'lastName': data.get('lastName'),
        }
    })
    return jsonify(new_user)

@app.route('/login', methods=['POST'])
def login():
    pass

if __name__ == '__main__':
    app.run(debug=True)