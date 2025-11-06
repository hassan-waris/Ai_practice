#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class PubSub:
    def __init__(self):
        rospy.init_node('hassanwaris_pubsub')
        self.subscriber = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        self.publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.distance_to_run = 5.0  # Specify the distance for the robot to run
        self.current_distance = 0.0
        self.is_running = False

    def odom_callback(self, odom):
        if self.is_running:
            self.current_distance = odom.pose.pose.position.x
            if self.current_distance >= self.distance_to_run:
                self.stop_robot()

    def move_robot(self, linear_speed):
        twist = Twist()
        twist.linear.x = linear_speed
        self.publisher.publish(twist)
        self.is_running = True

    def stop_robot(self):
        twist = Twist()
        twist.linear.x = 0.0
        self.publisher.publish(twist)
        self.is_running = False

if __name__ == '__main__':
    try:
        pubsub = PubSub()
        pubsub.move_robot(0.5)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass

