from flask import Flask, render_template

from domofon.klawisz import Klawisz

CHANNEL = 14
SECONDS = 5
KLAWISZ = Klawisz(CHANNEL)

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def lokaj():
    return render_template('lokaj.html')


@app.route("/otwórz/")
def otwórz():
    KLAWISZ.otwórz(SECONDS)
    return "Otwarte"


def run():
    app.run(host='0.0.0.0')
