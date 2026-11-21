import cv2

from core.camera import Camera
from core.human_detector import HumanDetector


def main():

    camera = Camera()
    detector = HumanDetector()

    camera.start()

    print("Human Detector Test Started")
    print("Stand in front of the webcam.")
    print("Press 'Q' to quit.")

    while True:

        success, frame = camera.read_frame()

        if not success:
            break

        human_detected = detector.detect_humans(frame)

        if human_detected:
            detector.draw_detections(frame)

        cv2.imshow("Human Detection Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()