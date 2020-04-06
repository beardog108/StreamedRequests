from setuptools import setup, find_packages

setup(name='streamedrequests',
      version='1.0.2',
      description='Library for streaming http get or post request\'s responses',
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
