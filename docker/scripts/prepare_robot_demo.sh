#!/bin/bash
set -e

# Update repository and set FASTRTPS profile to run over UDP when net=host.
cd /root/sas_tutorial_workspace/src/sas_kuka_control_template
git pull
export FASTRTPS_DEFAULT_PROFILES_FILE=/root/sas_tutorial_workspace/src/sas_kuka_control_template/.devel/scripts/fastrtps_profile.xml

# Build workspace
colcon build
source install/setup.bash

# Show countdown
cd /root/sas_tutorial_workspace/src/sas_kuka_control_template/.devel/scripts/
./countdown.sh 10

