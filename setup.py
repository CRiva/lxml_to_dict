#!/usr/bin/env python3
from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

setup(name='lxml_to_dict',
      version="0.1.2",
      description='A simple conversion of an lxml.objectify element to a python dictionary.',
      packages=find_packages('lib'),
      package_dir={'': 'lib'},
      author='Connor Riva',
      author_email='criva@westmont.edu',
      url='https://github.com/CRiva/lxml_to_dict',
      py_modules=[splitext(basename(path))[0] for path in glob('lib/*.py')],
      keywords=['lxml', 'dict', 'dictionary', 'lxml.objectify', 'convert'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      )
