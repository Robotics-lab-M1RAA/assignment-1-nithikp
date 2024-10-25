#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(msg.data)

def nodeA():
    rospy.init_node('nithik', anonymous=True)
    rospy.Subscriber("welcome",String,callback=call_back)
    pub = rospy.Publisher('hello_class', String, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        msg = String()
        msg.data = "Hello RAA 24_26" 
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        nodeA()
    except rospy.ROSInterruptException:
        pass
