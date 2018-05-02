#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

try:
    long_description = open('README.rst').read()
except:
    long_description = ''

setup(
    name='nessus_report_parser',
    version="0.2.3",
    description='A wrapper around the tapioca-nessus_report_parser for translating the'
                ' Nessus API documents into Python Objects',
    long_description=long_description,
    author="Flávio Cardoso Ferreira Pontes",
    author_email="flavio.pontes@siteblindado.com.br",
    url='https://github.com/siteblindado/nessus_report_parser-report-nessus_parser',
    packages=['nessus_parser', ],
    package_dir={'nessus_parser': 'nessus_parser'},
    package_data={
        '': ['LICENSE.txt', 'README.rst']
    },
    include_package_data=True,
    install_requires=[
        'tapioca-nessus',
        'lxml'
    ],
    license="MIT",
    zip_safe=False,
    keywords='nessus',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
