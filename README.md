# SAS Kuka Control Template

> [!TIP]
> Repository for this template: https://github.com/MarinhoLab/sas_kuka_control_template \
> More information about SmartArmStack is available in https://smartarmstack.github.io/.

This is a control template for [KUKA](https://www.kuka.com/en-gb/products/robotics-systems) robotic manipulators. It relies on [`sas_robot_driver_kuka`](https://github.com/MarinhoLab/sas_robot_driver_kuka) to communicate
with the robot via [Sunrise.FRI](https://my.kuka.com/s/category/software/system-software-extension/kuka-sunrise-extensions/kuka-sunrisefri/0ZG1i000000XapDGAS?language=en_US).

## Docker

### Simulation

https://github.com/user-attachments/assets/d0c00b59-8b45-4c11-9c85-6ec9807eda97

![](./sas_kct_simulation.mp4)

Run

```commandline
mkdir -p ~/sas_tutorial_workspace/docker/kuka_control_template/simulation_demo
cd ~/sas_tutorial_workspace/docker/kuka_control_template/simulation_demo
curl -OL https://raw.githubusercontent.com/MarinhoLab/sas_kuka_control_template/refs/heads/main/.devel/simulation_demo/compose.yml

xhost +local:root
docker compose up
```

### Real robot

> [!CAUTION]
> For using the real robot, you **must** have the risk assessments in place. 
> This guide is meant to be helpful but holds absolutely no liability whatsoever. More details are available in the software license.

> [!WARNING]
> This code will move the robot. Be sure that the workspace is free and safe for operation.
> Be sure that the robot is in a joint configuration in which it will not hit itself or anything around it. 

https://github.com/user-attachments/assets/8340a929-487e-4ed7-b256-809f769bc446

![](./sas_kct_realrobot.mp4)

Run

```commandline
mkdir -p ~/sas_tutorial_workspace/docker/kuka_control_template/robot_demo
cd ~/sas_tutorial_workspace/docker/kuka_control_template/robot_demo
curl -OL https://raw.githubusercontent.com/MarinhoLab/sas_kuka_control_template/refs/heads/main/.devel/robot_demo/compose.yml

docker compose up
```

> [!IMPORTANT]
> The Sunrise Cabinet has a number of steps necessary for the robot to be operable in automatic mode. \
> Refer to the vendor for complete instructions. 

> [!IMPORTANT]
> This [App](https://github.com/MarinhoLab/sas_robot_driver_kuka/blob/main/teaching_pendant_app/MM_FRI_RobotApp.java) must be running in the Sunrise Cabinet.

