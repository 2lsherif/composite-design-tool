from flask import Flask, jsonify
import psycopg2
from config import Config

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT
    )


@app.route('/')
def index():
    return 'Composite Design Tool: PostgreSQL is connected ✅'


@app.route('/fibers')
def get_fibers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fibers LIMIT 10;")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])


@app.route('/resins')
def get_resins():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM resins LIMIT 10;")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()
    return jsonify([dict(zip(columns, row)) for row in rows])


if __name__ == '__main__':
    app.run(debug=True)
