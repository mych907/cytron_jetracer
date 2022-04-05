#!/usr/bin/env python3

import rospy
from jetracer.nvidia_racecar import NvidiaRacecar
from std_msgs.msg import Float32

import time

#Initialize car variable and tune settings
car = NvidiaRacecar()
car.steering_gain = 0.5
car.steering_offset = 0
car.throttle_gain = -0.5
car.steering = 0.0
car.throttle = -1

#Throttle
def throttle(throt):
    car.throttle = throt
    rospy.loginfo("Throttle: %s", str(throt))

#Steering
def callback_steering(steer):
    car.steering = steer.data
    rospy.loginfo("Steering: %s", str(steer.data))

def steering(steer):
    car.steering = steer
    rospy.loginfo("Steering: %s", str(steer))


#Setup node and topics subscription
def racecar():
    throttle(-1)


if __name__ == '__main__':
    print("Running shutdown.py")
    racecar()
