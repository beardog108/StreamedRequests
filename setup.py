from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'Readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='streamedrequests',
      version='1.0.3',
      description='Library for streaming http get or post request\'s responses',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Kevin Froman',
      author_email='beardog@mailbox.org',
      url='https://github.com/beardog108/StreamedRequests',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=['requests'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
      ],
     )
