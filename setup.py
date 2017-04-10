#!/usr/bin/env python
from setuptools import setup
from fep1mong_check import __version__

entry_points = {'console_scripts': 'fep1mong_check = fep1mong_check.fep1mong_check:main'}

url = 'https://github.com/acisops/fep1mong_check/tarball/{}'.format(__version__)

setup(name='fep1mong_check',
      packages=["fep1mong_check"],
      version=__version__,
      description='ACIS Thermal Model for FEP1 Mongoose Temperature',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/fep1mong_check',
      download_url=url,
      include_package_data=True,
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
      ],
      entry_points=entry_points,
      )
