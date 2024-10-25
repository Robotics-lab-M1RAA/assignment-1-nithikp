#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo(f"recived : {msg.data}")

def subscriber1():
    rospy.init_node("RAA24_subnode")
    rospy.Subscriber("Greetings",String,callback)
    rospy.spin()
    
if __name__ == "__main__" :
    subscriber1()