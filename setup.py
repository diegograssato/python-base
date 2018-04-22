#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# setup parameters
setup(name='dtux',
      version='0.14',
      description='Sample application',
      long_description=readme,
      author='Diego',
      include_package_data=True,
      url='https://github.com/diegograssato/samplemod',
      license=license,
      packages=find_packages(exclude=('tests', 'docs')),
      author_email='diego@gmail.com',
      classifiers=["Programming Language :: Python :: 3.5",
                   'Programming Language :: Python',
                   ],
      scripts=['bin/wph-network-test'],
      entry_points={
          'console_scripts': ['dtux_app = tasks.example:execute']}
      )
