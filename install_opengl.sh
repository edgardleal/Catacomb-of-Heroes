#!/bin/bash -       
#title           :install_opengl.sh
#description     :This script will install all libraries needed to run OpenGL
#author          :Edgard Leal <edgardleal@gmail.com>
#date            :20170521
#version         :0.1    
#usage           :bash install_opengl.sh
#notes           :
#bash_version    :4.1.5(1)-release
#==============================================================================
set -eu

sudo apt-get update
sudo apt-get install freeglut3
sudo apt-get install freeglut3-dev
sudo apt-get install binutils-gold
sudo apt-get install g++ cmake
sudo apt-get install libglew-dev
sudo apt-get install g++
sudo apt-get install mesa-common-dev
sudo apt-get install build-essential
sudo apt-get install libglew1.5-dev libglm-dev

exit 0
