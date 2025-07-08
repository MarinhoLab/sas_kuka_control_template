# SAS Kuka Control Template

> [!TIP]
> Repository for this template: https://github.com/MarinhoLab/sas_kuka_control_template \
> More information about SmartArmStack is available in https://smartarmstack.github.io/.

This is a control template for [KUKA](https://www.kuka.com/en-gb/products/robotics-systems) robotic manipulators. It relies on [`sas_robot_driver_kuka`](https://github.com/MarinhoLab/sas_robot_driver_kuka) to communicate
with the robot via [Sunrise.FRI](https://my.kuka.com/s/category/software/system-software-extension/kuka-sunrise-extensions/kuka-sunrisefri/0ZG1i000000XapDGAS?language=en_US).

## Docker

### Simulation


https://github.com/user-attachments/assets/d0c00b59-8b45-4c11-9c85-6ec9807eda97


Run

```commandline
mkdir -p ~/sas_tutorial_workspace/docker/kuka_control_template/simulation_demo
cd ~/sas_tutorial_workspace/docker/kuka_control_template/simulation_demo
curl -OL https://raw.githubusercontent.com/MarinhoLab/sas_kuka_control_template/refs/heads/main/.devel/simulation_demo/compose.yml

xhost +local:root
docker compose up
```

### Real robot

TODO

## Unreliable network profiles

If the wired connection is in the `Connecting` status, it fails randomly, frequently, and fast. This is followed by a `Connection failure` Ubuntu error that pops up.
To solve it permanently, in the system admin account, I deleted the wired network profile and redefined it with the correct configuration.
