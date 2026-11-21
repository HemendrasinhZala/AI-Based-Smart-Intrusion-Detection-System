"""
===========================================================
AI Intrusion Detection System
Recorder Module

Author : Hemendrasinh Zala

This module is responsible for:
1. Capturing intrusion images.
2. Recording intrusion videos.
===========================================================
"""

import cv2

from config import (
    FPS,
    VIDEO_CODEC,
)

from core.logger import Logger
from core.utils import (
    save_image,
    get_video_filename,
)


class Recorder:
    """
    Handles image capture and video recording.
    """

    def __init__(self):
        """
        Initialize the recorder.
        """

        self.logger = Logger()

        self.video_writer = None

        self.recording = False

        self.video_path = None

        self.image_path = None

    # =======================================================
    # CAPTURE IMAGE
    # =======================================================

    def capture_image(self, frame):
        """
        Capture and save an image from the frame.

        Parameters
        ----------
        frame : numpy.ndarray
            Frame to capture.

        Returns
        -------
        pathlib.Path
            Path of the saved image.
        """

        print("capture_image() called")

        try:

            self.image_path = save_image(frame)

            print("Image path:", self.image_path)

            self.logger.info(f"Image saved: {self.image_path}")

            return self.image_path

        except Exception as error:

            print("Capture Image Error:", error)

            self.logger.error(f"Failed to save image: {error}")

            return None
        
        # =======================================================
    # START RECORDING
    # =======================================================

    def start_recording(self, frame_size):
        """
        Start recording a video.

        Parameters
        ----------
        frame_size : tuple
            Frame size in the format (width, height).

        Returns
        -------
        pathlib.Path
            Path of the video being recorded.
        """

        # Prevent multiple recordings
        if self.recording:
            return self.video_path

        try:

            self.video_path = get_video_filename()
            print("Video path:", self.video_path)

            self.video_writer = cv2.VideoWriter(
                str(self.video_path),
                cv2.VideoWriter_fourcc(*VIDEO_CODEC),
                FPS,
                frame_size
            )
            print("VideoWriter opened:", self.video_writer.isOpened())

            # Verify VideoWriter opened successfully
            if not self.video_writer.isOpened():

                self.logger.error("Unable to create video file.")

                self.video_writer = None

                self.video_path = None

                return None

            self.recording = True

            self.logger.info(
                f"Recording started: {self.video_path}"
            )

            return self.video_path

        except Exception as error:

            self.logger.error(
                f"Failed to start recording: {error}"
            )

            # Do not attempt to save a backup frame here because `frame`
            # is not available in this context. Just log the failure.

            self.video_writer = None
            self.video_path = None
            self.recording = False

            return None

    # =======================================================
    # UPDATE RECORDING
    # =======================================================

    def update(self, frame):
        """
        Write the current frame to the video.

        Parameters
        ----------
        frame : numpy.ndarray
        """

        if not self.recording:
            return

        if self.video_writer is None:
            return

        self.video_writer.write(frame)
        print("Writing frame...")

        # =======================================================
    # STOP RECORDING
    # =======================================================

    def stop_recording(self):
        """
        Stop the current video recording.
        """

        if not self.recording:
            return

        try:

            if self.video_writer is not None:

                self.video_writer.release()

                self.video_writer = None

            self.recording = False

            self.logger.info(
                f"Recording stopped: {self.video_path}"
            )

        except Exception as error:

            self.logger.error(
                f"Failed to stop recording: {error}"
            )

    # =======================================================
    # RECORDING STATUS
    # =======================================================

    def is_recording(self):
        """
        Check whether recording is currently active.

        Returns
        -------
        bool
        """

        return self.recording