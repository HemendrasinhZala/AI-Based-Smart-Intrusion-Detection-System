"""
===========================================================
AI Intrusion Detection System
Door Sensor Module

Raspberry Pi 5 Compatible (gpiozero)
Author : Hemendrasinh Zala
===========================================================
"""

from gpiozero import Button

from config import DOOR_SENSOR_PIN
from core.logger import Logger


class DoorSensor:
    """
    Handles Door Sensor operations.
    """

    def __init__(self):

        self.logger = Logger()

        # Reed switch connected between GPIO and GND
        self.sensor = Button(
            DOOR_SENSOR_PIN,
            pull_up=True
        )

        self.logger.info(
            "Door Sensor Initialized Successfully."
        )

    # =====================================================
    # DOOR STATUS
    # =====================================================

    def is_door_open(self):
        """
        Returns True if the door is OPEN.
        """

        # Button released -> Door Open
        return not self.sensor.is_pressed

    # =====================================================
    # GET STATUS
    # =====================================================

    def get_status(self):

        return "OPEN" if self.is_door_open() else "CLOSED"

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):

        self.sensor.close()

        self.logger.info(
            "Door Sensor Cleaned Successfully."
        )

        #python -c "from gpiozero import Buzzer; from time import sleep; b=Buzzer(22); b.on(); sleep(5); b.off()"