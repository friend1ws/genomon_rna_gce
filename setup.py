#!/usr/bin/env python

from distutils.core import setup

setup(name='genomon_rna_gce',
      version='0.1.0',
      description='Python tools for executing Genomon RNA pipeline in Google Compute Engine.',
      author='Yuichi Shiraishi',
      author_email='friend1ws@gamil.com',
      url='https://github.com/friend1ws/genomon_rna_gce',
      package_dir = {'': 'lib'},
      packages=['genomon_rna_gce'],
      scripts=['genomon_rna_gce'],
      license='MIT'
     )

