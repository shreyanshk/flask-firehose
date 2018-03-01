#!/usr/bin/env python

"""
Flask-Firehose
--------------

HTTP/2 Server Push for your Flask apps.
"""
from setuptools import setup


setup(
    name='Flask-Firehose',
    version='0.1',
    url='https://github.com/shreyanshk/flask-firehose',
    license='See License',
    author='Shreyansh Khajanchi',
    author_email='hello@shreyanshja.in',
    description='HTTP/2 Server Push for your Flask apps.',
    long_description=__doc__,
    py_modules=['flask_firehose'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask>=0.10'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
