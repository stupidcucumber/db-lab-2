from flask import Flask, request, json
import pymongo


app = Flask(__name__)
database = pymongo.MongoClient('mongodb://localhost:27017')['santa']


@app.route('/users', methods=['GET'])
def get_all_users():
    pass


@app.route('/users/insert', methods=['POST'])
def insert_user():
    pass


@app.route('/users/delete/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    pass


@app.route('/users/patch/<int:id>', methods=['PUT'])
def update_user(id: int):
    pass


if __name__ == '__main__':
    app.run('localhost', 5052)