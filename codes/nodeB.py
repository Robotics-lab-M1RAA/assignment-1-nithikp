#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def call_back(msg):
    rospy.loginfo(msg.data)


def nodeB():
    rospy.init_node('M1RAA 2024', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    rospy.Subscriber('hello_class', String, callback=call_back)
    
    pub1 = rospy.Publisher("welcome",String, queue_size=10)
    msg1 = String()
    msg1.data = "Hello, Nithik Welcome!" 
    
    pub2 = rospy.Publisher("hello_college",String,queue_size=10)
    msg2= String()
    msg2.data = "Hello CET"
    
    while not rospy.is_shutdown():
        pub1.publish(msg1)
        rospy.loginfo(msg1.data)
        rate.sleep()
        
        pub2.publish(msg2)
        rospy.loginfo(msg2.data)
        rate.sleep()

if __name__ == '__main__':
    try:
        nodeB()
    except rospy.ROSInterruptException:
        pass    

   
