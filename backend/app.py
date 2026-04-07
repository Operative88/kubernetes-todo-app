import os
import time
import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASSWORD", "mysecretpassword")
DB_NAME = os.environ.get("DB_NAME", "tododb")

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
            )
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            time.sleep(2)
    raise Exception("Nie można połączyć się z bazą danych")

@app.route('/api/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT task FROM todos ORDER BY id ASC;')
    rows = cur.fetchall()
    # Wyciągamy pierwszy element z krotki (treść zadania)
    todos = [row[0] for row in rows]
    cur.close()
    conn.close()
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    # Pobieramy wartość przypisaną do klucza 'task' wysłanego z JS
    new_task = data.get('task')
    
    if new_task:
        conn = get_db_connection()
        cur = conn.cursor()
        # WAŻNE: Wstawiamy zmienną new_task do kolumny 'task'
        cur.execute('INSERT INTO todos (task) VALUES (%s);', (new_task,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Zadanie dodane"}), 201
    return jsonify({"error": "Brak treści"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)