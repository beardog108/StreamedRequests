from distutils.core import setup

setup(name='streamedrequests',
      version='0.0.0',
      description='Library for streaming http get or post request\'s responses',
      author='Kevin Froman',
      author_email='beardog@mailbox.org',
      url='https://github.com/beardog108/streamedrequests',
      packages=['streamedrequests'],
      install_requires=['requests'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
      ],
     )
