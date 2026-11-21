"""
===========================================================
AI Intrusion Detection System
Configuration File

Author : Hemendrasinh Zala

This file contains all configurable settings used
throughout the project.
===========================================================
"""

from pathlib import Path
import cv2

# ===========================================================
# PROJECT PATHS
# ===========================================================

BASE_DIR = Path(__file__).resolve().parent

MODELS_DIR = BASE_DIR / "models"

STORAGE_DIR = BASE_DIR / "storage"

IMAGE_DIR = STORAGE_DIR / "images"

VIDEO_DIR = STORAGE_DIR / "videos"

LOG_DIR = STORAGE_DIR / "logs"

ASSETS_DIR = BASE_DIR / "assets"

# ===========================================================
# AI MODEL
# ===========================================================

YOLO_MODEL = MODELS_DIR / "yolov8n.pt"

CONFIDENCE_THRESHOLD = 0.50

# ===========================================================
# CAMERA SETTINGS
# ===========================================================

CAMERA_INDEX = 0      # USB webcam
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30

# ===========================================================
# MOTION DETECTION
# ===========================================================

MIN_CONTOUR_AREA = 1200

BLUR_KERNEL_SIZE = (21, 21)

# ===========================================================
# RECORDING SETTINGS
# ===========================================================

VIDEO_CODEC = "XVID"

VIDEO_DURATION = 15      # Seconds

VIDEO_FORMAT = ".avi"

IMAGE_FORMAT = ".jpg"

# ===========================================================
# STORAGE SETTINGS
# ===========================================================

SAVE_IMAGES = True

SAVE_VIDEOS = True

# ===========================================================
# LOGGING
# ===========================================================

LOG_FILE = LOG_DIR / "application.log"

# ===========================================================
# ALARM
# ===========================================================

ALARM_SOUND = ASSETS_DIR / "alarm.wav"

# ===========================================================
# RASPBERRY PI GPIO
# (Used later during hardware integration)
# ===========================================================

ENABLE_GPIO = False

PIR_PIN = 17

DOOR_SENSOR_PIN = 27

LED_PIN = 22

BUZZER_PIN = 18

# ===========================================================
# DISPLAY SETTINGS
# ===========================================================

WINDOW_NAME = "AI Intrusion Detection System"

SHOW_FPS = True

SHOW_DATE_TIME = True

SHOW_STATUS = True

# ===========================================================
# COLORS (OpenCV uses BGR)
# ===========================================================

COLOR_RED = (0, 0, 255)

COLOR_GREEN = (0, 255, 0)

COLOR_BLUE = (255, 0, 0)

COLOR_YELLOW = (0, 255, 255)

COLOR_WHITE = (255, 255, 255)

# ===========================================================
# TEXT SETTINGS
# ===========================================================

FONT = cv2.FONT_HERSHEY_SIMPLEX

FONT_SCALE = 0.7

FONT_THICKNESS = 2

# Threat Level Colors (OpenCV uses BGR)

THREAT_LOW_COLOR = (0, 255, 0)       # Green
THREAT_MEDIUM_COLOR = (0, 255, 255)  # Yellow
THREAT_HIGH_COLOR = (0, 0, 255)      # Red

# ==========================================================
# PIR SENSOR
# ==========================================================

PIR_PIN = 17

# ==========================================================
# DOOR SENSOR
# ==========================================================

DOOR_SENSOR_PIN = 27

# ==========================================================
# HARDWARE BUZZER
# ==========================================================

BUZZER_PIN = 22

# ==========================================================
# STATUS LED PINS
# ==========================================================

GREEN_LED_PIN = 5

YELLOW_LED_PIN = 6

RED_LED_PIN = 13