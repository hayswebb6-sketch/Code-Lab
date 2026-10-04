import os

from flask import Flask, abort, send_from_directory

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = os.path.join(BASE, "Code Lab")
INDEX = "learning-html.html"

app = Flask(__name__, static_folder=None)


@app.route("/")
@app.route("/<path:filename>")
def serve(filename=None):
    name = filename or INDEX
    try:
        return send_from_directory(FILES, name)
    except FileNotFoundError:
        abort(404)
