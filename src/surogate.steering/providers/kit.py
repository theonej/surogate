from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16)

increment = 10

def set_angle(angle, servo_index):
    steering_servo = kit.servo[servo_index]
    steering_servo.angle = angle
    
def turn(amount, steering_servo):
    modified = False

    print(steering_servo.angle)
    angle = steering_servo.angle + amount
    if(angle >= 0 and angle <= 180):
        print("turning")
        steering_servo.angle = angle
        modified = True
        time.sleep(1)

    return modified

def right(servo_index):
    print("turning right")
    steering_servo = kit.servo[servo_index]
    return turn(increment, steering_servo)

def left(servo_index):
    print("turning left")
    steering_servo = kit.servo[servo_index]
    return turn(increment * -1, steering_servo)