from time import sleep

from hardware.pir_sensor import PIRSensor

pir = PIRSensor()

print("Testing PIR Sensor...")
print("Press Ctrl + C to stop.")

try:

    while True:

        if pir.detect_motion():

            print("Motion Detected")

        else:

            print("No Motion")

        sleep(1)

except KeyboardInterrupt:

    print("\nStopping Test...")

finally:

    pir.cleanup()