import RPi.GPIO as GPIO
import requests
import json
import time


KANAŁ = 15
SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'
SLACK_HOOK_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
SLACK_HOOK_DATA = json.dumps({
    "channel": "#boot_test",
    "username": "Odźwierny",
    "text": "Ktoś stoi u Twoich drzwi, Panie. Czy mam <http://192.168.1.55:8000/|otworzyć>?",
    "icon_emoji": ":door:",
})


if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KANAŁ, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        while True:
            GPIO.wait_for_edge(KANAŁ, GPIO.FALLING)
            requests.post(SLACK_HOOK_URL, data=SLACK_HOOK_DATA, headers=SLACK_HOOK_HEADERS)
            time.sleep(10)
            
    except:
        GPIO.cleanup(KANAŁ)

