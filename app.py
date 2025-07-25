from flask import (
    Flask,
    jsonify,
    render_template,
    request,
)
import psycopg2
from config import Config
from scripts.recommend import recommend_materials
import os
import matplotlib.pyplot as plt

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
    return render_template('index.html', recommendations=None, plot_filename=None)


@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        min_strength = float(request.form.get('min_tensile_strength') or 100)
        max_density = float(request.form.get('max_density') or 1.5)
        max_cost = float(request.form.get('max_cost') or 3.0)
    except ValueError:
        min_strength = 100
        max_density = 1.5
        max_cost = 3.0

    recommendations = recommend_materials(
        min_tensile_strength=min_strength,
        max_density=max_density,
        max_cost=max_cost
    )

    plot_filename = None

    if recommendations:
        fibers = [f"{rec['fiber']} + {rec['resin']}" for rec in recommendations]
        strengths = [rec['combo_strength'] for rec in recommendations]

        plt.figure(figsize=(10, 6))
        plt.barh(fibers, strengths, color='skyblue')
        plt.xlabel('Tensile Strength (MPa)')
        plt.title('Recommended Fiber + Resin Combinations')
        plt.tight_layout()

        os.makedirs('static', exist_ok=True)
        plot_filename = 'recommendations_plot.png'
        plt.savefig(os.path.join('static', plot_filename))
        plt.close()

    return render_template(
        'index.html',
        recommendations=recommendations,
        plot_filename=plot_filename
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
