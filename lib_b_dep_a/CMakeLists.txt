cmake_minimum_required(VERSION 3.15)
project(lib_b_dep_a)

find_package(lib_a_nodeps REQUIRED)

add_library(${PROJECT_NAME} LibB.cpp LibB.h)
target_link_libraries(${PROJECT_NAME} PUBLIC lib_a_nodeps::lib_a_nodeps)

# Specify the public headers
set_target_properties(${PROJECT_NAME} PROPERTIES PUBLIC_HEADER LibB.h)

# Install rules
install(TARGETS ${PROJECT_NAME}
        LIBRARY DESTINATION lib
        ARCHIVE DESTINATION lib
        PUBLIC_HEADER DESTINATION include)

