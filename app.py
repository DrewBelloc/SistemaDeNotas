import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("script.html")

if __name__=="__main__":
    main()
