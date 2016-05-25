from flask import Flask, render_template
import requests
import json

from domofon.klawisz import Klawisz

DEBUG = True
CHANNEL = 14
SECONDS = 5
KLAWISZ = Klawisz(CHANNEL)
SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'
SLACK_HOOK_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
SLACK_HOOK_DATA = json.dumps({
    "channel": "#office",
    "username": "Odźwierny",
    "text": "Otwarłem!",
    "icon_emoji": ":door:",
})

app = Flask(__name__)
app.config.from_object(__name__)


@app.route("/")
def lokaj():
    return render_template('lokaj.html')


@app.route("/otwórz/")
def otwórz():
    KLAWISZ.otwórz(SECONDS)
    requests.post(SLACK_HOOK_URL, data=SLACK_HOOK_DATA, headers=SLACK_HOOK_HEADERS)
    return "Otwarte"


def run():
    app.run(host='0.0.0.0')
