#!/usr/bin/env python3

import rospy
from rss2_msgsrv_pkg.srv import srv_turtlebot3_move, srv_turtlebot3_moveResponse
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

rospy.init_node('move_server')

def move_callback(request):
    rospy.loginfo("Moving in a circle for 20 seconds...")
    move_circle(20)

    rospy.loginfo("Stopping for 5 seconds...")
    stop(5)

    rospy.loginfo("Moving along the x-axis for 5 seconds...")
    move_x_axis(5)

    rospy.loginfo("Stopping...")
    stop()

    return TriggerResponse(success=True, message="Movement complete")

def move_circle(duration):
    twist_cmd = Twist()
    twist_cmd.linear.x = 0.2
    twist_cmd.angular.z = 0.5

    start_time = rospy.get_time()
    while rospy.get_time() - start_time < duration:
        pub.publish(twist_cmd)
        rate.sleep()

def move_x_axis(duration):
    twist_cmd = Twist()
    twist_cmd.linear.x = 0.2

    start_time = rospy.get_time()
    while rospy.get_time() - start_time < duration:
        pub.publish(twist_cmd)
        rate.sleep()

def stop(duration=None):
    twist_cmd = Twist()
    twist_cmd.linear.x = 0.0
    twist_cmd.angular.z = 0.0

    if duration:
        start_time = rospy.get_time()
        while rospy.get_time() - start_time < duration:
            pub.publish(twist_cmd)
            rate.sleep()
    else:
        pub.publish(twist_cmd)

rospy.Service('/move_duration', srv_turtlebot3_move, move_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(10)

rospy.spin()
