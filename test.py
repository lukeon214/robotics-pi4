from adafruit_servokit import ServoKit
import time
from sshkeyboard import listen_keyboard

kit = ServoKit(channels=16)

def on_key_press(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 0.5
    if key == "d":
        kit.continuous_servo[0].throttle = -0.5

def on_key_release(key):
    if key == "a":
        kit.continuous_servo[0].throttle = 0.0
    if key == "d":
        kit.continuous_servo[0].throttle = 0.0

listen_keyboard(
    on_release=on_key_release,
    on_press=on_key_press
)