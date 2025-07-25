from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    send_file,
)
import io
import psycopg2
import matplotlib.pyplot as plt
from config import Config
from adjustText import adjust_text
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
    return render_template('index.html', recommendations=None)


@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        min_strength = float(
            request.form.get('min_tensile_strength') or 100
        )
        max_density = float(
            request.form.get('max_density') or 1.5
        )
        max_cost = float(
            request.form.get('max_cost') or 3.0
        )
    except ValueError:
        min_strength = 100
        max_density = 1.5
        max_cost = 3.0

    recommendations = recommend_materials(
        min_tensile_strength=min_strength,
        max_density=max_density,
        max_cost=max_cost,
    )

    return render_template(
        'index.html',
        recommendations=recommendations,
    )


@app.route('/plot')
def plot():
    data = recommend_materials()
    if not data:
        return 'No data to plot', 404

    densities = [rec["combo_density"] for rec in data]
    strengths = [rec["combo_strength"] for rec in data]
    labels = [f"{rec['fiber']} + {rec['resin']}" for rec in data]

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(densities, strengths, c='blue')

    # Create all label texts
    texts = []
    for x, y, label in zip(densities, strengths, labels):
        texts.append(ax.text(x, y, label, fontsize=8))

    # Adjust to prevent overlap
    adjust_text(
        texts,
        only_move={'points': 'y', 'texts': 'y'},
        arrowprops=dict(arrowstyle="->", color='gray', lw=0.5)
    )

    ax.set_xlabel("Combo Density (g/cm³)")
    ax.set_ylabel("Combo Tensile Strength (MPa)")
    ax.set_title("Composite Material Recommendations")
    ax.grid(True)

    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)
    plt.close(fig)

    return send_file(img, mimetype='image/png')


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
