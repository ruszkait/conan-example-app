cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR)

project(dena_app)

## update paths for find_package calls
list(APPEND CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR})
list(APPEND CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR})

add_executable(${PROJECT_NAME})

## compile
target_sources(${PROJECT_NAME}
PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cc
)

## link
find_package(dena_library)
if(TARGET dena_library::dena_library)
    target_link_libraries(${PROJECT_NAME} PRIVATE dena_library::dena_library)
endif()

## install
install(TARGETS ${PROJECT_NAME} DESTINATION bin)