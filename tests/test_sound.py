import time

from core.sound import Sound


def main():

    sound = Sound()

    print("Starting alarm for 5 seconds...")

    sound.play_alarm()

    time.sleep(5)

    sound.stop_alarm()

    print("Alarm stopped successfully.")

    print("Alarm Playing:", sound.is_playing())


if __name__ == "__main__":
    main()