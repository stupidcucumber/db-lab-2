from flask import Flask, request, json
import pymongo


app = Flask(__name__)
client = pymongo.MongoClient(
    'mongodb://mongodb:27017',
    username='mongodb',
    password='password'
)

print(client.server_info())

database = client['santa']


@app.route('/users', methods=['GET'])
def get_all_users():
    result = database.users.find({})

    return json.dumps(list(result), default=str), 200


@app.route('/users/insert', methods=['POST'])
def insert_user():
    data = request.get_json()
    if data.get('telegram_id', None) is None or data.get('username', None) is None:
        return json.dumps({}), 500
    
    _ = database.users.insert_one({
        'telegram_id': data['telegram_id'],
        'username': data['username'],
        'about': data.get('about', '')
    })

    return json.dumps(data), 200


@app.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    database.users.delete_one(
        {
            'telegram_id': id
        }
    )

    return json.dumps({'telergam_id': id}), 200


@app.route('/users/patch/<int:id>', methods=['PATCH'])
def update_user(id: int):
    database.users.update_one({
        'telegram_id':id
    }, {'$set' : {'username': 'test_stupid'}})

    return json.dumps({ '_id': id}), 200


if __name__ == '__main__':
    app.run('0.0.0.0', 5052)