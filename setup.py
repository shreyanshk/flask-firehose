#!/usr/bin/env python

"""
Flask-Firehose
--------------

HTTP/2 Server Push for your Flask apps.
"""
from setuptools import setup


with open("README.rst", 'rt', encoding='utf8') as f:
    readme = f.read()


setup(
    name='Flask-Firehose',
    version='0.2.2',
    url='https://github.com/shreyanshk/flask-firehose',
    license='MIT',
    author='Shreyansh Khajanchi',
    author_email='hello@shreyanshja.in',
    description='HTTP/2 Server Push for your Flask apps.',
    long_description=readme,
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
