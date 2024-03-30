cmake_minimum_required(VERSION 3.21)

include(cmake/prelude.cmake)

project(
    shifo
    VERSION 0.1.0
    DESCRIPTION "Yet another DB!"
    HOMEPAGE_URL "https://github.com/tcordeu"
    LANGUAGES C
)

include(cmake/variables.cmake)

# ---- Declare library ----

add_library(
    shifo_lib OBJECT
    source/lib.c
)

target_include_directories(
    shifo_lib ${warning_guard}
    PUBLIC
    "\$<BUILD_INTERFACE:${PROJECT_SOURCE_DIR}/source>"
)

target_compile_features(shifo_lib PUBLIC c_std_23)

find_package(json-c REQUIRED)
target_link_libraries(shifo_lib PRIVATE json-c::json-c)

# Unfortunately, hedley provides no CMake package to be found trivially using
# find_package, so it has to be found manually
find_path(HEDLEY_INCLUDE_DIR hedley.h REQUIRED)
target_include_directories(
    shifo_lib SYSTEM
    PRIVATE "${HEDLEY_INCLUDE_DIR}"
)

# ---- Declare executable ----

add_executable(shifo_exe source/main.c)
add_executable(shifo::exe ALIAS shifo_exe)

set_property(TARGET shifo_exe PROPERTY OUTPUT_NAME shifo)

target_compile_features(shifo_exe PRIVATE c_std_23)

target_link_libraries(shifo_exe PRIVATE shifo_lib)

# ---- Install rules ----

if(NOT CMAKE_SKIP_INSTALL_RULES)
  include(cmake/install-rules.cmake)
endif()

# ---- Developer mode ----

if(NOT shifo_DEVELOPER_MODE)
  return()
elseif(NOT PROJECT_IS_TOP_LEVEL)
  message(
      AUTHOR_WARNING
      "Developer mode is intended for developers of shifo"
  )
endif()

include(cmake/dev-mode.cmake)
