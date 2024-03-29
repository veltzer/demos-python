"""
This example catches all urls via variables.

References:
- https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
- https://stackoverflow.com/questions/14023864/flask-url-route-route-all-other-urls-to-some-function
"""

import flask

app = flask.Flask(__name__)


@app.route("/")
def empty():
    return flask.redirect("/index.html")


@app.route("/<path:path>")
def all_routes(path):
    return f"path is [{path}]"


print(app.url_map)

app.run(port=8000, host="0.0.0.0")
