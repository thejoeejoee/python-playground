from random import choice
from time import sleep

import RPi.GPIO as GPIO


class LEDCatcher(object):
    WIN_DELAY_ON = .2
    WIN_DELAY_OFF = .2
    WIN_BEEPS_COUNT = 4
    BOUNCE_BUTTON_TIME = 200
    SLEEP_TIME = lambda self: .2

    LED_PINS = (5, 6, 13, 19, 26)
    BUTTON_PINS = (25, 24, 23, 18, 15)
    BUTTON_2_LED = {button: led for led, button in zip(LED_PINS, BUTTON_PINS)}

    def __init__(self):
        self.active_led = []
        self.win_celebration = False

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        map(lambda pin: GPIO.setup(pin, GPIO.OUT), self.LED_PINS)
        map(lambda pin: GPIO.setup(pin, GPIO.IN), self.BUTTON_PINS)
        map(lambda pin: GPIO.add_event_detect(pin, GPIO.RISING,
                                              callback=self.on_button_press,
                                              bouncetime=self.BOUNCE_BUTTON_TIME),
            self.BUTTON_PINS)

    def on_win(self):
        for _ in range(self.WIN_BEEPS_COUNT):
            map(lambda pin: GPIO.output(pin, True), self.LED_PINS)
            sleep(self.WIN_DELAY_ON)
            map(lambda pin: GPIO.output(pin, False), self.LED_PINS)
            sleep(self.WIN_DELAY_OFF)

    def on_button_press(self, pin):
        if self.BUTTON_2_LED[pin] in self.active_led and not self.win_celebration:
            self.win_celebration = True
            self.on_win()
            self.win_celebration = False

    def run(self):
        try:
            self.setup()
            while True:
                led_pin = choice(self.LED_PINS)
                GPIO.output(led_pin, True)
                self.active_led.append(led_pin)
                sleep(self.SLEEP_TIME())
                GPIO.output(led_pin, False)
                self.active_led.remove(led_pin)
        except Exception:
            raise
        finally:
            GPIO.cleanup()


led_catcher = LEDCatcher()
led_catcher.run()
