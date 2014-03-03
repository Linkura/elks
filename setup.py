#!/usr/bin/env python

from distutils.core import setup

appname = 'elks'
version = __import__(appname).__version__

setup(
    name=appname,
    version=version,
    description='Python bindings for 46elks API.',
    author='Gustaf Hansen',
    author_email='gustaf@linkura.se',
    url='https://github.com/Linkura/elks',
    packages=['elks'],
    platforms=['any'],
    scripts=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Telephony',
    ],
    requires=['requests (>=1.0)'],
)
