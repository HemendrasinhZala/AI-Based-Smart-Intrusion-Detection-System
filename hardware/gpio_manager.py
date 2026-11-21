"""
===========================================================
AI Intrusion Detection System
GPIO Manager Module

Author : Hemendrasinh Zala

This module initializes and cleans up Raspberry Pi GPIO.

All hardware modules should use this manager.
===========================================================
"""

try:

    import RPi.GPIO as GPIO      # type: ignore

    GPIO_AVAILABLE = True

except ImportError:

    GPIO_AVAILABLE = False


from core.logger import Logger


class GPIOManager:
    """
    Central GPIO Manager.
    """

    _initialized = False

    def __init__(self):
        """
        Initialize GPIO Manager.
        """

        self.logger = Logger()

    # =====================================================
    # INITIALIZE GPIO
    # =====================================================

    def initialize(self):
        """
        Initialize GPIO once.
        """

        if not GPIO_AVAILABLE:

            self.logger.warning(
                "RPi.GPIO not available."
            )

            return

        if GPIOManager._initialized:

            return

        GPIO.setmode(GPIO.BCM)

        GPIO.setwarnings(False)

        GPIOManager._initialized = True

        self.logger.info(
            "GPIO Initialized Successfully."
        )

    # =====================================================
    # CLEANUP
    # =====================================================

    def cleanup(self):
        """
        Cleanup all GPIO pins.
        """

        if not GPIO_AVAILABLE:

            return

        GPIO.cleanup()

        GPIOManager._initialized = False

        self.logger.info(
            "GPIO Cleaned Successfully."
        )