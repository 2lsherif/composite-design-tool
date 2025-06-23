from flask import (
    Flask,
    jsonify,
    render_template,
    request,
)
import psycopg2
from config import Config
from scripts.recommend import recommend_materials


app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        dbname=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        host=Config.DB_HOST,
        port=Config.DB_PORT,
    )


@app.route('/')
def index():
    return render_template(
        'index.html',
        recommendations=None,
    )


@app.route('/recommend', methods=['POST'])
def recommend():
    min_strength = float(
        request.form.get('min_tensile_strength', 100)
    )
    max_density = float(request.form.get('max_density', 1.5))
    max_cost = float(request.form.get('max_cost', 3.0))

    recommendations = recommend_materials(
        min_tensile_strength=min_strength,
        max_density=max_density,
        max_cost=max_cost,
    )

    return render_template(
        'index.html',
        recommendations=recommendations,
    )


@app.route('/fibers')
def get_fibers():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM fibers LIMIT 10;")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()

    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)


@app.route('/resins')
def get_resins():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM resins LIMIT 10;")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    cur.close()
    conn.close()

    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
