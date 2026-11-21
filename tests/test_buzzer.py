from time import sleep

from hardware.buzzer import Buzzer

buzzer = Buzzer()

print("Testing Hardware Buzzer...")

try:

    buzzer.turn_on()

    print("Buzzer ON")

    sleep(5)

    buzzer.turn_off()

    print("Buzzer OFF")

finally:

    buzzer.cleanup()