#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from sensor_msgs.msg import LaserScan
from math import atan2
import numpy as np

x = 0.0
y = 0.0
theta = 0.0
angle_error = 0.0
obstacle_detected = False
charging_dock = (1, -3)
goal = Point()  # Initialize the goal variable globally

def newOdom(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])

def liDar_callback(data):
    global obstacle_detected
    global speed

    # Expanded the range for obstacle detection
    front_ranges = data.ranges[140:220]  
    if any(distance < 0.4 for distance in front_ranges):
        obstacle_detected = True
        speed.linear.x = -0.6
        speed.angular.z = 0.2
        pub.publish(speed)
    else:
        obstacle_detected = False

rospy.init_node("speed_controller")
lidar_sub = rospy.Subscriber("/scan", LaserScan, liDar_callback)
sub = rospy.Subscriber("/odom", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
speed = Twist()
r = rospy.Rate(4)
path_list = [(8, 4), (6, 7), (-8, 3), (4, 2), (0, -1), (-2, -4), charging_dock]
point_index = 0

while not rospy.is_shutdown():
    if obstacle_detected:
        # If an obstacle is detected, just continue with the loop and avoid publishing any other commands
        continue

    if point_index < len(path_list):
        goal.x = path_list[point_index][0]
        goal.y = path_list[point_index][1]
    else:
        break

    inc_x = goal.x - x
    inc_y = goal.y - y

    angle_to_goal = atan2(inc_y, inc_x)
    distance_to_goal = np.sqrt(goal.x * goal.x + goal.y * goal.y)
    to_distance_to_goal = np.sqrt(inc_x * inc_x + inc_y * inc_y)

    if to_distance_to_goal >= 0.1:
        angle_error = angle_to_goal - theta
        while angle_error > np.pi:
            angle_error -= 2 * np.pi
        while angle_error < -np.pi:
            angle_error += 2 * np.pi

        if abs(angle_error) > 0.5:
            speed.linear.x = 0.0
            speed.angular.z = 0.5 * np.sign(angle_error)
        else:
            k_p = 0.5
            speed.linear.x = 0.8
            speed.angular.z = k_p * angle_error

        pub.publish(speed)
    else:
        point_index += 1
    r.sleep()
