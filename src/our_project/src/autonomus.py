#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Int32MultiArray

cx = 0
cy = 0
targetx = 0
targety = 0

def coordinates_callback(msg):
    global cx, cy
    rospy.loginfo("Received integers: %d, %d", msg.data[0], msg.data[1])
    cx = msg.data[0]
    cy = msg.data[1]

def get_target_coordinates():
    global targetx, targety
    

def main():
    global cx, cy, targetx, targety
    rospy.loginfo("<<<<<<<<<Enter  target x coordinate:")
    targetx = int(input())
    rospy.loginfo("<<<<<<<<<<Enter  target y coordinate:")
    targety = int(input())
    
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
    sub = rospy.Subscriber('detected_coordinates', Int32MultiArray, coordinates_callback)

    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        rospy.loginfo("Current coordinates: (%d, %d)", cx, cy)
        get_target_coordinates()

        twist = Twist()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.angular.z = 0
        while True:
            # if cx==targetx and cy==targety:
            #     x=0
            #     y=0
            #     z=0
            #     th=0
            #     print("<<<<<<<<<<<<reached Target>>>>>>>>>>")
            if cx in range(targetx-2, targetx+3) and cy in range(targety-2, targety+3):
                 x = 0
                 y = 0
                 z = 0
                 th = 0
                 print("STOP")
                 for i in range(290):
                     x = 0
                     y = 0
                     z = 0
                     th = 0
                     print("in while")
                 
                 break
            elif cx==targetx and cy==targety:
                 x=0
                 y=0
                 z=0
                 th=0
                 print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                 break
            elif cy > targety + 1:
                x=1
                y=0
                z=0
                th=0
                print("greater than 290")
            elif cy < targety - 1:
                x=-1
                y=0
                z=0
                th=0
                print("forward")
            elif cx > targetx + 1:
                x=0
                y=1
                z=0
                th=0
                print("cx greater than 290")
            elif cx < targetx - 1:
                x=0
                y=-1
                z=0
                th=0
                print("cx ")
            
            else:
                x=0
                y=0
                z=0
                th=0
                print("reached Target")
                break
            twist.linear.x = x * 1
            twist.linear.y = y*1
            twist.linear.z = z*1

            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = th * 1

            pub.publish(twist)
            rate.sleep()
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        rospy.loginfo("Reached target")
        
        rospy.loginfo("Reached target coordinates. Waiting for new target...")

        
        rate.sleep()
        
        

if __name__ == '__main__':
    try:
        rospy.init_node('teleop')
        main()
    except rospy.ROSInterruptException:
        pass