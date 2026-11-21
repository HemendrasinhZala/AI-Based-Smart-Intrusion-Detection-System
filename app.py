"""
===========================================================
AI Intrusion Detection System

Main Application

Author : Hemendrasinh Zala
===========================================================
"""

import time
import cv2

from config import (
    WINDOW_NAME,
    FONT,
    FONT_SCALE,
    FONT_THICKNESS,
    COLOR_GREEN,
    COLOR_RED,
    THREAT_LOW_COLOR,
    THREAT_MEDIUM_COLOR,
    THREAT_HIGH_COLOR,
)

from core.camera import Camera
from core.intrusion_detector import IntrusionDetector


# ===========================================================
# MAIN APPLICATION
# ===========================================================

def main():
    """
    Main Application.
    """

    print("=" * 60)
    print("AI Intrusion Detection System")
    print("=" * 60)

    camera = Camera()

    detector = IntrusionDetector()

    camera.start()

    print("Initializing camera...")

    time.sleep(2)

    # Discard warm-up frames
    for _ in range(60):

        success, frame = camera.read_frame()

        if not success:

            print("Unable to initialize camera.")

            camera.release()

            return

    print("Camera Ready.")
    print()

    print("Keyboard Controls")
    print("-------------------------------")
    print("A -> Arm System")
    print("D -> Disarm System")
    print("Q -> Quit")
    print("=" * 60)

    # -------------------------------------------------------
    # Main Loop
    # -------------------------------------------------------

    while True:

        # Read frame
        success, frame = camera.read_frame()

        if not success:

            print("Failed to read frame from camera.")

            break

        # Process frame
        frame = detector.process_frame(frame)

        # Update detector
        detector.update()

        # ---------------------------------------------------
        # System Status
        # ---------------------------------------------------

        if detector.is_system_armed():

            system_status = "SYSTEM : ARMED"

            system_color = COLOR_RED

        else:

            system_status = "SYSTEM : DISARMED"

            system_color = COLOR_GREEN

        cv2.putText(

            frame,

            system_status,

            (20, 40),

            FONT,

            FONT_SCALE,

            system_color,

            FONT_THICKNESS

        )

        # ---------------------------------------------------
        # Intrusion Status
        # ---------------------------------------------------

        if detector.is_intrusion_detected():

            intrusion_status = "INTRUSION : DETECTED"

            intrusion_color = COLOR_RED

        else:

            intrusion_status = "INTRUSION : SAFE"

            intrusion_color = COLOR_GREEN

        cv2.putText(

            frame,

            intrusion_status,

            (20, 80),

            FONT,

            FONT_SCALE,

            intrusion_color,

            FONT_THICKNESS

        )

        # ---------------------------------------------------
        # Threat Score
        # ---------------------------------------------------

        score = detector.get_threat_score()

        cv2.putText(

            frame,

            f"Threat Score : {score}",

            (20, 120),

            FONT,

            FONT_SCALE,

            COLOR_GREEN,

            FONT_THICKNESS

        )

        # ---------------------------------------------------
# Threat Level
# ---------------------------------------------------

        level = detector.get_threat_level()

        if level == "LOW":

         level_color = THREAT_LOW_COLOR

        elif level == "MEDIUM":

         level_color = THREAT_MEDIUM_COLOR

        else:

         level_color = THREAT_HIGH_COLOR

        cv2.putText(

        frame,

        f"Threat Level : {level}",

        (20, 160),

        FONT,

        FONT_SCALE,

        level_color,

        FONT_THICKNESS

)
        # ---------------------------------------------------
        # Display Live Feed
        # ---------------------------------------------------

        cv2.imshow(

            WINDOW_NAME,

            frame

        )

        # ---------------------------------------------------
        # Keyboard Controls
        # ---------------------------------------------------

        key = cv2.waitKey(1) & 0xFF

        if key != 255:
         print("Key Pressed:", key, chr(key))

        if key == ord("a"):

            detector.arm_system()

            print("System Armed")

        elif key == ord("d"):

            detector.disarm_system()

            print("System Disarmed")

        elif key == ord("q"):

            print("Closing Application...")

            break

        # -------------------------------------------------------
    # Cleanup
    # -------------------------------------------------------

    print()

    print("Cleaning up resources...")

    detector.cleanup()

    camera.release()

    cv2.destroyAllWindows()

    print()

    print("=" * 60)
    print("AI Intrusion Detection System Closed Successfully.")
    print("=" * 60)


# ===========================================================
# ENTRY POINT
# ===========================================================

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        print()

        print("Application interrupted by user.")

    except Exception as error:

        print()

        print(f"Unexpected Error : {error}")

    finally:

        cv2.destroyAllWindows()


        #python3 -m venv --system-site-packages .venv