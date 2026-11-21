from core.logger import Logger


def main():

    logger = Logger()

    logger.info("Application started.")

    logger.warning("This is a warning message.")

    logger.error("This is an error message.")

    logger.critical("This is a critical message.")

    logger.log_intrusion(
        event="Human Detected",
        image_path="storage/images/test.jpg",
        video_path="storage/videos/test.mp4"
    )

    print("Logger test completed successfully.")
    print("Check storage/logs/application.log")


if __name__ == "__main__":
    main()