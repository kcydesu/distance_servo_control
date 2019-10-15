import time
import board
import busio
import adafruit_vl6180x
import rospy
from std_msgs.msg import Float32

def distancePub():
    pub = rospy.Publisher('obstacle', Float32, queue_size=10)
    rospy.init_node('distance', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    # Create I2C bus.
    i2c = busio.I2C(board.SCL, board.SDA)
    
    # Create sensor instance.
    sensor = adafruit_vl6180x.VL6180X(i2c)
    
    while not rospy.is_shutdown():
        range_mm = sensor.range
        rospy.loginfo(range_mm)
        pub.publish(range_mm)
        rate.sleep()

if __name__ == '__main__':
    try:
        distancePub()
    except rospy.ROSInterruptException:
        pass