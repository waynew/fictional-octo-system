#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='simple_crud',
    version='0.1.0',
    description='Just a simple CRUD application using web2py',
    long_description=readme,
    author='Wayne Werner',
    author_email='waynejwerner@gmail.com',
    url='https://github.com/waynew/fictional-octo-system',
    packages=[
        'simple_crud',
    ],
    entry_points={
        'console_scripts': [
            'simple-crud = simple_crud.app:run',
        ],
    },
    cmdclass={'test': PyTest},
    package_dir={'simple_crud': 'simple_crud'},
    include_package_data=True,
    install_requires=['web2py'
    ],
    license="MIT",
    zip_safe=False,
    keywords='draft flask blog publish static-site',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
    ],
    test_suite='tests',
    tests_require=['pytest', 'hypothesis', 'pytest-cov'],
)
