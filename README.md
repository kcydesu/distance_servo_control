# Before Using
Using this rospackage depends on many other packages, and they must be met before installing and using.

This guide assumes that you have already created a catkin workspace and installed ROS. For a guide on installing ROS on your machine, check [here](http://wiki.ros.org/ROS/Installation) and to learn how to create a catkin workspace check [here](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

This package also depends on the following packages that can be installed by following their respective installation directions:

* [Adafruit CircuitPython for VL6180X](https://github.com/adafruit/adafruit_circuitpython_vl6180x)
* [My Servo Control Package](https://github.com/kcydesu/servo-pi)

# Package Creation
The first step in creating your rospackage is to create the package and its core dependencies.
```
cd ~/catkin_ws
catkin_create_pkg <package_name> std_msgs rospy roscpp
catkin_make
. ~/catkin_ws/devel/setup.bash
source /opt/ros/%YOUR_ROS_DISTRO%/setup.bash
```

At this point, if you want to, you can follow the [ROS Wiki](http://wiki.ros.org/ROS/Tutorials/CreatingPackage) and customize the package further, however this is the base of what we need to start adding our publisher and subscriber.

In order to add the publisher and subscriber to the package we first need to get into out package: 
```cd ~/catkin_ws/src/<package_name>```

Check the folder to see if there is a ```/src``` folder, and if not, create it. This folder is where we will put all of out python code that will actually act as our ros nodes.

Run the following set of commands to copy the files from this repository into your catkin workspace:
```
cd src
wget https://raw.githubusercontent.com/kcydesu/distance_serve_control/master/src/distPublisher.py
wget https://raw.githubusercontent.com/kcydesu/distance_serve_control/master/src/servoSub.py
cd ~/catkin_ws
catkin_make
. ~/catkin_ws/devel/setup.bash
source /opt/ros/%YOUR_ROS_DISTRO%/setup.bash
```

After running these commands, you should be ready to use this package.

# Running the Package
## Hardware
There are two hardware components to set up and both are actually rather easy to get connected. First is the servo



## Software
In order to corretly us this package you need atleast three terminals. In each one you should specify the ROS_MASTER_URI and ROS_IP.
```
cd ~/catkin_ws
export ROS_MASTER_URI=http://<your_ip>:11311
esport ROS_IP=<your_ip>
```
In the first terminal, you should start the roscore using the ```roscore``` command.

In the next terminal we will start the subscriber that will start the servo. We can do this using rosrun as follows:
```
rosrun <package_name> servoSub.py <pwm_pin>
```
where <pwm_pin> is the Pulse-Width Modulated pin that you connected your servo to above.

In the final terminal, we will initiate the publisher that will publish the information from the distance sensor, which will be read by our subscriber and control the servo.
```
rosrun <package_name> distPublisher.py
```
