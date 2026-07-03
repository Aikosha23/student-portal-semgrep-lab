from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/login")
def login():
    username = request.args.get("username")
    conn = sqlite3.connect("portal.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '%s'" % username
    cursor.execute(query)
    return str(cursor.fetchall())

if __name__ == "__main__":
    app.run(debug=True)
