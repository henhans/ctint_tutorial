include_directories(${CMAKE_SOURCE_DIR}/c++ ${TRIQS_INCLUDE_ALL})

add_library(ctint_tutorial_c ctint.cpp)
target_link_libraries(ctint_tutorial_c ${TRIQS_LIBRARY_ALL})
triqs_set_rpath_for_target(ctint_tutorial_c)

install(TARGETS ctint_tutorial_c DESTINATION lib)

