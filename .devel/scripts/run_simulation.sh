#!/bin/bash
set -e

SCENE_DIR="$HOME"/sas_tutorial_workspace/src/sas_kuka_control_template/scenes
ls "${SCENE_DIR}"

# Run CoppeliaSim, start simulation, and auto quit
# https://manual.coppeliarobotics.com/en/commandLine.htm
cd "$COPPELIASIM_PATH"
./coppeliaSim.sh \
-s0 \
"${SCENE_DIR}"/KUKAR820_470rev4.ttt
