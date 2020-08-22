#!/usr/bin/env python
# license removed for brevity
import rospy
import pwm as pwm
from std_msgs.msg import String

def driving ():
    rospy.init_node('driving', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo(hello_str)
        rate.sleep()

def listner ():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("PLEASE_CHANGE_THIS", String, callback)
    rospy.spin()

if __name__ == '__main__':
    pwm.setPin(12)
    try:
        listener()
        talker()
    except rospy.ROSInterruptException:
        pass