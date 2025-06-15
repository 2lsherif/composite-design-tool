from flask import Flask, render_template
import psycopg2
from config import DB_CONFIG

app = Flask(__name__)

def get_data(table):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table};")
        data = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
        cur.close()
        conn.close()
        return colnames, data
    except Exception as e:
        return [], [[f"Error: {e}"]]

@app.route("/")
def home():
    return "<h2>Composite Tool Flask App</h2><p>Visit /fibers or /resins to see data</p>"

@app.route("/fibers")
def fibers():
    headers, rows = get_data("fibers")
    return render_template("table.html", title="Fibers", headers=headers, rows=rows)

@app.route("/resins")
def resins():
    headers, rows = get_data("resins")
    return render_template("table.html", title="Resins", headers=headers, rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

