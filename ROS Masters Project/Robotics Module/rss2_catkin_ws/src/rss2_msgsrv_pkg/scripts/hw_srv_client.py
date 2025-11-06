#! /usr/bin/env python3
import rospy

# Notice the difference with the server?
from rss2_msgsrv_pkg.srv import srv_turtlebot3_move, srv_turtlebot3_moveRequest

# The service client node
rospy.init_node ('turtlebot_move_client ')

# Wait for the service ›/turtlebot_move_service' to run
# You need to start the service first
rospy.wait_for_service ('/turtlebot_move_service')

# # Connect to the service '/turtlebot_move_service
# turtlebot_service_client = rospy.ServiceProxy('/turtlebot_move_service', srv_turtlebot3_move)

# # Create a request instance
# turtlebot_request_instance = srv_turtlebot3_moveRequest()

# turtlebot_request_instance.duration = 30

# # Send the request to the server through connection built
# feedback = turtlebot_service_client(turtlebot_request_instance)

# # Show resuls after the service being called
# rospy.loginfo(str(feedback))

# rospy.loginfo('End of service call ')

try:
    rospy.loginfo("Requesting Turtlebot3 to move for 30 seconds...")
    response =  srv_turtlebot3_moveRequest(30.0) 
    if response.success:
        rospy.loginfo("Turtlebot3 movement complete")
    else:
        rospy.loginfo("Turtlebot3 movement failed")
except rospy.ServiceException as e:
    rospy.loginfo("Service call failed: " + str(e))