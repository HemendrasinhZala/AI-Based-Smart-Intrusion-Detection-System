"""
===========================================================
AI Intrusion Detection System
Motion Detector Module

Author : Hemendrasinh Zala

This module detects motion using frame differencing.
===========================================================
"""

import cv2

from config import (
    MIN_CONTOUR_AREA,
    BLUR_KERNEL_SIZE,
    COLOR_GREEN,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS,
)

from core.logger import Logger


class MotionDetector:
    """
    Detects motion from consecutive video frames.
    """

    def __init__(self):
        """
        Initialize the motion detector.
        """

        self.logger = Logger()

        # Previous grayscale frame
        self.previous_frame = None

        # Motion bounding boxes
        self.motion_boxes = []

    # =======================================================
    # DETECT MOTION
    # =======================================================

    def detect_motion(self, frame):
        """
        Detect motion in the current frame.

        Parameters
        ----------
        frame : numpy.ndarray

        Returns
        -------
        bool
            True if motion is detected, otherwise False.
        """

        # Clear previous motion boxes
        self.motion_boxes.clear()

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Reduce image noise
        gray = cv2.GaussianBlur(
            gray,
            BLUR_KERNEL_SIZE,
            0
        )

        # First frame initialization
        if self.previous_frame is None:

            self.previous_frame = gray

            return False

        # Calculate frame difference
        frame_difference = cv2.absdiff(
            self.previous_frame,
            gray
        )

        # Binary threshold
        _, threshold = cv2.threshold(
            frame_difference,
            25,
            255,
            cv2.THRESH_BINARY
        )

        # Remove small holes
        threshold = cv2.dilate(
            threshold,
            None,
            iterations=2
        )

        # Find contours
        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        motion_detected = False

        for contour in contours:

            area = cv2.contourArea(contour)

            if area < MIN_CONTOUR_AREA:
                continue

            x, y, w, h = cv2.boundingRect(contour)

            self.motion_boxes.append((x, y, w, h))

            motion_detected = True

        # Store current frame for next comparison
        self.previous_frame = gray

        return motion_detected
    
        # =======================================================
    # DRAW MOTION BOXES
    # =======================================================

    def draw_motion_boxes(self, frame):
        """
        Draw bounding boxes around detected motion.

        Parameters
        ----------
        frame : numpy.ndarray

        Returns
        -------
        numpy.ndarray
        """

        for (x, y, w, h) in self.motion_boxes:

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                COLOR_GREEN,
                2
            )

            cv2.putText(
                frame,
                "Motion",
                (x, y - 10),
                FONT,
                FONT_SCALE,
                COLOR_GREEN,
                FONT_THICKNESS
            )

        return frame