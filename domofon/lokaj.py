from flask import Flask, render_template, request
import requests
import json
import subprocess
import re
import os

# from domofon.klawisz import Klawisz

CHANNEL = 14
SECONDS = 5
# KLAWISZ = Klawisz(CHANNEL)
SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'
SLACK_HOOK_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
SLACK_HOOK_DATA = {
    "channel": "#office",
    "username": "Odźwierny",
    "text": "Otwarłem ({})!",
    "icon_emoji": ":door:",
}

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

def get_name(ip):
    p = subprocess.Popen(('nmap', '-sP', ip), stdout=subprocess.PIPE,
                         cwd=os.path.dirname(__file__))
    string = p.communicate()[0].decode().strip()
    pattern = r"Nmap scan report for (.*) \({}\)".format(ip)
    search = re.search(pattern, string)
    if search and search.groups():
        name = search.groups()[0]
        if name.endswith('.lan'):
            name = name[0:-4]
        return name


@app.route("/")
def lokaj():
    return render_template('lokaj.html')


@app.route("/otwórz/")
def otwórz():
    data = SLACK_HOOK_DATA.copy()
    data['text'] = data['text'].format(get_name(request.remote_addr))
    KLAWISZ.otwórz(SECONDS)
    requests.post(SLACK_HOOK_URL, data=json.dumps(data), headers=SLACK_HOOK_HEADERS)
    print(data['text'])
    return "Otwarte"


def run():
    app.run(host='0.0.0.0')
