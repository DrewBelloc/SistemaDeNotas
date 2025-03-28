#!/usr/bin/env python3
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>funciona</h1>"

if __name__=="__main__":
    main()
