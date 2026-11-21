from time import sleep

from hardware.led import LED

led = LED()

try:

    print("LOW")
    led.show_low()
    sleep(3)

    print("MEDIUM")
    led.show_medium()
    sleep(3)

    print("HIGH")
    led.show_high()
    sleep(3)

    led.turn_off_all()

finally:

    led.cleanup()