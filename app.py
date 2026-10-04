import mimetypes
import os

BASE = os.path.dirname(os.path.abspath(__file__))
FILES = os.path.join(BASE, "Code Lab")
INDEX = "learning-html.html"


def app(environ, start_response):
    path = environ["PATH_INFO"].lstrip("/") or INDEX

    full = os.path.normpath(os.path.join(FILES, path))
    if not full.startswith(FILES) or not os.path.isfile(full):
        start_response("404 Not Found", [("Content-Type", "text/plain")])
        return [b"Not Found"]

    ctype = mimetypes.guess_type(full)[0] or "application/octet-stream"
    with open(full, "rb") as f:
        body = f.read()

    start_response("200 OK", [("Content-Type", ctype)])
    return [body]
