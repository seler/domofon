import RPi.GPIO as GPIO
import requests
import json
import time


ILOSC_SRPAWDZEN = 2
MAIN_PAUSE = 100
KANAL = 15

SLACK_HOOK_URL = 'https://hooks.slack.com/services/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'
SLACK_HOOK_HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}
SLACK_HOOK_DATA = json.dumps({
    "channel": "#boot_test",
    "username": "Odzwierny",
    "text": "Ktos stoi u Twoich drzwi, Panie. Czy mam <http://192.168.1.55:8000/|otworzyc>?",
    "icon_emoji": ":door:",
})


if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(KANAL, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        licznik=0
        slack_info=False
        pause=0
        while True:
            time.sleep(.1)
            if pause>0:
                pause-=1
                continue

            if GPIO.input(KANAL) == GPIO.HIGH:
                licznik+=1
                if licznik == ILOSC_SRPAWDZEN:
                    licznik=0
                    slack_info=True
            else: licznik=0

            if slack_info:
                pause=MAIN_PAUSE
                slack_info=False
                requests.post(SLACK_HOOK_URL, data=SLACK_HOOK_DATA, headers=SLACK_HOOK_HEADERS)
    except:
        GPIO.cleanup(KANAL)

