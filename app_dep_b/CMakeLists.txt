cmake_minimum_required(VERSION 3.15)
project(app_dep_b)

find_package(lib_b_dep_a REQUIRED)

add_executable(app_dep_b main.cpp)
target_link_libraries(app_dep_b lib_b_dep_a::lib_b_dep_a)

