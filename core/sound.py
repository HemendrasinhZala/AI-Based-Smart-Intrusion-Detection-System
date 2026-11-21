"""
===========================================================
AI Intrusion Detection System
Sound Module

Author : Hemendrasinh Zala

This module is responsible for:
1. Playing the alarm sound.
2. Stopping the alarm sound.

Current Platform:
    Windows (winsound)

Future Platform:
    Raspberry Pi (GPIO Buzzer)
===========================================================
"""

import platform

from config import ALARM_SOUND
from core.logger import Logger

# ----------------------------------------------------------
# Import winsound only on Windows
# ----------------------------------------------------------

if platform.system() == "Windows":
    import winsound


class Sound:
    """
    Handles alarm sound operations.
    """

    def __init__(self):
        """
        Initialize the sound module.
        """

        self.logger = Logger()

        self.sound_file = str(ALARM_SOUND)

        self.alarm_playing = False

    # =======================================================
    # PLAY ALARM
    # =======================================================

    def play_alarm(self):
        """
        Play the alarm continuously.
        """

        # Prevent multiple alarm instances
        if self.alarm_playing:
            return

        try:

            if platform.system() == "Windows":

                winsound.PlaySound(
                    self.sound_file,
                    winsound.SND_FILENAME
                    | winsound.SND_ASYNC
                    | winsound.SND_LOOP
                )

            else:
                # Raspberry Pi support will be added later.
                self.logger.info(
                    "Alarm playback is not implemented "
                    "for this operating system yet."
                )

            self.alarm_playing = True

            self.logger.info("Alarm started.")

        except Exception as error:

            self.logger.error(
                f"Unable to play alarm: {error}"
            )

        # =======================================================
    # STOP ALARM
    # =======================================================

    def stop_alarm(self):
        """
        Stop the alarm sound.
        """

        if not self.alarm_playing:
            return

        try:

            if platform.system() == "Windows":

                # Stop the currently playing sound
                winsound.PlaySound(
                    None,
                    winsound.SND_PURGE
                )

            else:
                # Raspberry Pi support will be added later.
                self.logger.info(
                    "Alarm stop is not implemented "
                    "for this operating system yet."
                )

            self.alarm_playing = False

            self.logger.info("Alarm stopped.")

        except Exception as error:

            self.logger.error(
                f"Unable to stop alarm: {error}"
            )

    # =======================================================
    # ALARM STATUS
    # =======================================================

    def is_playing(self):
        """
        Check whether the alarm is currently playing.

        Returns
        -------
        bool
        """

        return self.alarm_playing