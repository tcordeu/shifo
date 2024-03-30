# Parent project does not export its library target, so this CML implicitly
# depends on being added from it, i.e. the testing is done only from the build
# tree and is not feasible from an install location

project(shifoTests LANGUAGES CXX)

# ---- Dependencies ----

find_package(Catch2 REQUIRED)
include(Catch)

# ---- Tests ----

add_executable(shifo_test source/shifo_test.cpp)
target_link_libraries(
    shifo_test PRIVATE
    shifo_lib
    Catch2::Catch2WithMain
)
target_compile_features(shifo_test PRIVATE cxx_std_11)

catch_discover_tests(shifo_test)

# ---- End-of-file commands ----

add_folders(Test)
