"""
===========================================================
AI Intrusion Detection System
Buzzer Module

Raspberry Pi 5 Compatible (gpiozero)
Author : Hemendrasinh Zala
===========================================================
"""

from gpiozero import Buzzer as GPIOBuzzer

from config import BUZZER_PIN
from core.logger import Logger


class Buzzer:
    """
    Controls the hardware buzzer.
    """

    def __init__(self):

        self.logger = Logger()

        self.buzzer = GPIOBuzzer(BUZZER_PIN)

        self.buzzer_on = False

        self.logger.info(
            "Hardware Buzzer Initialized Successfully."
        )

    # =====================================================
    # TURN ON
    # =====================================================

    def turn_on(self):

        if self.buzzer_on:
            return

        self.buzzer.on()

        self.buzzer_on = True

        self.logger.info(
            "Hardware Buzzer ON."
        )

    # =====================================================
    # TURN OFF
    # =====================================================

    def turn_off(self):

        if not self.buzzer_on:
            return

        self.buzzer.off()

        self.buzzer_on = False

        self.logger.info(
            "Hardware Buzzer OFF."
        )

    # =====================================================
    # STATUS
    # =====================================================

    def is_on(self):

        return self.buzzer_on

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):

        self.buzzer.off()

        self.buzzer.close()

        self.logger.info(
            "Hardware Buzzer Cleaned Successfully."
        )