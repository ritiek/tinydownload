#!/usr/bin/env python

from setuptools import setup, find_packages
import tinydownload

with open("README.rst", "r") as f:
    long_description = f.read()

setup(name='tinydownload',
      version=tinydownload.__version__,
      description='Download files from tinyupload.com',
      long_description=long_description,
      author='Ritiek Malhotra',
      author_email='ritiekmalhotra123@gmail.com',
      packages = find_packages(),
      entry_points={
            'console_scripts': [
                  'tinydownload = tinydownload.tinydownload:command_line',
            ]
      },
      url='https://www.github.com/ritiek/tinydownload',
      keywords=['quora', 'terminal', 'command-line', 'question', 'python'],
      license='MIT',
      download_url='https://github.com/ritiek/tinydownload/archive/v' + tinydownload.__version__ + '.tar.gz',
      classifiers=[],
      install_requires=[
            'requests',
            'BeautifulSoup4',
      ]
     )
