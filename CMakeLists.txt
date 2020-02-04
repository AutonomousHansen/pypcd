# This is for use with ROS catkin only.

cmake_minimum_required(VERSION 2.8.3)
project(pypcd)

find_package(catkin_simple REQUIRED)

catkin_python_setup()

catkin_simple(ALL_DEPS_REQUIRED)

catkin_install_python(PROGRAMS src/pypcd/pypcd.py
                               src/pypcd/pdutil.py
                               src/pypcd/sautil.py
                               src/pypcd/nea_pc_format.py
                               src/numpy_pc2/numpy_pc2.py
                               DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

cs_export()
