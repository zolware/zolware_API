# Note: when executed in the build dir, then CMAKE_CURRENT_SOURCE_DIR is the
# build dir.
file( COPY zolware filterpy tests DESTINATION "${CMAKE_ARGV3}"
  FILES_MATCHING PATTERN "*.py" PATTERN "*.pyx" PATTERN "*.pxd" )
file( COPY setup.py README.rst setup.cfg pytest.ini .coveragerc MANIFEST.in tox.ini DESTINATION "${CMAKE_ARGV3}" )
