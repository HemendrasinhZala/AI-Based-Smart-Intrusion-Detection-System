"""
===========================================================
AI Intrusion Detection System
Logger Module

Author : Hemendrasinh Zala

This module provides logging functionality for the
entire project.
===========================================================
"""

import logging

from config import LOG_FILE
from core.utils import create_directories


class Logger:
    """
    Logger class used throughout the project.
    """

    def __init__(self):
        """
        Initialize the logger.
        """

        # Create required directories
        create_directories()

        self.logger = logging.getLogger(
            "AI_Intrusion_Detection_System"
        )

        # Prevent duplicate handlers
        if self.logger.hasHandlers():
            return

        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s",
            "%d-%m-%Y %H:%M:%S"
        )

        file_handler = logging.FileHandler(
            LOG_FILE,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)

    # =======================================================
    # INFO
    # =======================================================

    def info(self, message):
        """
        Log an information message.
        """

        self.logger.info(message)

    # =======================================================
    # WARNING
    # =======================================================

    def warning(self, message):
        """
        Log a warning message.
        """

        self.logger.warning(message)

    # =======================================================
    # ERROR
    # =======================================================

    def error(self, message):
        """
        Log an error message.
        """

        self.logger.error(message)

    # =======================================================
    # CRITICAL
    # =======================================================

    def critical(self, message):
        """
        Log a critical message.
        """

        self.logger.critical(message)

        # =======================================================
    # INTRUSION LOG
    # =======================================================

    def log_intrusion(
        self,
        event,
        image_path="",
        video_path=""
    ):
        """
        Log an intrusion event.

        Parameters
        ----------
        event : str
            Intrusion event description.

        image_path : str
            Saved image path.

        video_path : str
            Saved video path.
        """

        self.logger.info("=" * 60)
        self.logger.info("INTRUSION DETECTED")
        self.logger.info(f"Event : {event}")

        if image_path:
            self.logger.info(f"Image : {image_path}")

        if video_path:
            self.logger.info(f"Video : {video_path}")

        self.logger.info("=" * 60)

    # =======================================================
    # EXCEPTION
    # =======================================================

    def exception(self, message):
        """
        Log an exception with traceback.
        """

        self.logger.exception(message)