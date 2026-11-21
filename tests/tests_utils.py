"""
Test file for core/utils.py


Author : Hemendrasinh Zala
"""

from core.utils import (
    create_directories,
    get_timestamp,
    get_current_datetime,
    get_image_filename,
    get_video_filename,
    file_exists,
    format_elapsed_time,
)

from config import (
    IMAGE_DIR,
    VIDEO_DIR,
    LOG_DIR,
)


def main():

    print("=" * 60)
    print("Testing core/utils.py")
    print("=" * 60)

    # -------------------------------------------------
    # Create directories
    # -------------------------------------------------

    print("\nCreating project directories...")

    create_directories()

    print("✓ Directories created successfully.")

    # -------------------------------------------------
    # Timestamp
    # -------------------------------------------------

    print("\nTimestamp:")

    print(get_timestamp())

    # -------------------------------------------------
    # Current Date & Time
    # -------------------------------------------------

    print("\nCurrent Date & Time:")

    print(get_current_datetime())

    # -------------------------------------------------
    # Image Filename
    # -------------------------------------------------

    image_file = get_image_filename()

    print("\nGenerated Image Filename:")

    print(image_file)

    # -------------------------------------------------
    # Video Filename
    # -------------------------------------------------

    video_file = get_video_filename()

    print("\nGenerated Video Filename:")

    print(video_file)

    # -------------------------------------------------
    # File Exists
    # -------------------------------------------------

    print("\nChecking if generated image exists:")

    print(file_exists(image_file))

    # -------------------------------------------------
    # Time Formatting
    # -------------------------------------------------

    print("\nFormatted Time:")

    print(format_elapsed_time(3661))

    # -------------------------------------------------
    # Directory Check
    # -------------------------------------------------

    print("\nDirectory Status")

    print("Images :", IMAGE_DIR.exists())
    print("Videos :", VIDEO_DIR.exists())
    print("Logs   :", LOG_DIR.exists())

    print("\nAll utility tests completed successfully.")


if __name__ == "__main__":
    main()