from flask import Flask, request, json
import psycopg2 as db

# Connecting to the database and instantiating connection with server
app = Flask(__name__)
database = db.connect(database='santa', host='0.0.0.0', user='postgres', password='password', port=5434)


########################################### All important routes
@app.route('/users', methods=['GET'])
def get_all_users():
    cursor = database.cursor()
    cursor.execute(
        '''
            SELECT * FROM users;
        '''
    )
    result = cursor.fetchall()

    cursor.close()

    return json.dumps(result), 200


@app.route('/groups', methods=['GET'])
def get_all_groups():
    cursor = database.cursor()
    cursor.execute(
        '''
            SELECT * FROM groups;
        '''
    )

    result = cursor.fetchall()

    cursor.close()

    return json.dumps(result), 200


@app.route('/users/insert', methods=['POST'])
def insert_user():
    '''
        This method extracts telegram_id, username, and about fields and inserts
    user into database.
    '''
    data = request.get_json()
    if data.get('telegram_id', None) is None or data.get('username', None) is None:
        return '', 500

    cursor = database.cursor()
    cursor.execute(
        '''
            INSERT INTO users (telegram_id, username, about) VALUES (%d, '%s', '%s');
        ''' % (data['telegram_id'], data['username'], data['about'])
    )

    database.commit()
    cursor.close()
    
    return json.dumps(data), 200


@app.route('/groups/insert', methods=['POST'])
def insert_group():
    '''
        This method extracts group_name, admin_id, and inserts new group into groups table.
    Also this method inserts admin_id into members table.
    '''
    data = request.get_json()
    if data.get('group_name', None) is None or data.get('group_name', None) == '' or data.get('admin_id', None) is None:
        return '', 500
    
    cursor = database.cursor()
    cursor.execute(
        '''
            INSERT INTO groups (admin_id, group_name) VALUES (%d, "%s");
        ''' % (data['admin_id'], data['group_name'])
    )

    group_id = cursor.lastrowid

    cursor.execute(
        '''
            INSERT INTO members (group_id, recipient_id, desired) VALUES (%d, %d, "%s")
        ''' % (group_id, data['admin_id'], data.get('desired', ''))
    )

    database.commit()
    cursor.close()

    return json.dumps(data), 200


@app.route('/members/insert', methods=['POST'])
def insert_member():
    data = request.get_json()
    if data.get('telegram_id', None) is None or data.get('group_id', None) is None:
        return '', 500
    
    cursor = database.cursor()
    cursor.execute(
        '''
            INSERT INTO members (group_id, recipient_id, desired) VALUES (%d, %d, "%s")
        ''' % (data['group_id'], data['telegram_id'], data.get('desired', ''))
    )

    database.commit()
    cursor.close()

    return json.dumps(data), 200 


@app.route('/members/group/<int:group_id>', methods=['GET'])
def get_group_members(group_id):
    cursor = database.cursor()
    cursor.execute(
        '''
            SELECT *
            FROM members
            WHERE group_id = %d
        ''' % group_id
    )

    result = cursor.fetchall()

    cursor.close()

    return json.dumps(result), 200


@app.route('/members/santa/<int:telegram_id>', methods=['GET'])
def get_recipients(telegram_id):
    cursor = database.cursor()
    cursor.execute(
        '''
            SELECT * 
            FROM members
            WHERE santa_id = %d
        ''' % telegram_id
    )
    
    result = cursor.fetchall()

    cursor.close()

    return result, 200


# Run the backend
if __name__ == '__main__':
    app.run('localhost', 5051)