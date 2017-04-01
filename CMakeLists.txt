cmake_minimum_required (VERSION 3.2)
project (zolware)

set(CMAKE_BUILD_TYPE Release)
# Debugging Options
set (CMAKE_VERBOSE_MAKEFILE 0) # Use 1 for debugging, 0 otherwise.

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake )
set(CMAKE_CONFIG_PATH ${PROJECT_SOURCE_DIR}/cmake.config)

add_custom_target( ReplicatePythonSourceTree ALL ${CMAKE_COMMAND} -P
  ${CMAKE_CURRENT_SOURCE_DIR}/cmake/ReplicatePythonSourceTree.cmake
  ${CMAKE_CURRENT_BINARY_DIR}
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} )

add_subdirectory(${PROJECT_NAME})

include(CTest)
add_subdirectory(tests)