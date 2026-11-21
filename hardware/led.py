"""
===========================================================
AI Intrusion Detection System
LED Module

Raspberry Pi 5 Compatible (gpiozero)
Author : Hemendrasinh Zala
===========================================================
"""

from gpiozero import LED as GPIOLED

from config import (
    GREEN_LED_PIN,
    YELLOW_LED_PIN,
    RED_LED_PIN,
)

from core.logger import Logger


class LED:

    def __init__(self):

        self.logger = Logger()

        self.green = GPIOLED(GREEN_LED_PIN)
        self.yellow = GPIOLED(YELLOW_LED_PIN)
        self.red = GPIOLED(RED_LED_PIN)

        self.turn_off_all()

        self.logger.info(
            "LED Module Initialized Successfully."
        )

    # =====================================================
    # TURN OFF ALL LEDs
    # =====================================================

    def turn_off_all(self):

        self.green.off()
        self.yellow.off()
        self.red.off()

    # =====================================================
    # LOW
    # =====================================================

    def show_low(self):

        self.turn_off_all()
        self.green.on()

    # =====================================================
    # MEDIUM
    # =====================================================

    def show_medium(self):

        self.turn_off_all()
        self.yellow.on()

    # =====================================================
    # HIGH
    # =====================================================

    def show_high(self):

        self.turn_off_all()
        self.red.on()

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):

        self.turn_off_all()

        self.green.close()
        self.yellow.close()
        self.red.close()

        self.logger.info(
            "LED Module Cleaned Successfully."
        )