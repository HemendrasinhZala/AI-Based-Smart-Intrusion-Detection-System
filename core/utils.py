"""
===========================================================
AI Intrusion Detection System
Utility Functions
Author : Hemendrasinh Zala
===========================================================
"""

from pathlib import Path
from datetime import datetime
import os
import cv2

from config import (
    IMAGE_DIR,
    VIDEO_DIR,
    IMAGE_FORMAT,
    VIDEO_FORMAT,
)


# ===========================================================
# CREATE DIRECTORIES
# ===========================================================

def create_directories():
    """
    Create storage directories if they do not exist.
    """

    os.makedirs(IMAGE_DIR, exist_ok=True)
    os.makedirs(VIDEO_DIR, exist_ok=True)


# ===========================================================
# CURRENT TIMESTAMP
# ===========================================================

def get_timestamp():
    """
    Return current timestamp.

    Example:
    20260707_153015
    """

    return datetime.now().strftime("%Y%m%d_%H%M%S")


# ===========================================================
# IMAGE FILENAME
# ===========================================================

def get_image_filename():
    """
    Generate a unique image filename.
    """

    create_directories()

    filename = f"intrusion_{get_timestamp()}{IMAGE_FORMAT}"

    return IMAGE_DIR / filename


# ===========================================================
# VIDEO FILENAME
# ===========================================================

def get_video_filename():
    """
    Generate a unique video filename.
    """

    create_directories()

    filename = f"intrusion_{get_timestamp()}{VIDEO_FORMAT}"

    return VIDEO_DIR / filename


# ===========================================================
# SAVE IMAGE
# ===========================================================

def save_image(frame):
    """
    Save image to disk.
    """

    create_directories()

    image_path = get_image_filename()

    print("=" * 60)
    print("save_image() called")
    print("Saving image to:", image_path)

    if frame is None:
        print("ERROR: Frame is None")
        raise Exception("Frame is None")

    print("Frame shape:", frame.shape)
    print("Frame dtype:", frame.dtype)

    success = cv2.imwrite(str(image_path), frame)

    print("cv2.imwrite() returned:", success)

    if not success:
        raise Exception("OpenCV failed to save the image.")

    print("Image saved successfully.")
    print("=" * 60)

    return image_path