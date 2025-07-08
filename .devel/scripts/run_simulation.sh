#!/bin/bash
set -e

# Run CoppeliaSim, start simulation, and auto quit
# https://manual.coppeliarobotics.com/en/commandLine.htm
cd "$COPPELIASIM_PATH"
./coppeliaSim.sh \
-s0 \
"$HOME"/sas_tutorial_workspace/src/sas_kuka_control_template/scenes/KUKAR820_470rev4.ttt
