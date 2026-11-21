"""
===========================================================
AI Intrusion Detection System
Recorder Test

Author : Hemendrasinh Zala

Tests:
1. Image Capture
2. Video Recording
===========================================================
"""

import time
import cv2

from core.camera import Camera
from core.recorder import Recorder


def main():

    camera = Camera()
    recorder = Recorder()

    camera.start()

    print("=" * 60)
    print("Initializing camera...")
    print("=" * 60)

    # Give camera time to initialize
    time.sleep(2)

    # Discard initial frames (Lenovo logo / unstable frames)
    for _ in range(60):
        success, frame = camera.read_frame()

    print("Camera Ready.")
    print()

    recording_started = False
    start_time = None

    while True:

        success, frame = camera.read_frame()

        if not success:
            print("Failed to read frame.")
            break

        # --------------------------------------------------
        # Start recording automatically
        # --------------------------------------------------

        if not recording_started:

            height, width = frame.shape[:2]

            print("Capturing image...")

            image_path = recorder.capture_image(frame)

            print("Image Saved:", image_path)

            print("Starting video recording...")

            video_path = recorder.start_recording((width, height))

            print("Video Saved:", video_path)

            recording_started = True
            start_time = time.time()

        # --------------------------------------------------
        # Record every frame
        # --------------------------------------------------

        if recorder.is_recording():

            recorder.update(frame)

            cv2.putText(
                frame,
                "RECORDING...",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        cv2.imshow("Recorder Test", frame)

        # --------------------------------------------------
        # Stop automatically after 10 seconds
        # --------------------------------------------------

        if recording_started:

            elapsed = time.time() - start_time

            if elapsed >= 10:

                print("Stopping recording...")

                recorder.stop_recording()

                break

        if cv2.waitKey(1) & 0xFF == ord("q"):

            recorder.stop_recording()

            break

    camera.release()

    cv2.destroyAllWindows()

    print()
    print("=" * 60)
    print("Recorder Test Completed Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()