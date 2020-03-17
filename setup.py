#!/usr/bin/env python
from setuptools import setup

try:
    from testr.setup_helper import cmdclass
except ImportError:
    cmdclass = {}

entry_points = {'console_scripts': 'fep1_mong_check = fep1_mong_check.fep1_mong_check:main'}

setup(name='fep1_mong_check',
      packages=["fep1_mong_check"],
      use_scm_version=True,
      setup_requires=['setuptools_scm', 'setuptools_scm_git_archive'],
      description='ACIS Thermal Model for FEP1 Mongoose Temperature',
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/acisops/fep1_mong_check',
      include_package_data=True,
      entry_points=entry_points,
      zip_safe=False,
      tests_require=["pytest"],
      cmdclass=cmdclass,
      )
