from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# ✅ MySQL Config (edit these)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "feedback_app"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit-feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json()
    message = data.get("message", "").strip()

    # Validation
    if not message:
        return jsonify({"success": False, "message": "All fields are required!"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = """
            INSERT INTO feedback (message)
            VALUES (%s)
        """
        cursor.execute(query, (message,))
        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"success": True, "message": "Feedback submitted successfully!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Database error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
