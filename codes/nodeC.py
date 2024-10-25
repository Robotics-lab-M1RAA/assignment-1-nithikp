#!/usr/bin/python3

import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(f"recived : {msg.data}")

def nodeC():
    rospy.init_node("CET")
    rospy.Subscriber("hello_college",String,callback=call_back)
    rospy.spin()
    
if __name__ == "__main__" :
    nodeC()