# This is for use with ROS catkin only.

cmake_minimum_required(VERSION 2.8.3)
project(pypcd)

find_package(catkin_simple REQUIRED)

catkin_simple(ALL_DEPS_REQUIRED)

catkin_python_setup()

cs_export()

catkin_install_python(PROGRAMS pypcd/pypcd.py
                               DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
