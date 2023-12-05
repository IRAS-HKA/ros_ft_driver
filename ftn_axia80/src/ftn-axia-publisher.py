#!/usr/bin/env python3
# license removed for brevity
import rospy
import sys
from ftn_axia import FtnAxia
from geometry_msgs.msg import Wrench


def talker():
    pub = rospy.Publisher('ftn_axia', Wrench, queue_size=10)
    rospy.init_node('ftn_axia', anonymous=True)
    rate = rospy.Rate(1000)     # 1 kHz

    mySensor = FtnAxia()

    while not rospy.is_shutdown():
        mySensor.read_ft()

        myWrench = Wrench()
        myWrench.force.x = mySensor.Wrench[0]
        myWrench.force.y = mySensor.Wrench[1]
        myWrench.force.z = mySensor.Wrench[2]

        myWrench.torque.x = mySensor.Wrench[3]
        myWrench.torque.y = mySensor.Wrench[4]
        myWrench.torque.z = mySensor.Wrench[5]

        # muss man nicht unbedingt loggen
        rospy.loginfo(myWrench)

        pub.publish(myWrench)

        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass