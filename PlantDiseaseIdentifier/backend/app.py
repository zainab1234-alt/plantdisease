
from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="plants_db",
        user="user",
        password="password"
    )
    return conn

@app.route('/identify', methods=['POST'])
def identify_disease():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    # Simulate disease identification by file name
    plant_name = file.filename.split('.')[0]  # Use file name as plant name

    # Query database for plant disease details
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diseases WHERE plant = %s", (plant_name,))
    disease = cursor.fetchone()
    conn.close()

    if disease:
        return jsonify({
            "plant": disease[1],
            "disease": disease[2],
            "symptoms": disease[3],
            "treatment": disease[4]
        })
    return jsonify({"error": "No disease information found for this plant"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
