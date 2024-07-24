from flask import Flask, request, jsonify
import psycopg2
import os
app =Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn
@app.route('/add_user', methods=['POST'])
def add_user():
    data= request.json
    conn= get_db_connection()
    cur = conn.cursor()
    cur.execute =('INSERT INTO users (name, email) VALUES (%s, %s)', (data['name'], data['email']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'user added successfully'}), 201

@app.route('/get_users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)