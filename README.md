# SAS Kuka Control Template

> [!TIP]
> More information about the SmartArmStack is available in https://smartarmstack.github.io/.

This is a control template for [Universal Robots](https://www.universal-robots.com) robotic manipulators. It relies on [`sas_robot_driver_ur`](https://github.com/MarinhoLab/sas_robot_driver_ur) to communicate
with the robot via [URCL](https://github.com/UniversalRobots/Universal_Robots_Client_Library).

## Docker image

### Simulation

TODO

### Real robot

TODO

### Troubleshooting realtime problems

I have tested the driver with a considerable load in the machine, including CoppeliaSim (part of the example), Firefox, PyCharm, etc. open.
What I have found so far is that the connection is robust, with no interruptions. 

#### Unreliable network profiles

If the wired connection is in the `Connecting` status, it fails randomly, frequently, and fast. This is followed by a `Connection failure` Ubuntu error that pops up.
Although I cannot pinpoint the source of this issue, manually re-applying the settings **temporarily** fixed the issue.

To solve it permanently, in the system admin account, I deleted the wired network profile and redefined it with the correct configuration.
