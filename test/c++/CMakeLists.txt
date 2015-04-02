include_directories(${CMAKE_SOURCE_DIR}/c++ ${TRIQS_INCLUDE_ALL})

add_executable(anderson_c anderson_c.cpp)
target_link_libraries(anderson_c ctint_tutorial_c ${TRIQS_LIBRARY_ALL})
triqs_set_rpath_for_target(anderson_c)

triqs_add_test_C_hdf(anderson_c " -d 1.e-7")
