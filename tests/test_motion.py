import cv2

from core.camera import Camera
from core.motion_detector import MotionDetector


def main():

    camera = Camera()
    detector = MotionDetector()

    camera.start()

    print("Motion Detector Test Started")
    print("Move in front of the webcam.")
    print("Press 'Q' to quit.")

    while True:

        success, frame = camera.read_frame()

        if not success:
            break

        motion = detector.detect_motion(frame)

        if motion:
            detector.draw_motion_boxes(frame)

        cv2.imshow("Motion Detection Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()