import time  
import sys
from servo_pi.servo import Servo
import rospy
from std_msgs.msg import Float32

def callback(data, args):
    dist = data.data
    serv = args[0]
    
    new_pos = ((200 - dist)/200)*180
    
    if new_pos <= 0:
        new_pos = 0
    elif new_pos > 180:
        new_pos = 180
    
    serv.set_position(new_pos)
    
    
    rospy.loginfo(rospy.get_caller_id() + " Distance to obstacle is ", data.data)
    
    
    
def listener(argv):
    serv_pin = argv[0]
    servo = Servo(serv_pin)
    pos = 0
    servo.set_position(pos)
    
    rospy.init_node('servoSub', anonymous=True)

    rospy.Subscriber("obstacle", Float32, callback, (servo))
    rospy.loginfo(rospy.get_caller_id() + "connected to servo on board pin {}".format(serv_pin))
       
    
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener(sys.argv[1:])