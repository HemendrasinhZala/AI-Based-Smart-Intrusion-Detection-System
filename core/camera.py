"""
===========================================================
AI Intrusion Detection System
Camera Module

Author : Hemendrasinh Zala

This module is responsible for:
1. Opening the USB camera.
2. Capturing frames.
3. Releasing the camera.

Platform:
    Raspberry Pi (USB Webcam)
===========================================================
"""

import cv2

from config import (
    CAMERA_INDEX,
    FRAME_WIDTH,
    FRAME_HEIGHT,
    FPS,
)

from core.logger import Logger


class Camera:
    """
    Handles USB webcam operations.
    """

    def __init__(self):
        """
        Initialize camera settings.
        """

        self.logger = Logger()
        self.cap = None

    # =======================================================
    # START CAMERA
    # =======================================================

    def start(self):
        """
        Open the USB webcam.
        """

        # Open USB webcam
        self.cap = cv2.VideoCapture(CAMERA_INDEX)

        if not self.cap.isOpened():

            self.logger.error("Unable to open USB webcam.")

            raise RuntimeError("Unable to open USB webcam.")

        # Set camera properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, FPS)

        self.logger.info("USB webcam started successfully.")

        print("Camera Opened:", self.cap.isOpened())

        # Warm-up camera
        print("Warming up camera...")

        for _ in range(30):
            self.cap.read()

        print("Camera ready.")

    # =======================================================
    # READ FRAME
    # =======================================================

    def read_frame(self):
        """
        Read a frame from the webcam.

        Returns
        -------
        tuple
            (success, frame)
        """

        if self.cap is None:

            self.logger.error("Camera has not been started.")

            return False, None

        success, frame = self.cap.read()

        if not success:

            self.logger.warning("Failed to read frame from webcam.")

            return False, None

        return True, frame

    # =======================================================
    # CAMERA STATUS
    # =======================================================

    def is_opened(self):
        """
        Check whether the camera is opened.

        Returns
        -------
        bool
        """

        return self.cap is not None and self.cap.isOpened()

    # =======================================================
    # RELEASE CAMERA
    # =======================================================

    def release(self):
        """
        Release the webcam resources.
        """

        if self.cap is not None:

            self.cap.release()

            self.cap = None

            self.logger.info("USB webcam released successfully.")