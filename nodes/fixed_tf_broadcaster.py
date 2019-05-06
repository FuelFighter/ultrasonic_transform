#!/usr/bin/env python  
import roslib
roslib.load_manifest('learning_tf')

import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('ultrasonic_transform_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        
        br.sendTransform((0.0, 0.0, 0.0),
                         tf.transformations.quaternion_from_euler(0, 0, -45),
                         rospy.Time.now(),
                         "ultrasound/right",
                         "ultrasound/center")
        br.sendTransform((0.0, 0.0, 0.0),
                         tf.transformations.quaternion_from_euler(0, 0, 45),
                         rospy.Time.now(),
                         "ultrasound/left",
                         "ultrasound/center")
        rate.sleep()
