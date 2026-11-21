"""
===========================================================
AI Intrusion Detection System
PIR Motion Sensor Module

Author : Hemendrasinh Zala

This module is responsible for:
1. Reading the PIR Motion Sensor.
2. Returning the motion status.
3. Supporting Raspberry Pi GPIO.

Sensor:
HC-SR501 PIR Motion Sensor
===========================================================
"""

try:

    import RPi.GPIO as GPIO  # type: ignore

    GPIO_AVAILABLE = True

except ImportError:

    GPIO_AVAILABLE = False


from config import PIR_PIN
from core.logger import Logger


class PIRSensor:
    """
    Handles PIR Motion Sensor operations.
    """

    def __init__(self):
        """
        Initialize the PIR Sensor.
        """

        self.logger = Logger()

        self.sensor_pin = PIR_PIN

        if GPIO_AVAILABLE:

            GPIO.setmode(GPIO.BCM)

            GPIO.setup(

                self.sensor_pin,

                GPIO.IN

            )

            self.logger.info(
                "PIR Sensor Initialized Successfully."
            )

        else:

            self.logger.warning(
                "RPi.GPIO not available. PIR Sensor disabled."
            )

    # =====================================================
    # READ SENSOR
    # =====================================================

    def detect_motion(self):
        """
        Read PIR Sensor.

        Returns
        -------
        bool
        """

        if not GPIO_AVAILABLE:

            return False

        try:

            if GPIO.input(self.sensor_pin):

                return True

            return False

        except Exception as error:

            self.logger.error(

                f"PIR Sensor Error : {error}"

            )

            return False

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):
        """
        Cleanup GPIO.
        """

        if GPIO_AVAILABLE:

            GPIO.cleanup(self.sensor_pin)

            self.logger.info(
                "PIR Sensor Cleaned Successfully."
            )