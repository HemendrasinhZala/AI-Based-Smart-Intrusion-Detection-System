import cv2

for index in [0, 1]:
    print(f"\nTesting Camera {index}")

    cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Cannot open")
        continue

    # Skip first 100 frames
    for _ in range(100):
        ret, frame = cap.read()

    ret, frame = cap.read()

    if ret:
        cv2.imshow(f"Camera {index}", frame)

        print("Press any key...")

        cv2.waitKey(0)

    cap.release()
    cv2.destroyAllWindows()