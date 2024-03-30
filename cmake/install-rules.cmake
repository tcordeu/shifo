install(
    TARGETS shifo_exe
    RUNTIME COMPONENT shifo_Runtime
)

if(PROJECT_IS_TOP_LEVEL)
  include(CPack)
endif()
