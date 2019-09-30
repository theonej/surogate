from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)
steering_servo = kit.servo[0]

increment = 5

def turn(amount):
    modified = False

    angle = steering_servo.angle + amount
    if(angle >= 0 and angle <= 180):
        steering_servo.angle = angle
        modified = True
        time.sleep(1)

    return modified

def right():
    return turn(increment)

def left():
    return turn(increment * -1)