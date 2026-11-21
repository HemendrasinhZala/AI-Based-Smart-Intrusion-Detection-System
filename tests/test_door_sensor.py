from time import sleep

from hardware.door_sensor import DoorSensor

door = DoorSensor()

print("Testing Door Sensor...")
print("Press Ctrl + C to stop.")

try:

    while True:

        if door.is_door_open():

            print("Door OPEN")

        else:

            print("Door CLOSED")

        sleep(1)

except KeyboardInterrupt:

    print("\nStopping Test...")

finally:

    door.cleanup()