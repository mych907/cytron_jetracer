#!/usr/bin/env python3

import rospy
from jetracer.nvidia_racecar import NvidiaRacecar
from std_msgs.msg import Float32
from std_msgs.msg import Empty

import time
import numpy as np

#Initialize car variable and tune settings
car = NvidiaRacecar()
car.steering_gain = -0.75
car.steering_offset = 0.12
car.throttle_gain = -0.5
car.steering = 0.0

#Throttle
def throttle(throt):
    car.throttle = throt
    rospy.loginfo("Throttle: %s", str(throt))

#Steering
def callback_steering(steer):
    steer_mapped = (steer.data*180/np.pi + 2.2)/19
    if steer_mapped > 1:
        car.steering = 1
    elif steer_mapped < -1:
        car.steering = -1
    else:
        car.steering = steer_mapped
    rospy.loginfo("Steering: %s", str(steer_mapped))

def steering(steer):
    car.steering = steer
    rospy.loginfo("Steering: %s", str(steer))


#Setup node and topics subscription
def callback_racecar(data):

    rate = rospy.Rate(20)


    steering(1)
    rospy.sleep(1)
    steering(0.0)
    rospy.sleep(2)

    ti = time.time()
    rospy.Subscriber("steering_angle", Float32, callback_steering)
    throttle(0.001)
    while time.time() - ti < 7:
        rospy.sleep(0.01)

    throttle(-1)

def racecar():
    rospy.init_node('racecar', anonymous=True, disable_signals=True)
    rospy.Subscriber("start", Empty, callback_racecar)
    rospy.spin()


if __name__ == '__main__':
    print("Running MY_run.py")
    racecar()
