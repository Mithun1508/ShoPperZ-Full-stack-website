from flask import Flask

app = Flask(__name__)


def template(file: str, *data):
    p = open(file).read()
    return p.format(*data)


def addRoute(url: str, func):
    app.add_url_rule("/", url, func)


def runApp(p: int):
    app.run("0.0.0.0", port=p)
