#!/usr/bin/env python

from distutils.core import setup

def readme():
    with open('readme.md') as f:
        return f.read()

setup(name='Splunk-HEC',
      version='1.5',
      description='This is a python class file for use with other python scripts to send events to a Splunk http event collector.',
      long_description=readme(),
      author='George (starcher) Starcher',
      author_email='george@georgestarcher.com',
      url='https://github.com/georgestarcher/Splunk-Class-httpevent',
      py_modules=['splunk_http_event_collector'],
      keywords="splunk hec",
      license="MIT",
      install_requires=[
          'requests'
      ],
     )
