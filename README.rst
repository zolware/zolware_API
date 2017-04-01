===========
Zolware API
===========

.. image:: https://travis-ci.org/zolware/zolware_API.svg?branch=master
    :target: https://travis-ci.org/zolware/zolware_API
.. image:: https://codecov.io/github/zolware/zolware_API/coverage.svg?branch=master
    :target: https://codecov.io/github/zolware/zolware_API/coverage.svg?branch=master

- Licensed under MIT

Structural Health Monitoring 

Requirements
------------

- Unix system with Python 2.7/3.6
- cmake


Download and test
-----------------

1. git clone `https://github.com/zolware/zolware_API.git <https://github.com/zolware/zolware_API.git>`_
2. cd zolware_API
3. pip install --upgrade wheel setuptools pip
4. pip install -r requirements/development.txt
5. mkdir build && cd build
6. pip install -e .
7. cmake ..
8. make
9. ctest --verbose
