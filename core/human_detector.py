"""
===========================================================
AI Intrusion Detection System
Human Detector Module

Author : Hemendrasinh Zala

This module detects humans using the YOLOv8 model.
===========================================================
"""

import cv2
from ultralytics import YOLO

from config import (
    YOLO_MODEL,
    CONFIDENCE_THRESHOLD,
    COLOR_RED,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS,
)

from core.logger import Logger


class HumanDetector:
    """
    Detect humans using the YOLOv8 model.
    """

    def __init__(self):
        """
        Initialize the human detector.
        """

        self.logger = Logger()

        try:

            # Load YOLO model only once
            self.model = YOLO(str(YOLO_MODEL))

            self.logger.info(
                "YOLO model loaded successfully."
            )

        except Exception as error:

            self.logger.error(
                f"Failed to load YOLO model: {error}"
            )

            raise

        # Store detected human bounding boxes
        self.human_boxes = []

    # =======================================================
    # DETECT HUMANS
    # =======================================================

    def detect_humans(self, frame):
        """
        Detect humans in the given frame.

        Parameters
        ----------
        frame : numpy.ndarray

        Returns
        -------
        bool
            True if at least one human is detected.
        """

        self.human_boxes.clear()

        try:

            results = self.model(
                frame,
                verbose=False
            )

            human_detected = False

            for result in results:

                for box in result.boxes:

                    class_id = int(box.cls[0])

                    confidence = float(box.conf[0])

                    # Person class
                    if class_id != 0:
                        continue

                    if confidence < CONFIDENCE_THRESHOLD:
                        continue

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    self.human_boxes.append(
                        (
                            x1,
                            y1,
                            x2,
                            y2,
                            confidence
                        )
                    )

                    human_detected = True

            return human_detected

        except Exception as error:

            self.logger.error(
                f"Human detection failed: {error}"
            )

            return False

    # =======================================================
    # DRAW BOXES
    # =======================================================

    def draw_boxes(self, frame):
        """
        Draw bounding boxes around detected humans.

        Parameters
        ----------
        frame : numpy.ndarray

        Returns
        -------
        numpy.ndarray
        """

        for (
            x1,
            y1,
            x2,
            y2,
            confidence,
        ) in self.human_boxes:

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                COLOR_RED,
                2,
            )

            label = f"Human {confidence:.2f}"

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                FONT,
                FONT_SCALE,
                COLOR_RED,
                FONT_THICKNESS,
            )

        return frame

    # =======================================================
    # GET DETECTIONS
    # =======================================================

    def get_human_boxes(self):
        """
        Return all detected human bounding boxes.

        Returns
        -------
        list
        """

        return self.human_boxes

    # =======================================================
    # DETECTION COUNT
    # =======================================================

    def get_human_count(self):
        """
        Return the number of detected humans.

        Returns
        -------
        int
        """

        return len(self.human_boxes)