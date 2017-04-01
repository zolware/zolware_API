#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
try:
    from setuptools import setup
except ImportError:
    print("Couldn't import setuptools. Falling back to distutils.")
    from distutils.core import setup
from distutils.util import convert_path


if os.path.exists('LICENSE'):
    print("The setup.py script should be executed from the build directory.")
    sys.exit(1)

main_ns = {}
ver_path = convert_path('zolware/__init__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

setup(
    name='zolware',
    version=main_ns['__version__'],
    author='Francois Roy',
    author_email='francois@zolware.com',
    description=("API for the core product."),
    license='BSD-2',
    keywords="Structural Health Monitoring",
    url='https://github.com/zolware/zolware_API',
    packages=['zolware', 'filterpy', 'tests'],
    package_dir={'zolware':
                 'zolware'},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'zolware = zolware.command_line:main',
        ]
    },
    setup_requires=['pytest-runner', ],
    install_requires=[
            'click',
            'numpy',
            'scipy',
            ],
    test_suite='tests.test_class',
    tests_require=['pytest', ],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    )
