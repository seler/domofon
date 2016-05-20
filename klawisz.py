import RPi.GPIO as GPIO
import time
import asyncio


class Klawisz:

    def __init__(ja, kanał):
        ja.kanał = kanał
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(kanał, GPIO.OUT, initial=GPIO.HIGH)

    def otwórz(ja, czas):
        def odpal():
            ja.sygnał(ja.kanał, GPIO.LOW, czas)
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, odpal)

    def __del__(ja):
        GPIO.cleanup(self.channel)

    def sygnał(ja, kanał, stan, czas):
        GPIO.output(kanał, stan)
        asyncio.sleep(czas)
        GPIO.output(kanał, not stan)
