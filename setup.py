#!/usr/bin/env python

# This is for use with ROS catkin only.

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['pypcd','numpy_pc2'],
    package_dir={'': 'src'},
)

setup(**d)
