# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include;/usr/include/eigen3".split(';') if "${prefix}/include;/usr/include/eigen3" != "" else []
PROJECT_CATKIN_DEPENDS = "roscpp;robotis_manipulator;dynamixel_workbench_toolbox;cmake_modules".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lopen_manipulator_p_libs".split(';') if "-lopen_manipulator_p_libs" != "" else []
PROJECT_NAME = "open_manipulator_p_libs"
PROJECT_SPACE_DIR = "/home/gabriele/catkin_ws/install"
PROJECT_VERSION = "1.0.0"
