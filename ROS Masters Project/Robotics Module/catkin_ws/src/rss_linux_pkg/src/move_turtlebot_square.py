#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

class MoveTurtleBot():
    def __init__(self):
        self.turtlebot_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.cmd = Twist()

    def move_forward(self, distance, linear_speed):
        duration = distance / linear_speed
        self.cmd.linear.x = linear_speed
        self.cmd.angular.z = 0.0
        self.turtlebot_vel_publisher.publish(self.cmd)
        rospy.sleep(duration)

    def rotate(self, angle, angular_speed):
        duration = abs(angle / angular_speed)

        # Set angular velocity
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = angular_speed

        # Publish the command
        self.turtlebot_vel_publisher.publish(self.cmd)

        # Sleep for the specified duration
        rospy.sleep(duration)

    def move_in_square(self, side_length, linear_speed):
        for _ in range(5):
            # Move forward
            self.move_forward(side_length, linear_speed)

            # Rotate 90 degrees
            self.rotate(1.57, 0.5) #turn 90 degrees

        # Stop at the end
        self.cmd.linear.x = 0.0
        self.cmd.angular.z = 0.0
        self.turtlebot_vel_publisher.publish(self.cmd)

if __name__ == '__main__':
    rospy.init_node('move_turtlebot_sqaure', anonymous=True)
    try:
        turtlebot = MoveTurtleBot()
        side_length = 1.0
        linear_speed = 0.2  # Adjust the linear speed of the robot

        turtlebot.move_in_square(side_length, linear_speed)
    except rospy.ROSInterruptException:
        pass

