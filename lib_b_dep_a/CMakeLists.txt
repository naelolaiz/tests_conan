cmake_minimum_required(VERSION 3.15)
project(lib_b_dep_a)

find_package(lib_a_nodeps REQUIRED)

add_library(lib_b_dep_a LibB.cpp LibB.h)
target_link_libraries(lib_b_dep_a lib_a_nodeps)

