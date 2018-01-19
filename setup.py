#!/usr/bin/env python

from distutils.core import setup

appname = 'elks'

setup(
    name=appname,
    version='1.1.0',
    description='Python bindings for 46elks API.',
    author='Gustaf Hansen',
    author_email='gustaf@linkura.se',
    url='https://github.com/Linkura/elks',
    packages=['elks'],
    platforms=['any'],
    scripts=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Telephony',
    ],
    install_requires=['requests>=1.0'],
)
