# Abel
## Design and implementation of a bio-inspired motor control system for social humanoid robot

The focus has been on creating a software control architecture based on the middleware ROS (Robot Operating System) and achieve a human-like movement for the arms and the neck.

![immagine](https://user-images.githubusercontent.com/36999962/156939619-47e46bb2-c957-4bee-82b8-63a6713d4c47.png)

## Bioinspired Cognitive Architecture: SEAI
Abel is based on a bio-inspired cognitive architecture called SEAI (Social Emotional Artificial Intelligence) that follows a hybrid (reactive/deliberative) paradigm:
![image](https://user-images.githubusercontent.com/36999962/164400467-7a6b26fe-b094-494a-a93f-ec0d6b12b9dc.png)

## Dynamixel_Workbench
Dynamixel_Workbench is the meta-package for ROS which include the controller for dynamixel motors. It provides the interface with the low-level hardware, and it creates the topics needed to send positions to the servos (i.e., the trajectories generated for the joints).

See [here](http://wiki.ros.org/dynamixel_workbench_controllers) for additional details.

## Software Architecture
Each directory is a ROS package and you need to install dependencies for dynamixel motor control.
![ACT-BODY-NEW drawio](https://user-images.githubusercontent.com/36999962/164402666-9f74fe73-1312-450f-8bf4-4b5fc9c89621.png)


### Abel_bringup
Abel_bringup handles launch files for other packages and calls the dynamixel controller.

### Abel_control
Abel_control is the main module for arms and neck control. It includes all the python classes and methods necessary for the realization of gestures and  for joints configuration. A static gestures dictionary and the head orientation control function are included in the latter package.

### Abel_moveit
Abel_moveit_config is responsible for inverse kinematics and trajectory planning with self-collisions avoidance (MoveIt Setup Assistant).

### Abel_description
Finally, abel_description is the package that conventionally collects all the files such as meshes or URDF for the description of the robot.





