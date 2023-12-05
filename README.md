# ftn-axia80
ROS integration for [SCHUNK FTN-AXIA80-DUAL SI-200-8/SI-500-20](https://schunk.com/de/de/automatisierungstechnik/kraft-momenten-sensoren/ft-axia/ftn-axia80-dual-si-200-8/si-500-20/p/000000000001324513) force/torque sensor.


## Prerequisites

## How to setup
Clone the _ftn_axia80_ package into your catkin workspace.  

In _ftn_axia.py_ , set the IP-adress of your gripper. 

Default IP __192.168.1.1__, default port __49151__.

Build and source your workspace.

## How to run
run the sensor node with
```bash
rosrun ftn_axia80 ftn-axia-publisher.py
```
or inside your custom launch file.

## How to use
Inside custom python script
```python
import rospy
from geometry_msgs.msg import Wrench

# get most recent FT-value
wrench = rospy.wait_for_message("/ftn_axia", Wrench)

# get continous stream of values
wrench_client = rospy.Subscriber("/ftn_axia", Wrench, wrench_cb)

def wrench_cb(data):
	read_wrench = data
	# do something

```

## ToDo
- [ ] create launch file with args